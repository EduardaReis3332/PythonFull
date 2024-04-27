# Escreva um programa que receba notas de um aluno (de 0 a 10), caso
# a nota digita esteja  fora do intervalo aceito, o programa deve imprimir: "Nota invalida!" e pedir para digitar outra nota.

while True:
    nota = int(input("Digite a nota do aluno: "))
    if nota >= 0 and nota <= 10:
        print(f'Nota {nota} registrada com sucesso!')
        break
    
    print('Nota inválida. Tente novamente.')