# Defina um usuário e senha e depois verifique se
# login do usuário é válido.

USUARIO = 'duda'
SENHA = 'duda1321'

while True:
    usuario_login = input('Digite o nome de Usuário: ')
    senha_login = input('Digite a Senha: ')
    
    if usuario_login == USUARIO and senha_login == SENHA:
        print('Login realizado com sucesso!')
        break
    elif usuario_login != USUARIO:
        print(f"O usuário '{usuario_login}' não existe. Tente novamente.")
    elif senha_login != SENHA:
        print('A senha está incorreta. Tente novamente.')
    else:
        print('Usuário e senha incorretos. Tente novamente.')