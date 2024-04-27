# Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo = input("Digite o sexo (F/M): ")

if sexo == 'F' or sexo == 'f':
    print('Sexo: Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Sexo: Masculino')
else:
    print('Sexo Inválido!')