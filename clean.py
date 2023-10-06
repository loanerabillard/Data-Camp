'''import pandas as pd
import re

# Lire le fichier CSV d'entrée
input_file = "songs.csv"
df = pd.read_csv(input_file)

# Utiliser une expression régulière insensible à la casse pour trouver "[verse 1]" dans la colonne "Lyrics"
pattern = re.compile(r'\[verse 1\]', flags=re.IGNORECASE)

# Filtrer les lignes où la colonne "Lyrics" contient "[verse 1]"
filtered_df = df[df["Lyrics"].str.contains(pattern, na=False)]

# Nom du fichier CSV de sortie
output_file = "resultat.csv"

# Écrire les lignes filtrées dans un nouveau fichier CSV
filtered_df.to_csv(output_file, index=False)

print(f"Les lignes contenant '[verse 1]' (insensible à la casse) ont été extraites dans {output_file}")'''
'''
import pandas as pd

# Lire le fichier CSV d'entrée
input_file = "songs.csv"
df = pd.read_csv(input_file)

# Supprimer les sauts de ligne de la colonne "Lyrics"
df["Lyrics"] = df["Lyrics"].replace('\n', ' ', regex=True)

# Nom du fichier CSV de sortie
output_file = "resultatss.csv"

# Écrire le DataFrame modifié dans un nouveau fichier CSV
df.to_csv(output_file, index=False)

print(f"Les sauts de ligne ont été supprimés et le fichier résultant a été enregistré sous {output_file}")
'''
import pandas as pd

# Lire le fichier CSV d'entrée
input_file = "resultatss.csv"
df = pd.read_csv(input_file)

# Filtrer les lignes où la colonne "Lyrics" ne contient pas "Lyrics not found"
filtered_df = df[df["Lyrics"] != "Lyrics not found"]

# Nom du fichier CSV de sortie
output_file = "resultat.csv"

# Écrire les lignes filtrées dans un nouveau fichier CSV
filtered_df.to_csv(output_file, index=False)

print(f"Les lignes contenant 'Lyrics not found' ont été supprimées, le fichier résultant a été enregistré sous {output_file}")
