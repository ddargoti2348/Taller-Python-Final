import pandas as pd

df = pd.read_csv("data/personas.csv")

# Convertir fechas a datetime manejando múltiples formatos
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors='coerce', dayfirst=True)

# Contar personas nacidas antes de 1960
cantidad = df[df["fecha_nacimiento"].dt.year < 1960].shape[0]

print(f"Personas nacidas antes de 1960: {cantidad}")