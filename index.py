import pandas as pd
import numpy as np
import pyautogui, webbrowser
from time import sleep

df = pd.read_excel("./telefonos.xlsx")
numbers = np.array(df["Telefono"])
messages = np.array(df["Mensaje"])

for num in numbers:
    webbrowser.open(f"https://web.whatsapp.com/send?phone={num}")

    sleep(8)

    pyautogui.typewrite(messages[0])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    sleep(2)
