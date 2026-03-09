import pandas as pd

df = pd.read_csv("data/personas.csv")

# Convertir fechas a datetime manejando múltiples formatos
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors='coerce', dayfirst=True)

# Contar personas nacidas entre 1990 y 2000 inclusive
cantidad = df[
    (df["fecha_nacimiento"].dt.year >= 1990) &
    (df["fecha_nacimiento"].dt.year <= 2000)
].shape[0]

print(f"Personas nacidas entre 1990 y 2000: {cantidad}")