#Näide loendist, kus igal sõnal on alguses või lõpus 4 lisatühikut:

sõnad = ["    õun", "banaan    ", "    pirn    ", "ploom", "    viinamari    "]

#todo
#Eemalda sõnade loendis liigsed tühikud

Ilma_tühikuteta = [sõnad.replace(' ','') for sõnad in sõnad]
print(Ilma_tühikuteta)



#Näide lähteandmetest:

summad = ["1,234.56", "12,000.00", "5,678.90", "100.00", "23,456.78"]

#todo
#Moodusta uus järjend, kus summades on eraldatud tuhande eristaja "," ning sõne on teisendatud ujukomaarvuks (float)

numbrina = []
for summad in summad:
    summad = summad.replace(',','')
    numbrina.append(float(summad))

print(numbrina)

# Ülesanne 2 - A ja E riigid

riigid = ["Eesti", "Austria", "Belgia", "Andorra", "Hispaania", "Soome", "Albaania", "Itaalia"]

riigid_A_E = [riigid for riigid in riigid if riigid.startswith ('A') or riigid.startswith('E')]
print(riigid_A_E)

# Ülesanne 3
print('Ülesanne 3')

toidud = {
    "õun": {
        "kalorsus": 52,
        "vitamiinid": ["C", "K", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 14,
        "rasv": 0.2,
        "valk": 0.3
    },
    "banaan": {
        "kalorsus": 89,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 23,
        "rasv": 0.3,
        "valk": 1.1
    },
    "kanafilee": {
        "kalorsus": 165,
        "vitamiinid": ["B3", "B6", "B12"],
        "mineraalid": ["Fosfor", "Seleen"],
        "süsivesikud": 0,
        "rasv": 3.6,
        "valk": 31.0
    },
    "kartul": {
        "kalorsus": 77,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Raud"],
        "süsivesikud": 17,
        "rasv": 0.1,
        "valk": 2.0
    },
    "lõhe": {
        "kalorsus": 208,
        "vitamiinid": ["D", "B12", "B6"],
        "mineraalid": ["Seleen", "Fosfor"],
        "süsivesikud": 0,
        "rasv": 13.0,
        "valk": 20.0
    },
    "riis": {
        "kalorsus": 130,
        "vitamiinid": ["B1", "B3", "B6"],
        "mineraalid": ["Magneesium", "Fosfor"],
        "süsivesikud": 28,
        "rasv": 0.3,
        "valk": 2.7
    }
}
print('I')
#Otsida välja kõik toidud, mille mineraalide hulgas on "Kaalium", ja väljasta nende nimed terminali.
Kaaliumiga_toidud = [toit for toit, data in toidud.items() if 'Kaalium' in data['mineraalid']]
print(Kaaliumiga_toidud)

print('II')
# Lisada lisatunnus "makro" väärtusega "süsivesikurohke", "rasvane" kui vastav osakaal makrotoitainetest on üle 50%. Muudel juhtudel lisa tekst "mitmekülgne"

for toit, data in toidud.items():

    kokku= data["süsivesikud"] + data["rasv"] + data["valk"]

    if kokku == 0:
        data["makro"] = "mitmekülgne"
    elif (data["süsivesikud"] / kokku) * 100 > 50:
        data["makro"] = "süsivesikurohke"
    else:
        (data["rasv"] / kokku) * 100 > 50
        data["makro"] = "rasvane"

print(toidud)

print('III')
#Otsida välja kõik toidud, mille vitamiinide hulgas on vähemalt kaks B vitamiini ja lisa need uude sõnastikku "b_vitaamini_rikkad"
b_vitamiini_rikkad = [] # Teen listi

for toit, data in toidud.items(): # Kust tulevad andmed

    b_vitamiini_arv = sum(
        1 for vitamiin in data["vitamiinid"] if vitamiin.startswith ('B')) # Kui palju on B vitamiine toidus
    
    if b_vitamiini_arv >= 2:
        b_vitamiini_rikkad.append(toit) # Kui on rohkem kui 2 B-vitamiini siis lisa listi
        
print("B vitamiini rikkad toidud:", b_vitamiini_rikkad)  # Prindi välja B-vitamiini rikkad toidud. 
        