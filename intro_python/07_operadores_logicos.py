# Definindo algumas variáveis para operações aritméticas
a = 5
b = 10
c = 15

soma = a + b
subtracao = b - c
multiplicacao = a * b
divisao = c / a
exponenciacao = a ** 2
raiz_quadrada_a = a ** 0.5
raiz_quadrada_b = b ** 0.5
resto_divisao = c % a
divisao_inteira = c // a

resultado1 = (soma > multiplicacao) and (divisao < subtracao)
resultado2 = (raiz_quadrada_a < raiz_quadrada_b) or (resto_divisao != 0)
resultado3 = not (divisao_inteira == 0)

print("Exemplo de operações lógicas com operações aritméticas:")
print(f'Resultado 1: {(soma > multiplicacao)} and {(divisao < subtracao)} = {resultado1}')
print(f'Resultado 2: {(raiz_quadrada_a < raiz_quadrada_b)} or {(resto_divisao != 0)} = {resultado2}')
print(f'Resultado 3: not {(divisao_inteira == 0)} = {resultado3}')