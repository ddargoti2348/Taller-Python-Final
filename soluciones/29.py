import pandas as pd

df = pd.read_csv("data/personas.csv")

# Limpiar email y contar los que tienen dominio gmail.com
df["email"] = df["email"].astype(str).str.strip().str.lower()

cantidad = df["email"].str.endswith("@gmail.com").sum()

print(f"Registros con email de dominio 'gmail.com': {cantidad}")