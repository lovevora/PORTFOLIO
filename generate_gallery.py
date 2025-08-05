import os

gallery_folder = 'images/gallery'
output_file = 'gallery.js'

# List only image files
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
images.sort()  # optional, for consistent order

# Write JS array
with open(output_file, 'w') as f:
    f.write('const images = [\n')
    for img in images:
        f.write(f"  '{img}',\n")
    f.write('];\n')
