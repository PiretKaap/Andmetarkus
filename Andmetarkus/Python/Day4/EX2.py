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