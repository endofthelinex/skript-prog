# Standardeingabestrom

import sys
# Lies solange von Eingabestrom, bis am Anfang das
# Wort "ende" steht. Gib die Eingabe aus.
for line in sys.stdin:
    if "ende" == line.strip():
        print("Skript wird beendet.")
        exit(0)
    else:
        print("-->" + line)
