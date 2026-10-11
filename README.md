# QR Project

A simple Python command-line tool that turns links into QR codes and reads links back out of QR images.

## Features
- **Link to QR code:** type any link and get a QR image saved as `my_qr.png`
- **QR code to link:** give it a QR image and it prints the link inside
- Simple menu that keeps running until you choose Exit
- Handles a missing or unreadable image without crashing

## Requirements
- Python 3.10 or newer

## Installation
```bash
git clone https://github.com/sriramchandra-67/qr-project.git
cd qr-project
pip install "qrcode[pil]" opencv-python
```

## Usage
```bash
python qr_project.py
```

Then pick an option from the menu:

```
1. Link to QR code
2. QR code to link
3. Exit
```

## How it works
- `qrcode` draws the QR image from your text
- `OpenCV` loads an image and detects and decodes the QR code inside it

## Future ideas
- Custom file names for saved QR codes
- Barcode support
- Morse code and cipher tools

## Author
Built by sriramchandra-67 as a first-year project while learning Python and Git.