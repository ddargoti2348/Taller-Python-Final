import pandas as pd

df = pd.read_csv("data/personas.csv")

# Normalizar campo activo a booleano
# Valores verdaderos: True, true, 1, SI, yes, si
# Valores falsos: False, false, 0, NO, no
df["activo"] = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
)

falsos = df["activo"].isin(['false', '0', 'no']).sum()

print(f"Existen {falsos} registros con 'activo' como falso.")