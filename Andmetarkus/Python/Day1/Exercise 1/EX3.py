age = 18

if age >= 18: 
    print ('Võid hääletada Riigikogu valimistel')
if age >= 16: 
    print ('Võid hääletada KOV valimistel')
else:
    print ('Sa oled liiga noor, et hääletada Riigikogu valimistel')

number_to_check = 100
if number_to_check < 100:
    print(f'Muutuja väärtus {number_to_check} on alla 100')  
elif number_to_check == 100: # või siis: else if
    print(f'Muutuja väärtus {number_to_check} on täpselt 100')   
else:
    print(f'Muutuja väärtus {number_to_check} on üle 100')   

is_adult = age >= 18
print(f'Kas isik on täisealine? {is_adult}')

if age >= 18:
    print('adult')
else: 
    print('not adult')
