import requests
import pandas as pd 

url = "https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php"

reponse= requests.get(url)
xml_content = reponse.content

df = pd.read_xml(xml_content, xpath='.//place')

min_temp = df[df['tempmin'] == df['tempmin'].min()]
max_temp = df[df['tempmax'] == df['tempmax'].max()]
grouped = df.groupby('tempmin').size().reset_index(name="count")

#print(min_temp)
#print(max_temp)
print(grouped)

