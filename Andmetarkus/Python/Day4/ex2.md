## Millal kasutatakse NLTK teeki?

NLTK (Natural Language Toolkit) kasutatakse peamiselt tekstianalüüsi ja loomuliku keele töötluse (NLP) ülesannete lahendamiseks. Mõned levinumad kasutusjuhud:

- Teksti tükeldamine (tokeniseerimine) sõnadeks ja lauseteks
- Sõnade põhivormide leidmine (lemmatiseerimine, stemming)
- Sõnade sageduse analüüs ja sõnapilvede loomine
- Teksti puhastamine ja filtreerimine (nt stoppsõnade eemaldamine)
- Teksti märgendamine (POS-tagging, ehk sõnaliikide määramine)
- Keele tuvastamine ja tekstide klassifitseerimine
- Sõnade ja fraaside vaheliste seoste leidmine (n-grammid, kollokatsioonid)
- Teksti sisu analüüs, nt sentiment analysis

NLTK on populaarne tööriist eesti ja inglise keele tekstide töötlemiseks ning sobib hästi nii õppe- kui ka uurimistöödeks.

### Näidistekst, mille puhul võiks NLTK-d kasutada

"Ilm on täna väga ilus. Hommikul paistis päike ja linnud laulsid. Õhtul võib sadada vihma, kuid nädalavahetusel lubatakse taas sooja ilma. Inimesed naudivad kevadet ja pargid on rahvast täis."

Selle teksti puhul saab NLTK abil:
- Tükeldada tekst lauseteks ja sõnadeks
- Leida sagedasemad sõnad
- Eemaldada stoppsõnad (nt "on", "ja", "kuid")
- Märgendada sõnaliigid (nt nimisõnad, tegusõnad)

#### Python näidiskood iga loetelu elemendi kohta (eeldab, et `nltk` on paigaldatud: pip install nltk)


```python
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = ("Ilm on täna väga ilus. Hommikul paistis päike ja linnud laulsid. "
        "Õhtul võib sadada vihma, kuid nädalavahetusel lubatakse taas sooja ilma.")

# Laadi vajalik tokenizer (vajalik vaid esmakordselt)
nltk.download('punkt')

# Lauseiteks (estonian proovib üldreeglitega; kui eesti keele tuge pole, kasutab üldist)
lauseed = sent_tokenize(text)
# Sõnadeks
sonad = word_tokenize(text)

print("Lauseid:", lauseed)
print("Sõnad:", sonad)
```