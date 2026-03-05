import pandas as pd

df = pd.read_csv("data/personas.csv")

# normalizar ciudad
df["ciudad"] = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("á","a")
    .str.replace(r"[^a-z]", "", regex=True)
)

# contar ciudades únicas
cantidad_ciudades = df["ciudad"].nunique()

print("Número de ciudades únicas después de normalizar:", cantidad_ciudades)