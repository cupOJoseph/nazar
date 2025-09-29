# resize everything in ./malocchios to 900px and export into ./900px/

import os
from PIL import Image

# get all the images in ./malocchios
images = [f for f in os.listdir("./malocchios") if f.endswith(".png")]

i = 0

# resize each image to 900px
for image in images:
    if i % 100 == 0:
        print(f"Resizing image {i+1} of {len(images)}")
    i += 1
    img = Image.open(f"./malocchios/{image}")
    img = img.resize((900, 900))
    img.save(f"./900px/{image}")