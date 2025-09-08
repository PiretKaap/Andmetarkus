
import pandas as pd

file_name = r'C:\Users\opilane\Desktop\Andmetarkus,git\Andmetarkus\Python\ANALYSIS\input\ProductTable.xlsx'
data = pd.read_excel(file_name)
data_dict = data.to_dict(orient='records') # paigutab read eraldi sõnastikesse
print(data_dict)

file_name_csv = r'C:\Users\opilane\Desktop\Andmetarkus,git\Andmetarkus\Python\ANALYSIS\input\CustomerTable.csv'
data_csv = pd.read_csv(file_name_csv)
data_dict_csv = data_csv.to_dict # paigutab kõik veerud eraldi sõnastikku
print(data_dict_csv)