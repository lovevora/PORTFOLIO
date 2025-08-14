import os

gallery_folder = 'images/gallery'
valid_exts = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.PNG', '.JPG', '.JPEG', '.GIF', '.WEBP')

try:
    images = [f for f in os.listdir(gallery_folder) if f.endswith(valid_exts)]
    
    # Read existing gallery.js
    with open('gallery.js', 'r') as f:
        content = f.read()
    
    # Generate new images array
    new_images = "const images = [\n"
    for img in images:
        new_images += f"  'images/gallery/{img}',\n"
    new_images += "];"
    
    # Replace the old array
    import re
    updated_content = re.sub(r'const images = \[.*?\];', new_images, content, flags=re.DOTALL)
    
    # Write back to file
    with open('gallery.js', 'w') as f:
        f.write(updated_content)
    
    print(f"Updated gallery.js with {len(images)} images!")
    
except Exception as e:
    print(f"Error: {e}")