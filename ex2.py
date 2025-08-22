cuvant = str(input("Introdu cuvantul dorit: "))
cuvant = cuvant.lower()
value = 0
vocale = ['a', 'e', 'i', 'o', 'u']
for i in cuvant:
    if i == 'x':
        value += 5
    elif i in vocale:
        value += 3
    else:
        value += 1
if len(cuvant) > 6 and len(cuvant) < 15:
    value += 10
print(f"Valoarea cuvantului este {value}.") 