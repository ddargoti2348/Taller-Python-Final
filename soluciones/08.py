import pandas as pd
import unicodedata

df = pd.read_csv("data/personas.csv")

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

df["ciudad"] = (
    df["ciudad"]
    .apply(quitar_tildes)
    .str.replace(r'\t', '', regex=True)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

ciudades_unicas = df["ciudad"].nunique()

print(f"Existen {ciudades_unicas} ciudades únicas en el dataset.")