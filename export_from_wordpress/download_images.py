#!/usr/bin/env python3
"""
Extract and download images from WordPress posts
"""
import re
from pathlib import Path
import requests
from urllib.parse import urlparse, unquote
import time

def extract_image_urls(posts_dir):
    """Extract all WordPress image URLs from markdown posts"""
    image_urls = set()
    
    for post_file in Path(posts_dir).glob('*.md'):
        content = post_file.read_text(encoding='utf-8')
        
        # Find all image links
        # Pattern: ![alt](url)
        matches = re.findall(r'!\[[^\]]*\]\((https://gigabaseorgigabyte\.wordpress\.com/[^)]+)\)', content)
        image_urls.update(matches)
    
    return sorted(image_urls)

def download_image(url, output_dir):
    """Download an image from URL to output directory"""
    try:
        # Get filename from URL
        parsed = urlparse(url)
        # Remove query parameters for filename
        path_without_query = parsed.path.split('?')[0]
        filename = Path(unquote(path_without_query)).name
        
        # Create output path
        output_path = output_dir / filename
        
        # Skip if already exists
        if output_path.exists():
            print(f"  ✓ Already exists: {filename}")
            return output_path, True
        
        # Download
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Save
        output_path.write_bytes(response.content)
        print(f"  ✓ Downloaded: {filename}")
        return output_path, True
        
    except Exception as e:
        print(f"  ✗ Failed: {url} - {e}")
        return None, False

def update_image_paths(posts_dir, images_dir):
    """Update image paths in posts to use local images"""
    for post_file in Path(posts_dir).glob('*.md'):
        content = post_file.read_text(encoding='utf-8')
        original_content = content
        
        # Find WordPress image URLs and replace with local paths
        def replace_url(match):
            alt_text = match.group(1)
            url = match.group(2)
            
            # Extract filename
            parsed = urlparse(url)
            path_without_query = parsed.path.split('?')[0]
            filename = Path(unquote(path_without_query)).name
            
            # Return new markdown with local path
            return f'![{alt_text}](/images/{filename})'
        
        content = re.sub(
            r'!\[([^\]]*)\]\((https://gigabaseorgigabyte\.wordpress\.com/[^)]+)\)',
            replace_url,
            content
        )
        
        # Only write if changed
        if content != original_content:
            post_file.write_text(content, encoding='utf-8')
            print(f"  Updated: {post_file.name}")

def main():
    posts_dir = Path('/home/wdecoster/repos/gigabaseorgigabyte/content/posts')
    images_dir = Path('/home/wdecoster/repos/gigabaseorgigabyte/static/images')
    
    # Create images directory if it doesn't exist
    images_dir.mkdir(parents=True, exist_ok=True)
    
    print("Extracting image URLs from posts...")
    image_urls = extract_image_urls(posts_dir)
    
    print(f"\nFound {len(image_urls)} unique images")
    
    if not image_urls:
        print("No images to download")
        return
    
    print("\n" + "="*60)
    user_input = input(f"\nDownload all {len(image_urls)} images? [y/N]: ")
    
    if user_input.lower() != 'y':
        print("\nImage URLs saved to image_urls.txt for manual download")
        with open('image_urls.txt', 'w') as f:
            for url in image_urls:
                f.write(url + '\n')
        print("\nYou can download them manually or with:")
        print("  wget -i image_urls.txt -P static/images/")
        return
    
    print("\nDownloading images...\n")
    success_count = 0
    fail_count = 0
    
    for i, url in enumerate(image_urls, 1):
        print(f"[{i}/{len(image_urls)}] {url}")
        _, success = download_image(url, images_dir)
        if success:
            success_count += 1
        else:
            fail_count += 1
        
        # Be nice to the server
        time.sleep(0.5)
    
    print(f"\n{'='*60}")
    print(f"Download complete: {success_count} succeeded, {fail_count} failed")
    
    if success_count > 0:
        print("\nUpdating image paths in posts to use local images...")
        update_image_paths(posts_dir, images_dir)
        print("\n✓ Image paths updated")

if __name__ == '__main__':
    main()
