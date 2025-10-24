#!/bin/bash

# Script simple de surveillance pour macOS
# Détecte les changements dans tour.xml et affiche un message

echo "🔍 Surveillance de tour.xml activée"
echo "🌐 Serveur accessible sur : http://localhost:8000/tour.html"
echo "💡 Rechargez manuellement le navigateur après chaque modification (Cmd+R)"
echo "⏹️  Appuyez sur Ctrl+C pour arrêter"
echo ""

LAST_MODIFIED=$(stat -f %m tour.xml 2>/dev/null || stat -c %Y tour.xml)

while true; do
    sleep 1
    CURRENT_MODIFIED=$(stat -f %m tour.xml 2>/dev/null || stat -c %Y tour.xml)

    if [ "$CURRENT_MODIFIED" != "$LAST_MODIFIED" ]; then
        LAST_MODIFIED=$CURRENT_MODIFIED
        timestamp=$(date '+%H:%M:%S')
        echo "🔄 [$timestamp] tour.xml modifié ! Rechargez tour.html dans le navigateur (Cmd+R)"

        # Essayer d'envoyer une notification macOS
        if command -v osascript &> /dev/null; then
            osascript -e 'display notification "Rechargez tour.html dans le navigateur" with title "tour.xml modifié"' 2>/dev/null
        fi
    fi
done
