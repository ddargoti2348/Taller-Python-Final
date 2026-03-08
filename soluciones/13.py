import pandas as pd

df = pd.read_csv("data/personas.csv")

# Detectar registros donde el salario tiene caracteres no numéricos
# Se considera no numérico si al eliminar dígitos queda algo
cantidad = df["salario"].apply(lambda x: bool(str(x).strip().translate(str.maketrans('', '', '0123456789')))).sum()

print(f"Existen {cantidad} registros con caracteres no numéricos en el campo salario.")