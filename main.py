# Main del proyecto 
import os, sys

"""Agregamos al path la dirrecion del "current_dir" => Así reconoce toods los modulos del proyecto"""
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

#Resto de importaciones

from Utils import utils
import pandas as pd 

def run():
    config = utils.Procesar_configuracion("config.yml")

    a = config["a"]
    b = config["b"]

    c = utils.suma(a,b)

    print(f"La suma de {a} y {b} es: {c}")

    dict_df = {"A" : [1,2],  "B": ["Arroz", "Huevo"]}
    df = pd.DataFrame(dict_df)
    print(df)
if __name__ == "__main__":
    run()