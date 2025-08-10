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

## Layers for Eyes
##TODO: add file names or colors for vectors to the list
colors = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 0, 255),    # Magenta
    (0, 255, 255),    # Cyan
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 192, 203),  # Pink
    (165, 42, 42),    # Brown
    (0, 128, 0),      # Dark Green
    (128, 0, 0),      # Dark Red
    (0, 0, 128),      # Dark Blue
    (255, 215, 0),    # Gold
    (192, 192, 192)   # Silver
]
layer1 = []
layer2 = []
layer3 = []
layer4 = []
layer5 = []
backgrounds = []


def load_svg_as_image(svg_path, size=(800, 800)):
    """Convert SVG to PIL Image"""
    try:
        # Convert SVG to PNG bytes
        png_data = cairosvg.svg2png(url=str(svg_path), output_width=size[0], output_height=size[1])
        # Convert bytes to PIL Image
        return Image.open(io.BytesIO(png_data)).convert("RGBA")
    except Exception as e:
        print(f"Error loading SVG {svg_path}: {e}")
        # Return a fallback image
        fallback = Image.new("RGBA", size, (255, 255, 255, 0))
        return fallback

def load_image(image_path):
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

def create_random_background(size=(800, 800)):
    """Create a random background with patterns or gradients"""
    background = Image.new("RGBA", size, (255, 255, 255, 255))
    draw = ImageDraw.Draw(background)
    
    # Random background style
    style = random.choice(["solid", "gradient", "pattern", "noise"])
    
    if style == "solid":
        color = random.choice(colors)
        background = Image.new("RGBA", size, color + (255,))
        
    elif style == "gradient":
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        for y in range(size[1]):
            ratio = y / size[1]
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(0, y), (size[0], y)], fill=(r, g, b, 255))
            
    elif style == "pattern":
        color = random.choice(colors)
        for i in range(0, size[0], 50):
            for j in range(0, size[1], 50):
                if random.random() > 0.5:
                    draw.rectangle([i, j, i + 25, j + 25], fill=color + (255,))
                    
    elif style == "noise":
        for x in range(0, size[0], 10):
            for y in range(0, size[1], 10):
                if random.random() > 0.7:
                    color = random.choice(colors)
                    draw.ellipse([x, y, x + 10, y + 10], fill=color + (255,))
    
    return background

def generate_random_image(image_number, export_folder):
    """Generate a single random image"""
    size = (800, 800)
    
    # Start with a random background
    background = create_random_background(size)
    
    # Define available layers and backgrounds from the eye_layers folder
    available_layers = {
        "lens": ["eye_layers/Lens 1.png"],
        "malocchio": ["eye_layers/Malocchio 3/Lens 1.svg"],
        "backgrounds": ["eye_layers/Backdrop 1.svg", "eye_layers/Malocchio 3/Backdrop 1.svg"]
    }
    
    # Add random layers
    layers_to_add = []
    
    # Randomly decide which layers to include
    if random.random() > 0.3:  # 70% chance to add lens
        lens_choice = random.choice(available_layers["lens"])
        lens_img = load_image(lens_choice)
        if lens_img:
            layers_to_add.append(("lens", lens_img))
    
    if random.random() > 0.5:  # 50% chance to add malocchio
        malocchio_choice = random.choice(available_layers["malocchio"])
        malocchio_img = load_image(malocchio_choice)
        if malocchio_img:
            layers_to_add.append(("malocchio", malocchio_img))
    
    # Randomly decide whether to use a backdrop
    if random.random() > 0.4:  # 60% chance to use backdrop
        backdrop_choice = random.choice(available_layers["backgrounds"])
        backdrop_img = load_image(backdrop_choice)
        if backdrop_img:
            # Resize backdrop to fit
            backdrop_img = backdrop_img.resize(size, Image.Resampling.LANCZOS)
            background = Image.alpha_composite(background, backdrop_img)
    
    # Composite all layers
    final_image = background.copy()
    for layer_name, layer_img in layers_to_add:
        if layer_img:
            # Resize layer to fit
            layer_img = layer_img.resize(size, Image.Resampling.LANCZOS)
            
            # Randomly apply color filter
            if random.random() > 0.7:  # 30% chance
                color = random.choice(colors)
                color_layer = Image.new("RGBA", layer_img.size, color + (128,))  # 50% opacity
                layer_img = Image.alpha_composite(layer_img, color_layer)
            
            # Composite layer
            final_image = Image.alpha_composite(final_image, layer_img)
    
    # Generate unique filename
    timestamp = str(image_number).zfill(4)
    random_hash = hashlib.md5(f"{image_number}_{random.random()}".encode()).hexdigest()[:8]
    filename = f"eye_{timestamp}_{random_hash}.png"
    
    # Save image
    output_path = export_folder / filename
    final_image.save(output_path, "PNG")
    
    return output_path, filename

def generate_all_images(count=3333):
    """Generate all images"""
    # Create export folder
    export_folder = Path("export")
    export_folder.mkdir(exist_ok=True)
    
    print(f"Starting generation of {count} images...")
    print(f"Export folder: {export_folder.absolute()}")
    
    metadata = []
    
    for i in range(1, count + 1):
        try:
            output_path, filename = generate_random_image(i, export_folder)
            metadata.append({
                "image_number": i,
                "filename": filename,
                "output_path": str(output_path)
            })
            
            if i % 100 == 0:
                print(f"Generated {i}/{count} images...")
                
        except Exception as e:
            print(f"Error generating image {i}: {e}")
            continue
    
    # Save metadata
    metadata_path = export_folder / "generation_metadata.json"
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\nGeneration complete! {count} images created in {export_folder}")
    print(f"Metadata saved to {metadata_path}")

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








