# Run this script with: `uv run noise-generator.py`
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
#     "pillow",
# ]
# ///

from pathlib import Path

import numpy as np
from PIL import Image


def main() -> None:
    width, height = 512, 512
    max_opacity = int(0.1 * 255)

    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    noise_data = np.random.randint(0, int(max_opacity) + 1, (height, width))

    for y in range(height):
        for x in range(width):
            opacity_value = noise_data[y, x]
            image.putpixel((x, y), (255, 255, 255, int(opacity_value)))

    file_path = Path(__file__).parent / "noise.png"
    image.save(file_path)

    print(f"Noise image generated and saved as {file_path}")


if __name__ == "__main__":
    main()
