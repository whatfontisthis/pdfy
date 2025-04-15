# PNG to PDF Merger

A simple Python utility to merge PNG images into a single PDF file while maintaining aspect ratio.

## Features

- Automatically finds all PNG images in the current directory
- Resizes images to a consistent height (1080px) while maintaining aspect ratio
- Preserves image quality using the LANCZOS resampling algorithm
- Sorts images alphabetically before combining
- Includes a progress bar for better visibility during processing

## Requirements

- Python 3.x
- PIL (Pillow)
- tqdm

## Installation

```bash
pip install pillow tqdm
```

## Usage

1. Place the script in the same directory as your PNG files
2. Run the script:

```bash
python png_to_pdf.py
```

By default, this will create a file named `merged_pdf.pdf` in the same directory.

## Customization

You can modify the output filename and target height by changing the parameters:

```python
# Change the output filename
merge_all_pngs_to_pdf("your_custom_name.pdf")

# To modify the target height, change this line in the function:
target_height = 1080  # Change to your desired height
```

## Example

```
$ python png_to_pdf.py
이미지 처리 중...
Resizing images: 100%|██████████| 15/15 [00:01<00:00, 12.34img/s]
merged_pdf.pdf로 저장 완료! (세로 1080px, 비율 유지)
```

## License

MIT

## Author

Your Name
