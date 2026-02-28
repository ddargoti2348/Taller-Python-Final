import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')
def decifrar_nombre(nombre_cifrado):
    return codecs.encode(nombre_cifrado, 'rot13')

datos['nombre'] = datos ['nombre_cifrado'].apply(decifrar_nombre)

Frecuencias = datos['nombre'].value_counts()

