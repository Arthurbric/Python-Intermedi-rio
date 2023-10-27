import pyautogui
from time import sleep
for i in range(26,51):
    sleep(1.5)
    pyautogui.moveTo(508, 54, 2)
    pyautogui.click(508, 54, clicks=1, interval=2, button='left')
    for i in range(1,20):
        pyautogui.write(f"https://dontpad.com/CEUB{i}")
        sleep(0.5)
        pyautogui.press("enter")

    sleep(1.5)
    pyautogui.moveTo(8, 123, 2)
    pyautogui.click(8, 123, clicks=1, interval=1, button='left')
    for i in range(10):
        pyautogui.press("enter")
    pyautogui.click(8, 123, clicks=1, interval=1, button='left')
    pyautogui.write("https://classroom.google.com/c/NjMzMDgxNTgzOTM1?cjc=ezz5zjd")
    sleep(4)



"""
# my_var = r"'ctrl','a'"
# sleep(0.5)
# pyautogui.hotkey(my_var)
# sleep(0.5)
"""