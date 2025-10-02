import requests
from bs4 import BeautifulSoup

link = "https://www.reisiekspert.ee/et/reiside-eripakkumised/55-egiptus"

response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")

reisi_kaart = soup.find_all("div", class_="card-body")

reiside_andmed = []

for reis in reisi_kaart:
    reisi_nimi = reis.find("h2").text.strip()
    reisi_hind = reis.find("span", class_="promohind_realopus")
    if reisi_hind is None:
        continue
    # võtame väärtuse tekstiväljalt ja puhastame liigsest
    reisi_hind = reisi_hind.text.strip().replace("€", "").replace(
        "\n                                                            \xa0", "")
    # pakime kokku tupleks
    reisi_andmed = reisi_nimi, int(reisi_hind)

    reiside_andmed.append(reisi_andmed)

    print(reisi_andmed)