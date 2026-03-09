import pandas as pd

df = pd.read_csv("data/personas.csv")


cantidad = (~df["salario"].astype(str).str.isnumeric()).sum()

print("Registros con caracteres no numéricos en salario:", cantidad)