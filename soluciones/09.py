import pandas as pd
import unicodedata

df = pd.read_csv('data/personas.csv')

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

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

# Corrección de profesiones con @ en lugar de 'a' y 3 en lugar de 'e'
# Ejemplo: 'Ing3ni3ro' → limpia como 'ingniro' → se corrige a 'ingeniero'
correcciones = {
    'abogdo':       'abogado',
    'administrdor': 'administrador',
    'arquitcto':    'arquitecto',
    'chf':          'chef',
    'contdor':      'contador',
    'crpintro':     'carpintero',
    'disndor':      'disenador',
    'economist':    'economista',
    'elctricist':   'electricista',
    'enfrmro':      'enfermero',
    'ingniro':      'ingeniero',
    'mcnico':       'mecanico',
    'mdico':        'medico',
    'plomro':       'plomero',
    'priodist':     'periodista',
    'profsor':      'profesor',
    'progrmdor':    'programador',
    'trductor':     'traductor',
    'vtrinrio':     'veterinario',
}

df["profesion"] = df["profesion"].replace(correcciones)

cantidad = (df["profesion"] == "ingeniero").sum()
print(f"Existen {cantidad} registros con la profesión 'Ingeniero'.")