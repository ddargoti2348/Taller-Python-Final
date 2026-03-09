import pandas as pd
import unicodedata

df = pd.read_csv("data/personas.csv")

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

# Limpiar ciudad
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

# Limpiar profesion
df["profesion"] = (
    df["profesion"]
    .apply(quitar_tildes)
    .str.replace(r'\t', '', regex=True)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

# Ciudad con más ingenieros
ciudad_top = (
    df[df["profesion"] == "ingeniero"]
    .groupby("ciudad")
    .size()
    .idxmax()
)

cantidad = df[(df["profesion"] == "ingeniero") & (df["ciudad"] == ciudad_top)].shape[0]

print(f"La ciudad con más ingenieros es '{ciudad_top}")