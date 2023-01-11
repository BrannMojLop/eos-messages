import pandas as pd
import numpy as np
import pyautogui
import webbrowser
from time import sleep
import pyperclip as clipboard

df = pd.read_excel("./telefonos.xlsx")
numbers = np.array((df["Telefono"]))

message = open('./message.txt', encoding='utf-8')
message = message.read()

for num in numbers:
    webbrowser.open(f"https://web.whatsapp.com/send?phone={num}")
    clipboard.copy(message)

    sleep(8)
    pyautogui.hotkey("ctrl", "v")
    sleep(1)
    pyautogui.hotkey("ctrl", "shift", "b")
    sleep(1)
    pyautogui.hotkey("ctrl", "v")
    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')

    print(num)
