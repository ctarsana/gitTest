a = 0
b = 1
fibonacci = [a, b]
n = int(input('Introdu o valoare pentru n: '))
for i in range (1, n):
    new_element = fibonacci[i-1] + fibonacci[i]
    fibonacci.append(new_element)

print(fibonacci)
suma = sum(fibonacci)
average = suma / len(fibonacci)
print(f"Suma elementelor este {suma}, iar valoarea medie este {average}.")
