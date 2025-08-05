import os
import random

gallery_folder = 'images/gallery'
output_file = 'gallery.js'

# List image files (case-insensitive matching)
valid_exts = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith(valid_exts)]

# Shuffle for random order
random.shuffle(images)

# Write JS array
with open(output_file, 'w') as f:
    f.write('// Auto-generated gallery image list\n')
    f.write('const images = [\n')
    for img in images:
        f.write(f"  '{img}',\n")
    f.write('];\n')
