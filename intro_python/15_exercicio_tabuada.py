# Receba um número do usuário e mostre a tabuada esse número

n1 = int(input('Digite o valor que queres saber a tabuada: '))

i = 1
while i <= 10:
    print(f'{n1} x {i} = {n1*i}')
    i += 1