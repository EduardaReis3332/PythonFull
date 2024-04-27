# + - * / ** % // math.sqrt()
import math

soma = 3 + 2
sub = 3 - 2
mult = 3 * 2
div = 3 / 2
exp = 3 ** 4 # potência
rQuadradas = 25 ** (1/2) # raiz quadrada sem biblioteca
rQuadrada =  math.sqrt(25) # raiz quadrada com a função da biblioteca Math
resto = 7 % 2 # resto da divisão de um número por outro
div_int = 7 // 2 # resultado inteiro da divisão

print(f'Soma: {soma}\n'
      f'Subtração: {sub}\n'
      f'Multiplicação: {mult}\n'
      f'Divisão: {div}\n'
      f'Exponenciação: {exp}\n'
      f'Raiz quadrada: {rQuadradas}, Raiz quadrada: {rQuadrada}\n'
      f'Resto da divisão: {resto}\n'
      f'Resultado inteiro da divisão: {div_int}')