# Receba 4 notas de um aluno e exiba se ele foi aprovado(nota maior ou igual a 6) 
# se ele ficou de recuperação(nota maior ou igual a 4) ou se ele foi
# reprovado(nota menor do que 4)

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))

media = (n1 + n2 + n3 + n4)/4

if media >= 6:
    print(f'A média do aluno foi: {media} e ele está APROVADO!')
elif media >= 4:
    print(f'A média do aluno foi: {media} e ele está em RECUPERAÇÃO.')
else:
    (print(f'A média do aluno foi: {media} e ele está REPROVADO.'))