import pandas as pd
import numpy as np
import pyautogui, webbrowser
from time import sleep
import pyperclip as clipboard

df = pd.read_excel("./telefonos.xlsx")
numbers = np.array((df["Telefono"]))

message = open("./message.txt", encoding="UTF-8")
imagen = open("./img.jpg")
message = message.read()

for num in numbers:
    webbrowser.open(f"https://web.whatsapp.com/send?phone={num}")

    sleep(8)

    pyautogui.hotkey("ctrl", "v")
    pyautogui.write(
        """¡Hola :) !  ¡Disfruta de la nueva colección en *Elements Joyería!*

Realiza fácilmente tu pedido en : elements-of-steel.com.mx/catalog/ * 
O con tu vendedor de confianza :)

*Recuerda *ingresar tu número celular como usuario y contraseña*

Si prefieres catálogo en PDF avísame ;D"""
    )
    # clipboard.copy(imagen)

    # sleep(1)
    # pyautogui.press("enter")
