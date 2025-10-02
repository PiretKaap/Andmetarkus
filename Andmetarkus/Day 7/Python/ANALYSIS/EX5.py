# paigalda pip install tools.api_request

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# url = "https://demo-datahub.rik.ee/api/v1/meta/classifications"

url_riik = 'https://api.worldbank.org/v2/countries/EST/?format=json'
url_rahvastik_ = 'https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL?format=json'
url_women = "https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL.FE.IN?format=json"
url_male = "https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL.MA.IN?format=json"

response = requests.get(url_rahvastik_)
data = response.json()

response_woman = requests.get(url_women)
data_woman = response_woman.json()

response_male = requests.get(url_male)  
data_male = response_male.json()

# json dumps muudab väljundi terminalis loetavaks
# print(json.dumps(data, indent=2, ensure_ascii=False))

values = {'year': [], 'population': [], "women_population": [], "male_population": []}

# {"year": ["2021", "2020", "2019", ...], "population": [1331057, 1326535, 1324820, ...]}

for item in data[1]:
    values['year'].append(item['date'])
    values['population'].append(item['value'])

for women in data_woman[1]:
    values['women_population'].append(women['value'])

for male in data_male[1]:
    values ['male_population'].append(male['value'])    

# print(json.dumps(values, indent=2, ensure_ascii=False))

df = pd.DataFrame(values)

# väljastan esimesed read
print(df.head())

# joonistamise osa
df.plot(x='year', y=['population', 'women_population', 'male_population'], kind='line', marker='o',
        title='Eesti rahvaarv aastatel 1960-2021', xlabel='Aasta', ylabel='Inimeste arv')
plt.ylim(bottom=0)  # y-telje alumine piir
plt.grid(visible=True)  # võrgustik

plt.savefig('output/population_est.png')
plt.show()



# print(df)

# response_df = pd.json_normalize(data)
# print(response_df)