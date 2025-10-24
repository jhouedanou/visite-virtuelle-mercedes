#!/bin/bash

# Script de surveillance simple pour recharger tour.html
# lorsque tour.xml est modifié

echo "🔍 Surveillance active de tour.xml..."
echo "📁 Fichier surveillé: tour.xml"
echo "💡 Le navigateur rechargera automatiquement tour.html"
echo "⏹️  Appuyez sur Ctrl+C pour arrêter"
echo ""

# Utiliser fswatch si disponible (installation: brew install fswatch)
if command -v fswatch &> /dev/null; then
    fswatch -o tour.xml | while read change; do
        timestamp=$(date '+%H:%M:%S')
        echo "🔄 [$timestamp] tour.xml modifié - Signal de rechargement envoyé"

        # Essayer de recharger Chrome
        osascript -e 'tell application "Google Chrome" to reload active tab of window 1' 2>/dev/null

        # Si Chrome ne marche pas, essayer Safari
        if [ $? -ne 0 ]; then
            osascript -e 'tell application "Safari" to do JavaScript "location.reload()" in current tab of window 1' 2>/dev/null
        fi
    done
else
    echo "⚠️  fswatch n'est pas installé"
    echo "📦 Installation recommandée: brew install fswatch"
    echo ""
    echo "Alternative: utiliser 'node watch-reload.js' à la place"
fi
