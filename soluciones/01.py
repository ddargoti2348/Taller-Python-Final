import pandas as pd

datos = pd.read_csv('data/personas.csv')

datos["id"] = datos["id"].astype(str)

# 3. Detectar ids con caracteres no numéricos
ids_no_numericos = ~datos["id"].str.isnumeric()

# 4. Contar filas
cantidad = ids_no_numericos.sum()

print("Filas con id no numérico:", cantidad)





