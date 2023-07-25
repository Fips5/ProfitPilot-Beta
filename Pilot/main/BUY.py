import pyautogui
import time

def buy():
    pyautogui.hotkey('ctrl', '1')

    pyautogui.hotkey('ctrl', 'r')

    pyautogui.sleep(12.62)
    pyautogui.moveTo(1249, 223, duration=1)
    pyautogui.click()

    pyautogui.moveTo(777, 246, duration=1)
    pyautogui.click()

    pyautogui.moveTo(777, 246, duration=1)
    pyautogui.click()

    pyautogui.moveTo(679, 692, duration=1)
    pyautogui.click()

    pyautogui.hotkey('ctrl', '1')