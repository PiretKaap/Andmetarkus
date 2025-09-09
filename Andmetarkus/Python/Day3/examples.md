## Näide: Andmete filtreerimine list comprehensioniga

Oletame, et meil on nimekiri vanustest ja soovime leida kõik vanused, mis on suuremad kui 18:

```python
vanused = [12, 17, 19, 24, 15, 30]
täisealised = [vanus for vanus in vanused if vanus > 18]
print(täisealised)  # Väljund: [19, 24, 30]
```

## Näide: Andmete filtreerimine Pandas abil

Sama ülesanne Pandas teegiga:

```python
import pandas as pd

vanused = [12, 17, 19, 24, 15, 30]
df = pd.DataFrame({'vanus': vanused})
täisealised = df[df['vanus'] > 18]
print(täisealised)
```

## Näide: Autode filtreerimine ja läbisõidu summeerimine

Oletame, et meil on autode andmed sõnastike (dictionary) nimekirjas. Filtreerime autod, mille värv on punane, ja summeerime nende läbisõidu:

```python
autod = [
    {"mark": "Toyota", "vanus": 5, "läbisõit": 80000, "värv": "punane"},
    {"mark": "BMW", "vanus": 3, "läbisõit": 40000, "värv": "must"},
    {"mark": "Audi", "vanus": 7, "läbisõit": 120000, "värv": "punane"},
    {"mark": "Honda", "vanus": 2, "läbisõit": 25000, "värv": "sinine"},
]

punased_autod = [auto for auto in autod if auto["värv"] == "punane"]
punaste_labisõit = sum(auto["läbisõit"] for auto in punased_autod)

print(f"Punasete autode läbisõidu summa: {punaste_labisõit}")
# Väljund: Punasete autode läbisõidu summa: 200000
```

## Näide: Autode filtreerimine ja läbisõidu summeerimine Pandas abil

Sama ülesanne Pandas teegiga:

```python
import pandas as pd

autod = [
    {"mark": "Toyota", "vanus": 5, "läbisõit": 80000, "värv": "punane"},
    {"mark": "BMW", "vanus": 3, "läbisõit": 40000, "värv": "must"},
    {"mark": "Audi", "vanus": 7, "läbisõit": 120000, "värv": "punane"},
    {"mark": "Honda", "vanus": 2, "läbisõit": 25000, "värv": "sinine"},
]

df = pd.DataFrame(autod)
punased_autod = df[df["värv"] == "punane"]
punaste_labisõit = punased_autod["läbisõit"].sum()

print(f"Punasete autode läbisõidu summa: {punaste_labisõit}")
# Väljund: Punasete autode läbisõidu summa: 200000
```