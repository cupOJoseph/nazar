# Eye Image Generator

A Python script that generates 3333 unique random eye images by combining different layers and backgrounds.

## Features

- **Random Layer Combination**: Combines different eye layers (lens, malocchio) with varying probabilities
- **Dynamic Backgrounds**: Creates random backgrounds with solid colors, gradients, patterns, and noise
- **Color Variations**: Applies random color filters to layers for additional uniqueness
- **SVG Support**: Handles both PNG and SVG files seamlessly
- **Metadata Tracking**: Records generation details for each image
- **Unique Naming**: Generates unique filenames with timestamps and hashes

## Requirements

- Python 3.7+
- Pillow (PIL)
- cairosvg

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Pillow cairosvg
```

## Usage

1. Ensure your folder structure is set up correctly:
```
nazar/
├── eye_layers/
│   ├── Lens 1.png
│   ├── Malocchio 3/
│   │   ├── Backdrop 1.svg
│   │   └── Lens 1.svg
│   └── Malocchio.zip
├── export/          # Output folder (created automatically)
├── generate.py      # Main script
└── requirements.txt
```

2. Run the generation script:
```bash
python generate.py
```

The script will:
- Create an `export` folder if it doesn't exist
- Generate 3333 unique images
- Save each image with a unique filename (e.g., `eye_0001_a1b2c3d4.png`)
- Create a `generation_metadata.json` file with details about each generated image
- Show progress every 100 images

## Output

- **Images**: 800x800 PNG files in the `export` folder
- **Metadata**: JSON file containing generation details for each image
- **Naming Convention**: `eye_XXXX_hash.png` where XXXX is the image number and hash is a unique identifier

## Customization

You can modify the script to:
- Change the number of images generated
- Adjust layer probabilities
- Add more color variations
- Modify background styles
- Change output image dimensions

## Troubleshooting

- **Missing packages**: Install required packages using `pip install -r requirements.txt`
- **SVG loading issues**: Ensure cairosvg is properly installed
- **Memory issues**: The script processes images one at a time to minimize memory usage

## Performance

- Generates approximately 100-200 images per minute (depending on system)
- Total generation time: ~15-30 minutes for 3333 images
- Memory usage: Low (processes one image at a time)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
