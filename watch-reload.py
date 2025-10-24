#!/usr/bin/env python3
"""
Script de surveillance pour recharger automatiquement tour.html
lorsque tour.xml est modifié

Usage: python3 watch-reload.py

Nécessite: pip install watchdog
"""

import time
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("❌ Module 'watchdog' non trouvé")
    print("📦 Installation: pip install watchdog")
    sys.exit(1)


class TourXMLHandler(FileSystemEventHandler):
    """Gestionnaire d'événements pour tour.xml"""

    def __init__(self):
        self.last_modified = None

    def on_modified(self, event):
        if event.src_path.endswith('tour.xml'):
            # Éviter les doubles événements
            current_time = time.time()
            if self.last_modified and (current_time - self.last_modified) < 1:
                return

            self.last_modified = current_time
            self.reload_browser()

    def reload_browser(self):
        """Recharge tour.html dans le navigateur"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"🔄 [{timestamp}] tour.xml modifié - Rechargement en cours...")

        # Pour macOS
        if sys.platform == 'darwin':
            self.reload_macos()
        # Pour Windows
        elif sys.platform == 'win32':
            self.reload_windows()
        # Pour Linux
        else:
            self.reload_linux()

    def reload_macos(self):
        """Recharge le navigateur sur macOS"""
        # Essayer Chrome
        chrome_script = '''
        tell application "Google Chrome"
            set windowList to every window
            repeat with aWindow in windowList
                set tabList to every tab of aWindow
                repeat with atab in tabList
                    if (URL of atab contains "tour.html") then
                        tell atab to reload
                        return "success"
                    end if
                end repeat
            end repeat
        end tell
        '''

        try:
            subprocess.run(['osascript', '-e', chrome_script],
                          capture_output=True, timeout=2)
            print("✅ Rechargement effectué dans Chrome")
        except Exception:
            # Essayer Safari
            safari_script = '''
            tell application "Safari"
                set windowList to every window
                repeat with aWindow in windowList
                    set tabList to every tab of aWindow
                    repeat with atab in tabList
                        if (URL of atab contains "tour.html") then
                            tell atab to do JavaScript "location.reload()"
                            return "success"
                        end if
                    end repeat
                end repeat
            end tell
            '''
            try:
                subprocess.run(['osascript', '-e', safari_script],
                              capture_output=True, timeout=2)
                print("✅ Rechargement effectué dans Safari")
            except Exception:
                print("⚠️  Rechargez manuellement tour.html dans votre navigateur")

    def reload_windows(self):
        """Recharge le navigateur sur Windows"""
        print("⚠️  Rechargement automatique non disponible sur Windows")
        print("   Rechargez manuellement tour.html dans votre navigateur")

    def reload_linux(self):
        """Recharge le navigateur sur Linux"""
        print("⚠️  Rechargement automatique non disponible sur Linux")
        print("   Rechargez manuellement tour.html dans votre navigateur")


def main():
    """Fonction principale"""
    # Chemin du répertoire à surveiller
    watch_path = Path(__file__).parent
    tour_xml = watch_path / 'tour.xml'

    print("🔍 Surveillance active de tour.xml...")
    print(f"📁 Fichier surveillé: {tour_xml}")
    print(f"🌐 Fichier à recharger: tour.html")
    print("")
    print("✅ Surveillance démarrée avec succès!")
    print("💡 Modifiez tour.xml et tour.html sera rechargé automatiquement")
    print("⏹️  Appuyez sur Ctrl+C pour arrêter la surveillance")
    print("")

    # Créer l'observateur
    event_handler = TourXMLHandler()
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n")
        print("⏹️  Arrêt de la surveillance...")
        observer.stop()

    observer.join()
    print("✅ Surveillance arrêtée")


if __name__ == "__main__":
    main()
