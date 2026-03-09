import pandas as pd

df = pd.read_csv("data/personas.csv")

# Limpiar salario: eliminar caracteres no numéricos excepto punto decimal
# Se eliminan símbolos como @, $, %, paréntesis, corchetes, texto como 'aprox.'
# Se reemplaza coma decimal por punto para unificar formato
df["salario"] = (
    df["salario"]
    .astype(str)
    .str.replace(',', '.', regex=False)       # coma decimal → punto
    .str.replace(r'[^0-9.]', '', regex=True)  # eliminar todo excepto dígitos y punto
)

df["salario"] = pd.to_numeric(df["salario"], errors='coerce')

promedio = df["salario"].mean()
print(f"El salario promedio después de limpiar es: {promedio:,.2f}")