
## cargar datos
import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')
############--------------carga de datos------------------##########################
###-------------------FIN---------------------##

texto_original = "Maria"

# Cifrar (ROT13)
texto_cifrado = codecs.encode(texto_original,'rot13')
print(f"Cifrado: {texto_cifrado}") 

## MARIA = Znevn


condicion = datos['nombre_cifrado']=='Znevn'
datos_nuevos = datos[condicion]
print("El numero de repeticiones de Maria es:", datos_nuevos.shape[0])

