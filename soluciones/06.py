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

cantidad = (df["ciudad"] == "bogota").sum()

print(f"Después de limpiar los datos, existen {cantidad} registros correspondientes a la ciudad de Bogotá.")