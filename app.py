from flask import Flask, request, jsonify
import pytesseract
import cv2
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Read the image file and convert it to a format that OpenCV can process
    image_bytes = image_file.read()
    image = np.fromstring(image_bytes, np.uint8)
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    # Return the extracted text as JSON
    return jsonify({"extracted_text": text})

if __name__ == '__main__':
    app.run(debug=True, port=8784)
