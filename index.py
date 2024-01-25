import re
import pandas as pd
from unidecode import unidecode
import pyautogui
import webbrowser
from time import sleep


try:
    sleep_open = input(
        "Por favor, ingresa el tiempo de espera para abrir la ventana (Ingresa un número entre 1 y 15):"
    )
    sleep_open = int(sleep_open)

    image = None

    while not image == "SI" and not image == "NO":
        image = input("El mensaje se enviara con imagen? (SI/NO)").strip().upper()

    if image == "SI":
        image_load = input(
            "Por favor, ingresa el tiempo de espera para cargar la imagen (Ingresa un número entre 1 y 15): "
        )
        image_load = int(image_load)

    sleep_send = input(
        "Por favor, ingresa el tiempo de espera despues de enviar el mensaje (Ingresa un número entre 1 y 15): "
    )
    sleep_send = int(sleep_send)

    df = pd.read_excel("./telefonos.xlsx")

    message = open("./message.txt", encoding="utf-8")
    message = message.read()

    for index, row in df.iterrows():
        webbrowser.open(f"https://web.whatsapp.com/send?phone={row['Telefono']}")

        sleep(sleep_open)
        lines = message.split("\n")

        for line in lines:
            line = unidecode(line)
            text = line
            words_key = re.findall(r"\{(.*?)\}", line)

            for word in words_key:
                if word in df.columns:
                    text = text.replace(f"{{{word}}}", str(df[word][index]))

            pyautogui.write(text, interval=0.01)
            pyautogui.hotkey("ctrl", "enter")

        sleep(1)

        if image == "SI":
            pyautogui.hotkey("ctrl", "v")
            sleep(image_load)

        pyautogui.press("enter")
        sleep(sleep_send)
        pyautogui.hotkey("ctrl", "w")
        sleep(5)
        pyautogui.press("enter")

        print(row["Telefono"])

    print("El programa a finalizado con exito.")

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")
