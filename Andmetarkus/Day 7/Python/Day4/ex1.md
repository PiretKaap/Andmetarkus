# Regex

Viide, kus saab regex-it testida:

[regex101.com](https://regex101.com)

## Olulisemad regex näited ja selgitused

| Regex         | Selgitus                                      | Näide sobivusest         |
|---------------|-----------------------------------------------|--------------------------|
| `.`           | Suvaline üks märk                             | `a`, `1`, `?`            |
| `\d`          | Üks number (0-9)                             | `5`, `0`                 |
| `\w`          | Üks täht, number või alakriips (_)            | `a`, `Z`, `7`, `_`       |
| `\s`          | Üks tühik (whitespace)                        | ` `, `\t`, `\n`          |
| `^`           | Algus                                         | `^a` leiab "a" rea alguses|
| `$`           | Lõpp                                          | `a$` leiab "a" rea lõpus |
| `*`           | 0 või rohkem korda                            | `ab*` leiab `a`, `ab`, `abb` jne |
| `+`           | 1 või rohkem korda                            | `ab+` leiab `ab`, `abb` jne, aga mitte `a` |
| `?`           | 0 või 1 kord                                  | `ab?` leiab `a` või `ab` |
| `{n}`         | Täpselt n korda                               | `a{3}` leiab `aaa`       |
| `{n,}`        | Vähemalt n korda                              | `a{2,}` leiab `aa`, `aaa`, ... |
| `{n,m}`       | Vahemikus n kuni m korda                      | `a{2,4}` leiab `aa`, `aaa`, `aaaa` |
| `[abc]`       | Üks märk valikust                             | `a`, `b` või `c`         |
| `[^abc]`      | Üks märk, mis EI OLE valikus                  | kõik peale `a`, `b`, `c` |
| `(abc)`       | Grupp                                         | leiab täpselt `abc`      |
| `|`           | Või                                           | `a|b` leiab `a` või `b`  |
| `\`           | Põgenemismärk (escape)                        | `\.` leiab punkti `.`    |

**Näiteid:**

- `^\d{3}-\d{2}-\d{4}$` — sobib kujule `123-45-6789` (nt isikukood)
- `^[A-Z][a-z]+$` — sobib sõnale, mis algab suure tähega ja järgneb väikseid tähti (nt `Kaido`)
- `\b\w{4}\b` — leiab kõik 4-tähelised sõnad

### Tekst, millest otsida '\n' märki

    See on esimene rida.
    See on teine rida.
    Kolmas rida on siin.
    Neljandal real on samuti tekst.

#### Vastus:

Tekstis esineb **3** '\n' märki.

## Ülesanne: Leia kuuekohalised kontod, mis algavad 3-ga

Kirjuta regex, mis leiab ainult need numbrid, mis on täpselt 6-kohalised ja algavad numbriga 3.

### Näidistekst

Minu kontonumber on 345678, aga vana konto oli 312345. Mõned näited, mida ei tohiks leida: 234567, 34567, 33445566, 39876, 399999, 3123457, 31234. Samuti on olemas 398765 ja 300001.

#### Vastus:

- 345678
- 312345
- 399999
- 398765
- 300001


## Regex näide Eesti telefoninumbrite leidmiseks

Oletame, et soovid leida Eesti telefoninumbreid erinevates vormingutes. Näiteks sobib järgmine regex:

```regex
(\+372[\s-]?)?(\(?372\)?[\s-]?)?(\d{2,4}[\s-]?\d{3}[\s-]?\d{3,4})
```

### Näidistekst

Tere! Minu telefoninumber on 51234567, kuid töö jaoks kasutan tihti ka vormingut +372 5123 4567. Mõnikord kirjutatakse numbrid ka nii: 372-5123-4567 või isegi (372) 5123 4567. Mõned inimesed lisavad vahele tühikuid, näiteks 51 234 567 või +372-51-234-567. Vanemad kontaktid võivad olla kujul 6 123 456 või 6123456. Palun helista mulle, kui vajad abi!

#### Vastus:

- 51234567
- +372 5123 4567
- 372-5123-4567
- (372) 5123 4567
- 51 234 567
- +372-51-234-567
- 6 123 456

