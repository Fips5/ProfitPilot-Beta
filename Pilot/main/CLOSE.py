import pyautogui
import time

def close():
    pyautogui.hotkey('ctrl', '2')

    pyautogui.hotkey('ctrl', 'r')

    pyautogui.sleep(12.62)
    pyautogui.moveTo(423, 329, duration=0)
    pyautogui.click()

    pyautogui.sleep(0.5)
    pyautogui.moveTo(1262, 340, duration=0)
    pyautogui.click()

    pyautogui.sleep(0.5)
    pyautogui.moveTo(681, 534, duration=0)
    pyautogui.click()

    pyautogui.hotkey('ctrl', '1')
