import pyautogui, time
time.sleep(4)
f = open("text.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)