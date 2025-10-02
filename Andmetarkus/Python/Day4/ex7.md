# Andmete laadimine veebilehelt ja nende välja lugemine

## Lühijuhend: Kuidas saada andmed veebilehelt BeautifulSoup abil

1. **Paigalda vajalikud paketid:**
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Näide andmete lugemisest:**
   ```python
   import requests
   from bs4 import BeautifulSoup

   url = "https://www.example.com"
   response = requests.get(url)
   soup = BeautifulSoup(response.text, "html.parser")

   # Näide: leia kõik pealkirjad (h1)
   for h1 in soup.find_all("h1"):
       print(h1.text)
   ```

3. **Kokkuvõte:**
   - `requests.get(url)` laeb veebilehe sisu.
   - `BeautifulSoup(..., "html.parser")` võimaldab HTML-i töödelda.
   - `soup.find_all("elemendi_nimi")` leiab kõik soovitud elemendid (nt "table", "tr", "td", "a" jne).


   # ÜLESANNE

   