# We use pyautogui module and the version is 0.9.53
import pyautogui

for i in range(10):
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")