# Gigabase or gigabyte

Hugo-based blog about bioinformatics and long-read sequencing.

## Local Development

```bash
# Start the Hugo development server
hugo server -D

# Build the site
hugo
```

## Deployment

This site is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the main branch.

## Converting from WordPress

1. Export your WordPress content from https://gigabaseorgigabyte.wordpress.com/
   - Go to Tools → Export → Select "All content"
   - Download the XML file

2. Convert WordPress export to Hugo markdown:
   ```bash
   # Option 1: Use wordpress-to-hugo-exporter
   # Install: pip install wordpress-to-hugo-exporter
   
   # Option 2: Use online converter or manual conversion
   ```

3. Place converted posts in `content/posts/`

4. Download and save images to `static/images/`

5. Update image paths in posts from WordPress URLs to local paths

## Theme

This site uses [Hermit-V2](https://github.com/1bl4z3r/hermit-V2), a minimal and fast Hugo theme designed for bloggers.

## License

Content: © 2020-2026 Wouter De Coster
Theme: [Hermit-V2 License](themes/hermit-v2/LICENSE)
