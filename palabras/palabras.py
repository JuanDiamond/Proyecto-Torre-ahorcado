import random

def palabra_radom(tematica, nivel):

    ruta = f"palabras/{tematica}/nivel{nivel}.txt"

    with open(ruta, "r", encoding="utf-8") as archivo:
        palabras = archivo.read().splitlines()

    return random.choice(palabras)