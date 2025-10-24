# Scripts de Rechargement Automatique

Ces scripts surveillent le fichier `tour.xml` et rechargent automatiquement `tour.html` dans votre navigateur à chaque modification.

## 🚀 Utilisation Rapide

### Option 1: Script Python (Recommandé - Fonctionne sur tous les systèmes)

```bash
# Installer la dépendance (une seule fois)
pip install watchdog

# Lancer la surveillance
python3 watch-reload.py
```

### Option 2: Script Shell (macOS/Linux uniquement)

```bash
# Installer fswatch (une seule fois sur macOS)
brew install fswatch

# Lancer la surveillance
./watch-reload.sh
```

### Option 3: Script Node.js (Si vous avez Node.js installé)

```bash
# Lancer la surveillance
node watch-reload.js
```

## 📋 Instructions Détaillées

### 1. Ouvrir `tour.html` dans votre navigateur

- Ouvrez Chrome ou Safari
- Chargez le fichier `tour.html`
- Gardez l'onglet ouvert

### 2. Lancer le script de surveillance

Choisissez une des options ci-dessus selon votre préférence et votre système.

### 3. Modifier `tour.xml`

- Éditez le fichier `tour.xml` dans votre éditeur
- Sauvegardez les modifications
- Le script détectera automatiquement le changement
- `tour.html` sera rechargé dans le navigateur

### 4. Arrêter la surveillance

Appuyez sur `Ctrl+C` dans le terminal pour arrêter le script.

## 🔧 Modifications Effectuées dans tour.xml

Les commandes de navigation ont été activées avec les paramètres suivants :

- **Thumbnails (Miniatures)** : `thumbs="true"` - Affichage des vignettes des scènes
- **Thumbnails ouvertes** : `thumbs_opened="true"` - Panneau de miniatures ouvert par défaut
- **Texte des miniatures** : `thumbs_text="true"` - Affichage des titres sous les miniatures
- **Boutons de défilement** : `thumbs_scrollbuttons="true"` - Boutons pour naviguer dans les miniatures
- **Indicateur de défilement** : `thumbs_scrollindicator="true"` - Barre de progression
- **Défilement au survol** : `thumbs_onhoverscrolling="true"` - Défilement automatique au survol
- **Tooltips des boutons** : `tooltips_buttons="true"` - Info-bulles sur les boutons
- **Tooltips des miniatures** : `tooltips_thumbs="true"` - Info-bulles sur les miniatures
- **Tooltips des hotspots** : `tooltips_hotspots="true"` - Info-bulles sur les points d'intérêt
- **Tooltips des points de carte** : `tooltips_mapspots="true"` - Info-bulles sur la carte

## 🎨 Interface de Navigation Visible

Après rechargement de `tour.html`, vous verrez :

1. **Barre de contrôle complète** en bas de l'écran avec :
   - Bouton de lecture automatique
   - Contrôles de zoom
   - Bouton plein écran
   - Bouton VR/gyroscope
   - Navigation précédent/suivant

2. **Panneau de miniatures** :
   - Vignettes de toutes les scènes
   - Titres des scènes
   - Navigation rapide entre les scènes
   - Boutons de défilement

3. **Info-bulles** :
   - Sur tous les boutons
   - Sur tous les hotspots
   - Sur toutes les miniatures

## ⚠️ Dépannage

### Le script Python ne démarre pas
```bash
# Vérifier que Python 3 est installé
python3 --version

# Installer watchdog
pip install watchdog
```

### Le navigateur ne se recharge pas automatiquement
- Vérifiez que `tour.html` est ouvert dans Chrome ou Safari
- Sur Windows/Linux : rechargez manuellement le navigateur (F5 ou Cmd+R)
- Le script affiche un message à chaque détection de modification

### fswatch non trouvé (macOS)
```bash
# Installer Homebrew si nécessaire
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer fswatch
brew install fswatch
```

## 💡 Astuces

- Gardez le terminal visible pour voir les messages de rechargement
- Vous pouvez modifier plusieurs fois `tour.xml`, chaque sauvegarde déclenchera un rechargement
- Si vous travaillez sur plusieurs onglets, tous les onglets contenant `tour.html` seront rechargés

## 📝 Notes

- Les scripts ne modifient pas les fichiers, ils surveillent seulement `tour.xml`
- Le rechargement automatique fonctionne mieux sur macOS avec Chrome ou Safari
- Sur Windows/Linux, un rechargement manuel peut être nécessaire (le script vous le signalera)
