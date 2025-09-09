import pandas as pd 

data  = pd.read_excel('Python\Day3\Tallinn-Harku-2004-2024.xlsx')

df = pd.DataFrame(data)

df_2024 = df[df['Aasta'] == 2024]

#Salvesta uus excel
df_2024.to_csv('Python\Day3\Tallinn-Harku-2024.csv', index=False)