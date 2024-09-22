# OCR Using Tesseract - Python

**OCR-Using-Tesseract** is a simple API built with Flask, OpenCV, and Tesseract OCR to extract text from images. This project provides an easy-to-use API that processes images and returns the extracted text in JSON format.

## Features
- Extracts text from images using the Tesseract OCR engine.
- Supports multiple image formats like JPEG, PNG, etc.
- Easy to integrate into other applications via HTTP requests.

## Installation

### Prerequisites
1. **Tesseract OCR**: Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract). Ensure it's added to your system's PATH.
2. **Python 3.x**: Make sure Python is installed on your machine.

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/VRAJ-07/ocr-using-tesseract.git
   cd ocr-using-tesseract
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the Tesseract path in `app.py` to match your local installation:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

The API will be hosted at `http://localhost:8784/ocr`.

## API Usage

Send a `POST` request with an image file to `/ocr`. The API will return the extracted text from the image.

### Example Request

```bash
curl -X POST -F "image=@path_to_image.jpg" http://localhost:8784/ocr
```

### Example Response

```json
{
  "extracted_text": "The text extracted from the image"
}
```

## Dependencies

- **Flask**: Web framework for building the API.
- **pytesseract**: Python wrapper for the Tesseract OCR engine.
- **OpenCV**: Image processing library.
- **numpy**: Library for handling image data arrays.
