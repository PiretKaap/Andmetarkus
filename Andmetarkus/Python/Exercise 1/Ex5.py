girl_names = ['Jaanika', 'Malle', 'Kersti', 'Ann', 'Mari', 'Kati']
for name in girl_names:
    print(name)
print('I')
for i in range(2):
    print(girl_names[i])

print('II')
for name in girl_names[:2]:
    print(name)
print('teine kuni neljas')
for name in girl_names[1:4]: # 2nd, 3rd and 4th
    print(name)

print('Lahendus elemendid tagurpidi')
for name in reversed(girl_names):
    print(name)

print('Lahendus paaris indeksiga elemendid') # iga teine element
for i in range(0,len(girl_names), 2):
    print(girl_names[i])

print('Lahendus K-tähega algavad nimed')
for name in girl_names:
    if name.startswith('K'):
        print(name)

print('Sõnastik M-tähega algavad nimed')
sorted_names = {"M": []}

for name in girl_names:
    if name.startswith("M"):
        sorted_names["M"].append(name)
print(sorted_names)

print('Sõnastik esitähtede järgi')
sorted_names = {}

for first_letter in girl_names:
    if name.startswith(first_letter):
        sorted_names[first_letter].append(name)
print(sorted_names)


