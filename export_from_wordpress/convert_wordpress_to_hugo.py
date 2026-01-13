#!/usr/bin/env python3
"""
Convert WordPress XML export to Hugo markdown posts
"""
import xml.etree.ElementTree as ET
import re
from pathlib import Path
from datetime import datetime
import html

# WordPress namespaces
namespaces = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/'
}

def clean_content(content):
    """Clean and convert WordPress content to markdown"""
    if not content:
        return ""
    
    # Decode HTML entities
    content = html.unescape(content)
    
    # Remove <!--more--> tags
    content = re.sub(r'<!--more-->', '', content)
    
    # Remove WordPress block comments
    content = re.sub(r'<!-- wp:[^>]+ -->', '', content)
    content = re.sub(r'<!-- /wp:[^>]+ -->', '', content)
    
    # Convert WordPress code blocks to markdown
    # [code language="python"]...[/code] -> ```python\n...\n```
    content = re.sub(
        r'\[code language="([^"]+)"\](.*?)\[/code\]',
        r'```\1\n\2\n```',
        content,
        flags=re.DOTALL
    )
    
    # Convert simple [code]...[/code] to code blocks
    content = re.sub(
        r'\[code\](.*?)\[/code\]',
        r'```\n\1\n```',
        content,
        flags=re.DOTALL
    )
    
    # Convert [caption]...[/caption] - just remove the tags
    content = re.sub(
        r'\[caption[^\]]*\](.*?)\[/caption\]',
        r'\1',
        content,
        flags=re.DOTALL
    )
    
    # Convert WordPress image blocks to markdown images
    # <figure class="wp-block-image"><img src="URL" alt="ALT" /></figure>
    content = re.sub(
        r'<figure[^>]*class="wp-block-image[^>]*>.*?<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>.*?</figure>',
        r'![\2](\1)',
        content,
        flags=re.DOTALL
    )
    
    # Convert simple HTML images to markdown
    content = re.sub(
        r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>',
        r'![\2](\1)',
        content
    )
    
    # Extract images from complex gallery blocks
    # <figure class="coblocks-gallery--figure">![...](url)</figure>
    content = re.sub(
        r'<figure[^>]*>(\!\[[^\]]*\]\([^)]+\))</figure>',
        r'\n\n\1\n\n',
        content
    )
    
    # Convert HTML links to markdown
    content = re.sub(
        r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        r'[\2](\1)',
        content,
        flags=re.DOTALL
    )
    
    # Remove paragraph tags but keep content
    content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Remove gallery and list wrapper tags but keep content
    content = re.sub(r'<(?:div|ul|li)[^>]*>(.*?)</(?:div|ul|li)>', r'\1', content, flags=re.DOTALL)
    
    # Remove other common HTML tags
    content = re.sub(r'</?(?:div|span|strong|em|br\s*/?|ul|li|figure)>', '', content)
    
    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def parse_wordpress_xml(xml_file):
    """Parse WordPress XML and extract posts"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    posts = []
    
    for item in root.findall('.//item'):
        # Check if this is a post (not a page or attachment)
        post_type = item.find('wp:post_type', namespaces)
        status = item.find('wp:status', namespaces)
        
        if (post_type is not None and post_type.text == 'post' and
            status is not None and status.text == 'publish'):
            
            title_elem = item.find('title')
            title = title_elem.text if title_elem is not None and title_elem.text else "Untitled"
            
            # Get post date
            post_date_elem = item.find('wp:post_date', namespaces)
            if post_date_elem is not None and post_date_elem.text:
                post_date = datetime.strptime(post_date_elem.text, '%Y-%m-%d %H:%M:%S')
            else:
                post_date = datetime.now()
            
            # Get content
            content_elem = item.find('content:encoded', namespaces)
            content = content_elem.text if content_elem is not None else ""
            
            # Get excerpt
            excerpt_elem = item.find('excerpt:encoded', namespaces)
            excerpt = excerpt_elem.text if excerpt_elem is not None else ""
            
            # Get categories and tags
            categories = []
            tags = []
            for category in item.findall('category'):
                domain = category.get('domain')
                term = category.text
                if term:
                    if domain == 'category':
                        categories.append(term)
                    elif domain == 'post_tag':
                        tags.append(term)
            
            # Get slug
            post_name_elem = item.find('wp:post_name', namespaces)
            slug = post_name_elem.text if post_name_elem is not None and post_name_elem.text else slugify(title)
            
            posts.append({
                'title': title,
                'date': post_date,
                'slug': slug,
                'content': clean_content(content),
                'excerpt': clean_content(excerpt),
                'categories': categories,
                'tags': tags
            })
    
    return posts

def create_hugo_post(post, output_dir):
    """Create a Hugo markdown post file"""
    # Create filename from date and slug
    date_str = post['date'].strftime('%Y-%m-%d')
    filename = f"{date_str}-{post['slug']}.md"
    filepath = output_dir / filename
    
    # Build frontmatter
    frontmatter = ['---']
    frontmatter.append(f'title: "{post["title"]}"')
    frontmatter.append(f'date: {post["date"].strftime("%Y-%m-%dT%H:%M:%S")}')
    frontmatter.append('draft: false')
    
    if post['tags']:
        tags_str = ', '.join([f'"{tag}"' for tag in post['tags']])
        frontmatter.append(f'tags: [{tags_str}]')
    
    if post['categories']:
        cats_str = ', '.join([f'"{cat}"' for cat in post['categories']])
        frontmatter.append(f'categories: [{cats_str}]')
    
    frontmatter.append('---')
    frontmatter.append('')
    
    # Combine frontmatter and content
    full_content = '\n'.join(frontmatter) + '\n' + post['content']
    
    # Write file
    filepath.write_text(full_content, encoding='utf-8')
    print(f"Created: {filename}")
    
    return filepath

def main():
    xml_file = Path('/home/wdecoster/repos/gigabaseorgigabyte/gigabaseorgigabyte.WordPress.2026-01-13.xml')
    output_dir = Path('/home/wdecoster/repos/gigabaseorgigabyte/content/posts')
    
    print(f"Parsing WordPress XML: {xml_file}")
    posts = parse_wordpress_xml(xml_file)
    
    print(f"\nFound {len(posts)} published posts")
    print("\nConverting to Hugo markdown...\n")
    
    for post in posts:
        create_hugo_post(post, output_dir)
    
    print(f"\n✓ Converted {len(posts)} posts to Hugo format")
    print(f"  Output directory: {output_dir}")

if __name__ == '__main__':
    main()
