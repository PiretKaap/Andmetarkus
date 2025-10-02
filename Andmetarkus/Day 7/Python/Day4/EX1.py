# regex
import re

string = "Minu kontonumber on 345678, aga vana konto oli 312345. Mõned näited, mida ei tohiks leida: 234567, 34567, 33445566, 39876, 399999, 3123457, 31234. Samuti on olemas 398765 ja 300001."

matches= re.findall(r'\b3\d{5}\b', string)
print(matches)

text2 = """See on esimene rida.
See on teine rida.
Kolmas rida on siin.
Neljandal real on samuti tekst."""

matches2 = r'\n'
Text2_ilma_reavahetuseta= text2.replace('\n',' ')
print(Text2_ilma_reavahetuseta)
