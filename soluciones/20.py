import pandas as pd

df = pd.read_csv("data/personas.csv")


df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors='coerce', dayfirst=True)

cantidad = df[
    (df["fecha_nacimiento"].dt.year >= 1990) &
    (df["fecha_nacimiento"].dt.year <= 2000)
].shape[0]

print(f"Personas nacidas entre 1990 y 2000: {cantidad}")