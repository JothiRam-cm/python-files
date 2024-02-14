import pytesseract
from PIL import Image

# Path to your Tesseract executable (change this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract>'

# Load an image using PIL (Pillow)
image_path ="C:\Users\cmjot\OneDrive\Desktop\programmer tools\pythonfiles\img3.jpg"
img = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print("Extracted Text:")
print(text)