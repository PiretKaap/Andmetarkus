lilled=['võilill', 'nartsiss', 'tulikas', 'tulp', 'karikakar']
lilled.append('roos') # lisab nimekirja lõppu
lilled.insert(2,'kassitapp') # lisab nimekirja kindlasse kohta
print(lilled)   

puud=['kask', 'mänd', 'kuusk', 'haab', 'pärn']
puud.insert(3,'pappel') # lisab nimekirja kindlasse kohta
print(puud)

taimed=[]
taimed =lilled + puud
print ('taimed:', sorted(taimed))

max(taimed) # leiab nimekirjast maksimaalse väärtuse tähestikulises järjekorras
min(taimed) # leiab nimekirjast minimaalse väärtuse tähestikulises järjekorras
print('maksimaalne taim on:', max(taimed))
print('minimaalne taim on:', min(taimed))

len(taimed) # leiab nimekirja pikkuse
print('taimede nimekirjas on', len(taimed), 'taime')

print(taimed[0]) 


#SET
transaction_customer_id = [1, 2, 3, 4, 4, 5, 6]
print (transaction_customer_id)

unique_customer_id = set(transaction_customer_id) # teeb nimekirjast unikaalsete väärtustega kogumi
print(unique_customer_id)

all_customer_id = set(range(1, 11)) # teeb kogumi vahemikust 1 kuni 10
print(all_customer_id)

passive_customer_id = all_customer_id - unique_customer_id # võtab kogumist välja need, kes on tehingu teinud
print(passive_customer_id)


#Dictionary
my_comapany_data = {"id": 12345678
                    , "name": "Best_Data_Analytic"
                    , "year": {2023: 1111, 2024: 1112} } # sõnastik
print(my_comapany_data)

my_comapany_data["name"] = "Tolgus" # lisab sõnastikku uue võtme ja väärtuse
print(my_comapany_data)

my_comapany_data.update({"address": "Tartu mnt 84"}) # lisab sõnastikku uue võtme ja väärtuse
print(my_comapany_data)

my_comapany_data["year"][2024] = 1000
print(my_comapany_data)

my_comapany_data["year"][2025] = 1113 
print(my_comapany_data)



#Tuple
popular_boys_names = ('Peeter', 'Karl')
print(popular_boys_names)
random_data = ( viis, 5, 5.0)
print(random_data)
