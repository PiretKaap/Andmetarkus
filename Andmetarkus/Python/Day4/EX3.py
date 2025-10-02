import re

text = "Tere! (Kas sa tuled?)  Ma ei tea...võib-olla,   aga -- vaatame!  Õhtul, kell 18:00, \"Kohvikus\"."


text = re.sub(r'\s+', ' ', text).strip()
text = re.sub(r'\(.*?\)','',text)
text = re.sub(r'\"', '', text)
text = re.sub(r'--', '', text)
text = re.sub(r'  ', ' ', text)
text= text.replace('...', ', ')
print(text)


