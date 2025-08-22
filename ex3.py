sir = str(input("Introdu sirul de caractere aici: "))
cifre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in sir:
    if i in cifre:
        print("Ai introdus un numar.")
        break
    else:
        print("Ai introdus un text.")
        break

sir = list(sir)
for i in sir:
    if i == " ":
        sir.pop(sir.index(i))
sir_inversat = sir[::-1]
if sir == sir_inversat:
    print("Sirul introdus este un palindrom! :)")
else:
    print("Sirul introdus NU este un palindrom! :()")