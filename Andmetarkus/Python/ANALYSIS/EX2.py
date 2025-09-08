import csv

data_from_csv=[]

with open(r"C:\Users\opilane\Desktop\Andmetarkus,git\Andmetarkus\Python\ANALYSIS\input\CustomerTable.csv", encoding="utf-8") as f:
   # tekitab reader objekti
    reader = csv.reader(f, delimiter=',')
    # teisendab reader objekti listiks
    data_from_csv = list(reader)
    print(data_from_csv)

#esimene rida
insert_statement = "INSERT INTO customer"

#insert_statement ? veergude nimed
insert_statement = insert_statement + f"\n({','.join(data_from_csv[0])}) \nVALUES "
print(insert_statement)
for row in data_from_csv[1:-1]:
    insert_statement += f"\n({','.join(data_from_csv[-1])}),"
insert_statement = insert_statement[:-1]

print(insert_statement)
