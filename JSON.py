# Erstellen von JSON Files 
import json
with open ("studenten_note.txt","w") as f:
#INDENT und Seperators zur formatierung
    json.dump (personen_dict,f,indent=4,separators=(",",":"),sort_keys=True)
