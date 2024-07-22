import json
import os
from os import path

def cargar_tema(ruta_relativa="themes/lofi.json"):
    qtile_path = path.join(path.expanduser('~'), ".config", "qtile")
    archivo_json = os.path.join(qtile_path, ruta_relativa)
    
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as file:
            datos_json = json.load(file)
        return datos_json
    else:
        print(f"El archivo JSON {ruta_relativa} no existe en {qtile_path}.")
        return None
