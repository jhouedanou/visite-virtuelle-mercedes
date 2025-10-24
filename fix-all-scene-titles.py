#!/usr/bin/env python3
"""
Script pour ajouter set_page_title() à toutes les scènes
si l'événement global ne suffit pas
"""

import re

# Lire le fichier tour.xml
with open('tour.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern pour trouver les scènes avec onstart=""
pattern = r'(<scene[^>]*onstart=")("")'

# Remplacer par onstart="set_page_title();"
replacement = r'\1set_page_title();\2'

# Compter les occurrences
matches = re.findall(pattern, content)
print(f"Trouvé {len(matches)} scènes avec onstart vide")

# Effectuer le remplacement
new_content = re.sub(pattern, replacement, content)

# Sauvegarder
with open('tour.xml', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ Modification effectuée sur {len(matches)} scènes")
print("Toutes les scènes appelleront maintenant set_page_title() au démarrage")
