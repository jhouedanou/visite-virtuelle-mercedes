# 🚀 Instructions pour le Serveur de Développement

## Étape 1 : Lancer le serveur HTTP

Le serveur Python est **DÉJÀ EN COURS D'EXÉCUTION** sur le port 8000.

### Accéder à la visite virtuelle

Ouvrez votre navigateur et allez sur :

**http://localhost:8000/tour.html**

---

## Étape 2 : Surveiller les modifications (OPTIONNEL)

### Option A : Surveillance Simple avec Notifications (Recommandé)

Dans un **NOUVEAU terminal**, exécutez :

```bash
cd /Users/bfa/Documents/GitHub/visite-virtuelle-mercedes
./watch-simple.sh
```

Ce script :
- ✅ Détecte les modifications de tour.xml
- ✅ Affiche un message dans le terminal
- ✅ Envoie une notification macOS
- ⚠️ Vous devez recharger manuellement le navigateur (Cmd+R)

### Option B : Sans Surveillance

Vous pouvez simplement :
1. Modifier `tour.xml`
2. Sauvegarder
3. Recharger manuellement `tour.html` dans le navigateur (Cmd+R ou F5)

---

## Arrêter le Serveur

Pour arrêter le serveur HTTP Python :

```bash
# Trouver le processus
ps aux | grep "python3 -m http.server"

# Tuer le processus (remplacer <PID> par le numéro)
kill <PID>
```

Ou plus simplement :

```bash
pkill -f "python3 -m http.server 8000"
```

---

## 📋 Modifications Récentes

### ✅ Scène 13 - GLC 200
- Hotspot d'entrée dans la voiture (icône transformée)
- Hotspot info avec popup GLC 200 (en haut à gauche)

### ✅ Scène 16 - GLC 200
- Hotspot info avec popup GLC 200 (au centre en haut)

---

## 🔧 Dépannage

### Le serveur ne démarre pas (port déjà utilisé)
```bash
# Vérifier si le port 8000 est déjà utilisé
lsof -i :8000

# Utiliser un autre port
python3 -m http.server 8001 --bind localhost
# Puis accéder à : http://localhost:8001/tour.html
```

### La page ne se charge pas
- Vérifiez que le serveur est bien lancé
- Vérifiez l'URL : http://localhost:8000/tour.html
- Essayez de vider le cache du navigateur (Cmd+Shift+R)

### Les modifications ne s'affichent pas
1. Sauvegardez bien tour.xml
2. Rechargez la page avec Cmd+Shift+R (rechargement forcé)
3. Vérifiez la console du navigateur (F12) pour les erreurs

---

## 💡 Raccourcis Utiles

- **Recharger la page** : `Cmd+R` (Mac) ou `F5` (Windows/Linux)
- **Recharger sans cache** : `Cmd+Shift+R` (Mac) ou `Ctrl+Shift+R` (Windows/Linux)
- **Ouvrir la console** : `Cmd+Option+I` (Mac) ou `F12` (Windows/Linux)
- **Arrêter le script de surveillance** : `Ctrl+C` dans le terminal

---

## 📍 Liens Rapides

- **Visite virtuelle** : http://localhost:8000/tour.html
- **Fichier tour.xml** : `/Users/bfa/Documents/GitHub/visite-virtuelle-mercedes/tour.xml`
- **Documentation README** : [WATCH-RELOAD-README.md](WATCH-RELOAD-README.md)
