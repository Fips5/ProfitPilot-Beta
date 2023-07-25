import json
from PIL import Image
import pytesseract
import cv2
import pyautogui
import time

def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    custom_config = r'--psm 6 outputbase digits'

    while True:
        # Add a 2-second delay before capturing the screenshot
        time.sleep(2)

        # Capture a screenshot of the entire screen
        screenshot = pyautogui.screenshot()

        # Define the region to crop (left, top, right, bottom)
        # Adjust these coordinates to fit the region you want to capture
        left, top, right, bottom = 459, 141, 558, 172

        # Crop the screenshot to the defined region
        cropped_screenshot = screenshot.crop((left, top, right, bottom))

        # Save the cropped screenshot as 'cropped_screenshot.png'
        cropped_screenshot.save('cropped_screenshot.png')

        # Perform OCR on the cropped screenshot
        text = pytesseract.image_to_string(cropped_screenshot, config=custom_config)
        #text = text.replace('.', ',')
        price = float(text[:-1]) if text else None

        if price is not None:
            # Create a dictionary to store the output data
            output_data = {"price": price}

            with open('output.json', 'w') as json_file:
                json.dump(output_data, json_file)

if __name__ == "__main__":
    tesseract()


