#Moodusta eraldi loend names_starting_with_a kuhu lisad a tähega algavad nimed loendist names_sorted (kasuta list comprehensionit)
girl_names = ['Jaanika', 'Malle', 'Kersti', 'Ann', 'Mari', 'Ave', 'Aili', 'Kati']
names_starting_with_a = [name for name in girl_names if 'a'in name]
print(names_starting_with_a)

names_starting_with_A = [name for name in girl_names if name.startswith('A')]
print(names_starting_with_A)

name_shorter_4 = [name for name in girl_names if len(name)<4]
print(name_shorter_4)