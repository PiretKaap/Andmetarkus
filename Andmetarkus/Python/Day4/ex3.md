## Millal on vaja teksti normaliseerida?

Teksti normaliseerimist kasutatakse siis, kui soovime teha tekstiga automaatset töötlust või analüüsi, näiteks otsing, võrdlus, statistika või masinõpe. Normaliseerimine aitab eemaldada erinevused, mis pole sisuliselt olulised, kuid võivad mõjutada tulemusi. Näiteks:

- Sõnade võrdlemisel (kas "Õun" ja "õun" on sama sõna?)
- Otsingumootorites, et otsingutulemused oleksid täpsemad
- Teksti sagedusanalüüsis, et "banaan" ja "Banaan" loetaks üheks sõnaks
- Masinõppe mudelites, et vähendada müra ja parandada mudeli täpsust
- Kirjavahemärkide ja liigsete tühikute eemaldamiseks enne sõnade loendamist või tekstist võtmesõnade leidmist

Normaliseerimine muudab teksti ühtlasemaks ja lihtsustab edasist automaatset töötlemist.

### Näide teksti normaliseerimisest

```python
import re

text = "See on Näide! Tekstist, mida normaliseerida:  Õunad, pirnid ja banaanid."

# 1. Väiketähed
text = text.lower()

# 2. Kirjavahemärkide eemaldamine
text = re.sub(r'[^\w\s]', '', text)

# 3. Ülearuste tühikute eemaldamine
text = re.sub(r'\s+', ' ', text).strip()

print(text)
# väljund: see on näide tekstist mida normaliseerida õunad pirnid ja banaanid
```
### Näide, kus oleks vaja teksti korrastada

Algne tekst:
```
Tere! (Kas sa tuled?)  Ma ei tea...võib-olla,   aga -- vaatame!  Õhtul, kell 18:00, "Kohvikus".
```
#### Koodinäide: liigsete tühikute eemaldamine

```python
import re

text = "Tere!   (Kas sa tuled?)  Ma ei tea...võib-olla,   aga -- vaatame!  Õhtul, kell 18:00, \"Kohvikus\"."

# Eemalda liigsed tühikud (asenda mitu tühikut ühega)
text = re.sub(r'\s+', ' ', text).strip()

print(text)
# väljund: Tere! (Kas sa tuled?) Ma ei tea...võib-olla, aga -- vaatame! Õhtul, kell 18:00, \"Kohvikus\"."
```

#### Koodinäide: sulgude eemaldamine

```python
import re

text = "Tere! (Kas sa tuled?) Ma ei tea...võib-olla, aga -- vaatame! Õhtul, kell 18:00, \"Kohvikus\"."

# Eemalda kõik sulud ja nende sees olev tekst
text = re.sub(r'\(.*?\)', '', text)

print(text)
# väljund: Tere!  Ma ei tea...võib-olla, aga -- vaatame! Õhtul, kell 18:00, "Kohvikus".
```

#### Täienda koodi selliselt, et eemaldataks ka märk \"


