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

# get all the jsons in the jsons folder and load their content
json_files = [f for f in os.listdir("jsons") if f.endswith(".json")]
jsons = []

duplicatesList = [] # the number id of each matching one

for json_file in json_files:
    with open(f"jsons/{json_file}", "r") as f:
        jsons.append(json.load(f))

print(f"Loaded {len(jsons)} JSON files")

# check all the jsons in the jsons folder and print the ones that are the same
duplicates_found = 0
for i in range(len(jsons)):
    if i % 100 == 0:
        print(f"Checking jsons {i+1} of {len(jsons)}")
    for j in range(i+1, len(jsons)):
        if jsons[i]["attributes"] == jsons[j]["attributes"]:
            duplicates_found += 1
            print(f"DUPLICATE FOUND: {json_files[i]} and {json_files[j]} are the same")
            print(f"Attributes: {jsons[i]['attributes']}")
            print("--------------------------------")
            duplicatesList.append(i+1)
            duplicatesList.append(j+1)

print(f"Total duplicates found: {duplicates_found}")
print(f"Duplicates list: {duplicatesList}")

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

# randomly regenerate the duplicates
for i in range(len(duplicatesList)):
    if i % 100 == 0:
        print(f"Regenerating duplicates {i+1} of {len(duplicatesList)}")
    random.shuffle(duplicatesList)
    for j in range(i+1, len(duplicatesList)):
        if duplicatesList[i] == duplicatesList[j]:
            print(f"Regenerating duplicate {duplicatesList[i]}")
            regenerate_duplicate(duplicatesList[i])