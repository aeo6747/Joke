import pyautogui

pyautogui.alert("hi")

i = 1000

while True:
    pyautogui.alert(i)
    i -= 1
