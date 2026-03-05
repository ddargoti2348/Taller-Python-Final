import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')
def decifrar_apellido(apellido_cifrado):
    return codecs.encode(apellido_cifrado, 'rot13')

datos['apellido'] = datos ['apellido_cifrado'].apply(decifrar_apellido)

Frecuencias = datos['apellido'].value_counts()

apellido_frecuente = Frecuencias.idxmax()
Numero_de_veces = Frecuencias.max()

print ("El apellido mas frecuente es:", apellido_frecuente)
print ("Aparece:",Numero_de_veces, "veces")