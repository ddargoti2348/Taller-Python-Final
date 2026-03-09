import pandas as pd

df = pd.read_csv("data/personas.csv")


df["fecha_nacimiento"] = pd.to_datetime(
    df["fecha_nacimiento"],
    errors="coerce"
)

#
cantidad = df["fecha_nacimiento"].isna().sum()

print(f"Existen {cantidad} registros con formato incorrecto en fecha_nacimiento.")