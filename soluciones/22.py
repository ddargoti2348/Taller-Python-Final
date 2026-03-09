import pandas as pd
from datetime import date

df = pd.read_csv("data/personas.csv")

# Convertir fechas a datetime manejando múltiples formatos
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors='coerce', dayfirst=True)

# Fecha de referencia indicada en el ejercicio
fecha_actual = pd.Timestamp("2026-02-26")

# Calcular edad y contar mayores de 50 años
df["edad"] = (fecha_actual - df["fecha_nacimiento"]).dt.days // 365

cantidad = df[df["edad"] > 50].shape[0]

print(f"Personas con más de 50 años a fecha 2026-02-26: {cantidad}")