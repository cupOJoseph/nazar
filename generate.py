#generate a random image of an Eye and put it in the export folder.
# Import required libraries
import os
import random
import json
from pathlib import Path
from PIL import Image, ImageDraw
import cairosvg
import io
import hashlib


#generate 3333 Eyes     

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

]

iris_colors = [

]

pupil_colors = [
    030309, 
    00243e
    3f3f7d
    280171
    714400
    000057
    1d3100
    00223a
    002d29
]

    """Load image file (PNG or SVG)"""
    path = Path(image_path)
    if not path.exists():
        print(f"Warning: Image not found: {image_path}")
        return None
        
    if path.suffix.lower() == '.svg':
        return load_svg_as_image(path)
    else:
        try:
            return Image.open(path).convert("RGBA")
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None


def main():
    """Main function"""
    print("Eye Image Generator")
    print("=" * 50)
    
    # Check if required packages are available
    try:
        import PIL
        import cairosvg
    except ImportError as e:
        print(f"Error: Missing required package: {e}")
        print("Please install required packages:")
        print("pip install Pillow cairosvg")
        return
    
    # Generate all images
    generate_all_images(3333)

if __name__ == "__main__":
    main()








