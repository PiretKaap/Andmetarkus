# Andmete analüüs ja visualiseerimine

import glob
import json
from datetime import datetime

# Andmete analüüs ja visualiseerimine
el_data = []

print("test")

path = "Python\Day3\Elektrihind"

# Lae kõik 2025. aasta JSON failid kaustast
for filename in glob.glob(path + "/*.json"):
    print(f"Laen andmed failist: {filename}")
    if "2025" in filename:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            el_data += data['data']


# Salvesta el_data faili
with open(path + "el_data_2025.json", "w", encoding="utf-8") as f:
    json.dump({"data": el_data}, f, ensure_ascii=False, indent=2)
print("Andmed salvestatud faili el_data_2025.json")