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
