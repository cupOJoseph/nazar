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


num_to_generate = 100

## Layers colors

lens_colors = [ 
    "#064cee",
    "#00477a",
    "#545df3",
    "#5402ee",
    "#ee8f00",
    "#0000ee",
    "#477a00",
    "#0067b0",
    "#00544d",
    ]

sclera_colors = [ 
    "#dfeffa",
    "#a7d8f5",
    "#dbdbfd",
    "#c5baee",
    "#eec86b",
    "#b2baee",
    "#c0ff8b",
    "#a1daff",
    "#adfff4",
]

iris_colors = [
    "#07a4f2",
    "#51b0f3",
    "#9faef9",
    "#8b70ee",
    "#eea706",
    "#7180ee",
    "#68b200",
    "#0095ff",
    "#47a1a4",
]

pupil_colors = [
    "#030309", 
    "#00243e",
    "#3f3f7d",
    "#280171",
    "#714400",
    "#000057",
    "#1d3100",
    "#00223a",
    "#002d29",
]

# Background files from layers/backgrounds/ folder
backgrounds = [
    "Group 1.png",
    "Group 2.png", 
    "Group 3.png",
    "Group 4.png",
    "Group 5.png",
    "Group 6.png",
    "Group 7.png",
    "Group 8.png",
    "Group 9.png"
]

# Layer files from each folder
lens_files = [
    "g1-1.svg",
    "g1-2.svg", 
    "g1-3.svg",
    "g1-4.svg",
    "g1-5.svg",
    "g1-6.svg",
    "g1-7.svg",
    "g1-8.svg",
    "g1.svg"
]

sclera_files = [
    "g1-1.svg",
    "g1-2.svg", 
    "g1-3.svg",
    "g1-4.svg",
    "g1-5.svg",
    "g1-6.svg",
    "g1-7.svg",
    "g1-8.svg",
    "g1.svg"
]

iris_files = [
    "g1-1.svg",
    "g1-2.svg", 
    "g1-3.svg",
    "g1-4.svg",
    "g1-5.svg",
    "g1-6.svg",
    "g1-7.svg",
    "g1-8.svg",
    "g1.svg"
]

pupil_files = [
    "g1-1.png",
    "g1-2.png", 
    "g1-3.png",
    "g1-4.png",
    "g1-5.png",
    "g1-6.png",
    "g1-7.png",
    "g1-8.png",
    "g1.png"
]

# Generate random eye images
for i in range(num_to_generate):
    # Randomly select a background
    background = random.choice(backgrounds)

    # Randomly select a lens color
    lens_color = random.choice(lens_colors)

    # Randomly select a sclera color
    sclera_color = random.choice(sclera_colors)

    # Randomly select an iris color
    iris_color = random.choice(iris_colors)

    # Randomly select a pupil color
    pupil_color = random.choice(pupil_colors)

    # Randomly select layer files
    lens_file = random.choice(lens_files)
    sclera_file = random.choice(sclera_files)
    iris_file = random.choice(iris_files)
    pupil_file = random.choice(pupil_files)

    # Load background image
    background_image = Image.open(f"layers/backgrounds/{background}")
    
    # For now, let's work with just the pupil layer since it's PNG
    # TODO: Fix SVG handling when cairo library is properly installed
    pupil = Image.open(f"layers/Pupil/{pupil_file}")
    
    # Create placeholder images for other layers (same size as pupil)
    lens = Image.new('RGBA', pupil.size, (0, 0, 0, 0))  # Transparent
    sclera = Image.new('RGBA', pupil.size, (0, 0, 0, 0))  # Transparent  
    iris = Image.new('RGBA', pupil.size, (0, 0, 0, 0))  # Transparent

    # Combine layers
    combined_image = background_image.copy()
    combined_image.paste(lens, (0, 0), lens)    
    combined_image.paste(sclera, (0, 0), sclera)
    combined_image.paste(iris, (0, 0), iris)
    combined_image.paste(pupil, (0, 0), pupil)
    
    
    # Save the combined image
    output_filename = f"eye_{i+1:04d}.png"
    combined_image.save(f"export/{output_filename}")
    
    print(f"Generated {output_filename}")