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

verdaderos = df["activo"].isin(['true', '1', 'si', 'yes']).sum()

print(f"Existen {verdaderos} registros con 'activo' como verdadero.")