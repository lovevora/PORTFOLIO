import os

gallery_folder = 'images/gallery'
valid_exts = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.PNG', '.JPG', '.JPEG', '.GIF', '.WEBP')

try:
    images = [f for f in os.listdir(gallery_folder) if f.endswith(valid_exts)]
    
    print("Copy this into your gallery.js:")
    print("const images = [")
    for img in images:
        print(f"  'images/gallery/{img}',")
    print("];")
    
except Exception as e:
    print(f"Error: {e}")