# Receba um número e mostre todos dos números pares de 0 ate esse número.

num = int(input('Digite um número: '))

i = 1

while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1