import pandas as pd

df = pd.read_csv("data/personas.csv")

df["activo"] = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
)

falsos = df["activo"].isin(['false', '0', 'no']).sum()

print(f"Existen {falsos} registros con 'activo' como falso.")