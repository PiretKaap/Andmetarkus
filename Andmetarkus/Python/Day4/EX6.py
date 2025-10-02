import pandas as pd
import numpy as np

ilmaandmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "temperatuur": [18.5, 19.2, 17.8, 16.4, 15.9],
    "niiskus": [65, 60, 70, 68, 75],
    "tuul": [4.2, 3.8, 5.0, 4.5, 6.1]
}

linnad_andmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "elanike_arv": [440000, 95000, 51000, 57000, None],
    "pindala": [159.2, 38.8, 32.2, 84.5, 15.0]  # km²
}

ilmaandmed_df = pd.DataFrame(ilmaandmed)

linnad_andmed_df = pd.DataFrame(linnad_andmed)

linnad_andmed_df['elanike_arv'] = linnad_andmed_df['elanike_arv'].fillna(19000)
#print(linnad_andmed_df)

df = pd.merge(ilmaandmed_df,linnad_andmed_df, on='linn')
print(df)

#  Leia, millises linnas on kõrgeim temperatuur.
kõrgeim_temp = df['temperatuur']. idxmax()
kõrgeim_temp_linn = df.loc[kõrgeim_temp, 'linn']
print(kõrgeim_temp_linn)

#  Arvuta iga linna rahvastikutihedus (elanike arv / pindala). Lisaveeruna.
df['rahvastikutihedus'] =(df['elanike_arv']/df['pindala']).round(0)
print(df)

#  Filtreeri välja linnad, kus niiskus on üle 70%.
df_niiskus_70 = df[df['niiskus'] >70]
df_niisked_linnad = df_niiskus_70['linn']
print(df_niisked_linnad)

#  Sorteeri andmed tuule kiiruse järgi kasvavalt.
df_tuul_kasv = df.sort_values('tuul')
print(df_tuul_kasv)

#  Lisa uus veerg, mis näitab, kas temperatuur on üle keskmise ("üle keskmise" / "alla keskmise").
df_keskmine_temp= df['temperatuur'].mean()
df['keskmine_temperatuur'] = np.where(df['temperatuur']>df_keskmine_temp, 'üle keskmise', 'alla keskmise')
print(df)

#  Ühenda ilmaandmed ja elanike andmed üheks DataFrame'iks.
#  Leia, millises linnas on kõige rohkem elanikke.
#  Asenda kõik linnanimed väikeste tähtedega.
#  Eemalda read, kus mõni väärtus on puudu (NaN).
#  Salvesta lõplik DataFrame CSV-failina.