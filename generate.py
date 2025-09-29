#generate a random image of an Eye and put it in the export folder.
# Import required libraries
import os
import random
import json
from pathlib import Path
from PIL import Image, ImageDraw
# import cairosvg  # Commented out due to cairo library issues
import io
import hashlib


num_to_generate = 3333

# Background files from layers/backgrounds/ folder
backgrounds = [
    "Backdrop 1.png",
    "Backdrop 2.png", 
    "Backdrop 3.png",
    "Backdrop 4.png",
    "Backdrop 5.png",
    "Backdrop 6.png",
    "Backdrop 7.png",
    "Backdrop 8.png",
    "Backdrop 9.png"
]

# Layer files from each folder
lens = [
    "Lens 1 Sky.png",
    "Lens 1 Soil.png",
    "Lens 1.png",
    "Lens 2 Sky.png",
    "Lens 2 Soil.png",
    "Lens 2.png",
    "Lens 3 Sky.png",
    "Lens 3 Soil.png",
    "Lens 3.png",
    "Lens 4 Sky.png",
    "Lens 4 Soil.png",
    "Lens 4.png",
    "Lens 5 Sky.png",
    "Lens 5 Soil.png",
    "Lens 5.png",
    "Lens 6 Sky.png",
    "Lens 6 Soil.png",
    "Lens 6.png",
    "Lens 7 Sky.png",
    "Lens 7 Soil.png",
    "Lens 7.png",
    "Lens 8 Sky.png",
    "Lens 8 Soil.png",
    "Lens 8.png",
    "Lens 9 Sky.png",
    "Lens 9 Soil.png",
    "Lens 9.png"
]

sclera = [
    "Sclera 1.png",
    "Sclera 2.png",
    "Sclera 3.png",
    "Sclera 4.png",
    "Sclera 5.png",
    "Sclera 6.png",
    "Sclera 7.png",
    "Sclera 8.png",
    "Sclera 9.png"
]

iris = [
    "Iris 1 Saltwater.png",
    "Iris 1.png",
    "Iris 2 Saltwater.png",
    "Iris 2.png",
    "Iris 3 Saltwater.png",
    "Iris 3.png",
    "Iris 4 Saltwater.png",
    "Iris 4.png",
    "Iris 5 Saltwater.png",
    "Iris 5.png",
    "Iris 6 Saltwater.png",
    "Iris 6.png",
    "Iris 7 Saltwater.png",
    "Iris 7.png",
    "Iris 8 Saltwater.png",
    "Iris 8.png",
    "Iris 9 Saltwater.png",
    "Iris 9.png"
]

pupil = [
    "Pupil 1.png",
    "Pupil 2.png",
    "Pupil 3.png",
    "Pupil 4.png",
    "Pupil 5.png",
    "Pupil 6.png",
    "Pupil 7.png",
    "Pupil 8.png",
    "Pupil 9.png"
]

jsons = []

# Create jsons directory if it doesn't exist
os.makedirs("jsons", exist_ok=True)

def generate_eye(id):
    # Randomly select a background
    background = random.choice(backgrounds)

    # Randomly select a lens
    lens_file = random.choice(lens)

    # Randomly select a sclera 
    sclera_file = random.choice(sclera)

    # Randomly select an iris 
    iris_file = random.choice(iris)

    # Randomly select a pupil 
    pupil_file = random.choice(pupil)

    # Load background image
    background_image = Image.open(f"layers/Backdrop/{background}")
    
    # Load lens image
    lens_image = Image.open(f"layers/Lens/{lens_file}")
    
    # Load sclera image
    sclera_image = Image.open(f"layers/Sclera/{sclera_file}")
    
    # Load iris image
    iris_image = Image.open(f"layers/Iris/{iris_file}")
    
    # Load pupil image
    pupil_image = Image.open(f"layers/Pupil/{pupil_file}")

    # nft json
    eye_json = {
        "description": "An authentic Eye of Nazar.", 
        "image": "", 
        "name": "Malocchio",
        "attributes": [
            {
                "trait_type": "Backdrop", 
                "value": background
            },
            {
                "trait_type": "Lens", 
                "value": lens_file
            },
            {
                "trait_type": "Sclera", 
                "value": sclera_file
            },
            {
                "trait_type": "Iris", 
                "value": iris_file
            },
            {
                "trait_type": "Pupil", 
                "value": pupil_file
            }
        ]
    }
    eye_json["name"] = f"Malocchio {id:04d}"

    jsons.append(eye_json)
    
    # Combine layers
    combined_image = background_image.copy()
    combined_image.paste(lens_image, (0, 0), lens_image)    
    combined_image.paste(sclera_image, (0, 0), sclera_image)
    combined_image.paste(iris_image, (0, 0), iris_image)
    combined_image.paste(pupil_image, (0, 0), pupil_image)
    
    # Save the combined image malocchio0001.png
    output_filename = f"malocchio{id:04d}.png"
    combined_image.save(f"export/{output_filename}")
    # write json to file in ./jsons/malocchio#.json
    with open(f"jsons/malocchio{id:04d}.json", "w") as f:
        json.dump(eye_json, f)
    
    print(f"Generated {output_filename}")

# Generate random eye images
for i in range(num_to_generate):
    generate_eye(i+1)


duplicateList = []
# check if any of the jsons traits are the same and print the ones that are
for i in range(len(jsons)):
    if i % 10 == 0:
        print(f"Checking jsons {i+1} of {len(jsons)}")
    for j in range(i+1, len(jsons)):
        if jsons[i]["attributes"] == jsons[j]["attributes"]:
            print(f"Jsons {i+1} and {j+1} are the same")
            print(jsons[i]["attributes"])
            print(jsons[j]["attributes"])
            print("--------------------------------")
            duplicateList.append(i+1)
            duplicateList.append(j+1)

print(f"Duplicate list: {duplicateList}")

# while duplicateList is not empty
while duplicateList:
    #check if the duplicate is in the jsons list
    for i in range(len(jsons)):
        if i % 10 == 0:
            print(f"Checking jsons {i+1} of {len(jsons)}")
    for j in range(i+1, len(jsons)):
        if jsons[i]["attributes"] == jsons[j]["attributes"]:
            print(f"Jsons {i+1} and {j+1} are the same")
            print(jsons[i]["attributes"])
            print(jsons[j]["attributes"])
            print("--------------------------------")
            duplicateList.append(i+1)
            duplicateList.append(j+1)
    
    print(f"Regenerating duplicate {duplicateList[0]}")
    generate_eye(duplicateList.pop(0))
    print(f"Regenerating duplicate {duplicateList[0]}")
    generate_eye(duplicateList.pop(0))