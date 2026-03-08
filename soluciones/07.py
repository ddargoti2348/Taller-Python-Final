import pandas as pd

df = pd.read_csv("data/personas.csv")

df["ciudad"] = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("á","a")
    .str.replace(r"[@*!%#_]", "", regex=True)
)

cantidad = (df["ciudad"] == "medellin").sum()

print(f"Existen {cantidad} registros correspondientes a la ciudad de Medellin.")