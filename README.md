# SengProjekt
Seng Projekt SoSe2019

### Retro - Minigame Sammlung

##Mögliche Spiele
1. Bauernspiel
2. Vier Gewinnt
3. Hangman


Infos zum einbinden der Spiele:
Das Gamemanager Script importiert die Spiele als modul, die einbindung funktioniert bereits. Damit das funktioniert brauchen die Spiele folgenden Aufbau:

def main():
..Spielcode


..Spielcode Ende

if __name__ == "__main__":
  main()

Der Code sorgt dafür dass sich das spiel als modul einbinden lässt, zu testzwecken kann man das script aber auch alleine aufrufen.

Auf die gleiche Weise kann man auch den gamemanager am Ende des Spiels aufrufen:
import Gamemanager
gamemanager.main()
