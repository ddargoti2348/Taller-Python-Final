import pandas as pd

df = pd.read_csv("data/personas.csv")

# Intentar convertir la columna a fecha
df["fecha_nacimiento"] = pd.to_datetime(
    df["fecha_nacimiento"],
    errors="coerce"
)

# Contar registros donde la fecha es inválida
cantidad = df["fecha_nacimiento"].isna().sum()

print(f"Existen {cantidad} registros con formato incorrecto en fecha_nacimiento.")