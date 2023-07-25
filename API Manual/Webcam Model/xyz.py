import pyautogui

def get_coordinates():
    print("Move your mouse to the top-left corner of the region and press Enter.")
    input("Press Enter to continue...")  # Wait for Enter key press
    left, top = pyautogui.position()
    print(f"Top-left corner coordinates: ({left}, {top})")

    print("Move your mouse to the bottom-right corner of the region and press Enter.")
    input("Press Enter to continue...")  # Wait for Enter key press
    right, bottom = pyautogui.position()
    print(f"Bottom-right corner coordinates: ({right}, {bottom})")

    return left, top, right, bottom

# Call this function to get the coordinates for the region
left, top, right, bottom = get_coordinates()

# Now you can use these coordinates in the 'tesseract()' function to crop the region
