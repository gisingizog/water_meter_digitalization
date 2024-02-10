#The water meter readings are not detected because of the image quality but I added text.png as a sample file
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try:
    image = cv2.imread('pics/wm_reading')

    if image is None:
        raise FileNotFoundError("Image file not found.")
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray_image)

    if text.strip() == '':
        raise RuntimeError("No text detected in the image.")
    
    print(text)
except Exception as e:
    print("An error occurred:", e)
