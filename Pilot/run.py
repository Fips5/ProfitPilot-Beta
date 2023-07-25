import datetime
import time
import pyautogui

def run():
    typing_interval = 0.2


    #here do be chrome navigation section
    time.sleep(4)
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.typewrite(r'C:\Users\David\Desktop\Pilot\DAVID - Chrome - Copy.lnk', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite('https://www.etoro.com/markets/tsla', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('https://www.etoro.com/portfolio/overview', interval=typing_interval)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.press('f11')
    time.sleep(10)

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(5)


    pyautogui.typewrite(r'cd C:\Users\David\Desktop\API Manual\Webcam Model', interval=typing_interval )    #
    pyautogui.press('enter')
    pyautogui.typewrite('python main.py', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('win', 'down')

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(5)
    
    pyautogui.typewrite(r'cd C:\Users\David\Desktop\Pilot\5\sma', interval=typing_interval)    #
    pyautogui.press('enter')
    pyautogui.typewrite('python SMA5.py', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('win', 'down')

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.typewrite(r'cd C:\Users\David\Desktop\Pilot\20\sma', interval=typing_interval)   #
    pyautogui.press('enter')
    pyautogui.typewrite('python SMA20.py', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('win', 'down')

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.typewrite(r'cd C:\Users\David\Desktop\Pilot\5', interval=typing_interval)    #
    pyautogui.press('enter')
    pyautogui.typewrite('python results.py', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('win', 'down')

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=typing_interval)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.typewrite(r'cd C:\Users\David\Desktop\Pilot\20', interval=typing_interval)    #
    pyautogui.press('enter')
    pyautogui.typewrite('python results.py', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('win', 'down')

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=typing_interval)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.typewrite(r'cd C:\Users\David\Desktop\API Manual\Webcam Model', interval=typing_interval )    #
    pyautogui.press('enter')
    pyautogui.typewrite('python main.py', interval=typing_interval)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('win', 'down')

    #here do be the MAIN section
    pyautogui.typewrite(r'cd C:\Users\David\Desktop\Pilot\main', interval=typing_interval)    #
    pyautogui.press('enter')
    pyautogui.typewrite('python SMA.py', interval=typing_interval)
    pyautogui.press('enter')
    pyautogui.hotkey('win', 'shift', 'down')
    pyautogui.hotkey('win', 'shift', 'down')
    #pyautogui.hotkey('f11')

run()

