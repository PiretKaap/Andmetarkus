# Define a function that checks if a person is an adult (18 years or older)
   # return age >= 18 
def is_adult(age: int) -> bool:
    if not isinstance(age, int) or age < 0 or age > 120 or age == None or age == "" or age == " " :
        return 'Invalid input'
    elif age >= 18:
        return True     
    else:
        return False
       
print(is_adult(66))  # True
print(is_adult('kojkäjl'))  # False
print(is_adult(15))  # False
print(is_adult(-1))  # False

age = 13
if is_adult(age):
    print("Võib valida")
else:
    print("Ei või valida")

eu_northen_country_codes = ['DK', 'EE', 'FI', 'IS', 'LT', 'LV', 'NO', 'SE']
def is_eu_northen_country(country_code):
    if not isinstance(country_code, str) or len(country_code) != 2 :
        return 'Invalid input'
    if country_code in eu_northen_country_codes:
        return True
    else:
        return False
print(is_eu_northen_country('UK')) 
print(is_eu_northen_country('EE')) 
print(is_eu_northen_country('USA'))
print(is_eu_northen_country(55))
print(is_eu_northen_country('Eesti'))   

