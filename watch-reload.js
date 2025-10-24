#!/usr/bin/env node

/**
 * Script de surveillance pour recharger automatiquement tour.html
 * lorsque tour.xml est modifié
 *
 * Usage: node watch-reload.js
 */

const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const TOUR_XML = path.join(__dirname, 'tour.xml');
const TOUR_HTML = path.join(__dirname, 'tour.html');

console.log('🔍 Surveillance active de tour.xml...');
console.log(`📁 Fichier surveillé: ${TOUR_XML}`);
console.log(`🌐 Fichier à recharger: ${TOUR_HTML}`);
console.log('');

let lastModified = null;

// Fonction pour recharger tour.html dans le navigateur
function reloadBrowser() {
    const timestamp = new Date().toLocaleTimeString('fr-FR');
    console.log(`🔄 [${timestamp}] tour.xml modifié - Rechargement en cours...`);

    // Pour macOS avec Chrome/Safari
    const applescriptChrome = `
        tell application "Google Chrome"
            set windowList to every window
            repeat with aWindow in windowList
                set tabList to every tab of aWindow
                repeat with atab in tabList
                    if (URL of atab contains "tour.html") then
                        tell atab to reload
                        log "Rechargé dans Chrome"
                    end if
                end repeat
            end repeat
        end tell
    `;

    const applescriptSafari = `
        tell application "Safari"
            set windowList to every window
            repeat with aWindow in windowList
                set tabList to every tab of aWindow
                repeat with atab in tabList
                    if (URL of atab contains "tour.html") then
                        tell atab to do JavaScript "location.reload()"
                        log "Rechargé dans Safari"
                    end if
                end repeat
            end repeat
        end tell
    `;

    // Essayer Chrome d'abord
    exec(`osascript -e '${applescriptChrome}'`, (error) => {
        if (error) {
            // Si Chrome échoue, essayer Safari
            exec(`osascript -e '${applescriptSafari}'`, (error) => {
                if (error) {
                    console.log('⚠️  Impossible de recharger automatiquement le navigateur');
                    console.log('   Rechargez manuellement tour.html dans votre navigateur');
                } else {
                    console.log('✅ Rechargement effectué dans Safari');
                }
            });
        } else {
            console.log('✅ Rechargement effectué dans Chrome');
        }
    });
}

// Surveiller les modifications de tour.xml
fs.watch(TOUR_XML, (eventType, filename) => {
    if (eventType === 'change') {
        const stats = fs.statSync(TOUR_XML);
        const currentModified = stats.mtimeMs;

        // Éviter les doubles événements
        if (lastModified !== currentModified) {
            lastModified = currentModified;
            reloadBrowser();
        }
    }
});

console.log('✅ Surveillance démarrée avec succès!');
console.log('💡 Modifiez tour.xml et tour.html sera rechargé automatiquement');
console.log('⏹️  Appuyez sur Ctrl+C pour arrêter la surveillance');
console.log('');
