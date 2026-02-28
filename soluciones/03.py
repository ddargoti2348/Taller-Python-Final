
## cargar datos
import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')
############--------------carga de datos------------------##########################
###-------------------FIN---------------------##

texto_original = "Juan"

# Cifrar (ROT13)
texto_cifrado = codecs.encode(texto_original,'rot13')
print(f"Cifrado: {texto_cifrado}") 

## Juan = Whna

condicion = datos['nombre_cifrado']=='Whna'
datos_nuevos = datos[condicion]
print("El numero de repeticiones de Juan es:",datos_nuevos.shape[0])

