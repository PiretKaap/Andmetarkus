first_name = 'Piret'
surname = 'Kääp'
print(first_name)
print(surname)
full_name = first_name + ' ' + surname
print(full_name)
all_caps = full_name.upper()
print(all_caps)

age = 30
height = 1.62
print(f'Minu nimi on {all_caps} ja pikkus on {height} meetrit ning vanus on {age} aastat.')

print(surname[0])
print(surname[-1]) # prints last character
print(surname[1:3]) #prints characters from index 1 to 2
print(surname[:1]) #prints characters from start to index 2
print(surname[1:]) #prints characters from index 1 to end
hash_name=(surname[0]+ (len(surname)-1)  * surname[0]).lower() # first letter + (length of surname -1) times first letter, all in lowercase
print(hash_name)

initials= first_name[:2] + surname[:2]
print(initials)