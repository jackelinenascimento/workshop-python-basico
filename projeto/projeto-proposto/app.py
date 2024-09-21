import os

dicionario = [{}, {}, {}] # dicionario é uma estrutura de chave e valor

clientes = [{'id': 1, 'nome': 'Grace Hopper', 'email': 'grace@hopper', 'telefone': '123456789', 'status': True}]

# site: https://fsymbols.com/ 

def exibir_nome_programa():
    print ("""
▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 　 ▒█▀▀█ █░░ █▀▀█ █░░█ █▀▀▄ ▒█▀▀█ ░▀░ █▀▀█ █░░ █▀▀ 
▒█▀▀▄ █▄▄█ █░░█ █░░ █░░█ 　 ▒█░░░ █░░ █░░█ █░░█ █░░█ ▒█░▄▄ ▀█▀ █▄▄▀ █░░ ▀▀█ 
▒█▄▄█ ▀░░▀ ▀░░▀ ▀▀▀ ▀▀▀▀ 　 ▒█▄▄█ ▀▀▀ ▀▀▀▀ ░▀▀▀ ▀▀▀░ ▒█▄▄█ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀
    """)


def exibir_opcoes_clientes():
    print ('1. Cadastrar Cliente')
    print ('2. Listar Clientes')
    print ('3. Atualizar dados do Cliente')
    print ('4. Inativar Cliente')
    print ('5. Sair\n')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
        print(f'Opção escolhida: {opcao_escolhida}')   # print(type(opcao_escolhida)) # <class 'str'>
        
        if opcao_escolhida == 1:
            cadastrar_cliente()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            atualizar_cliente()
        elif opcao_escolhida == 4:
            inativar_cliente()
        elif opcao_escolhida == 5:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def cadastrar_cliente():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    print ('Cadastrar Cliente\n')
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')
    clientes.append({'id': len(clientes) + 1, 'nome': nome, 'email': email, 'telefone': telefone, 'status': True})
    print ('Cliente cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal...')
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    main()

def listar_clientes():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    print ('Listar Clientes\n')
    for cliente in clientes:
        status = 'Ativo' if cliente['status'] else 'Inativo'
        print (f" Id: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']} | Telefone: {cliente['telefone']} | Status: {status}")
    input('Digite uma tecla para voltar ao menu principal...')
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    main()

def atualizar_cliente():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    print ('Atualizar dados do Cliente\n')
    id_cliente = int(input('Digite o id do cliente que deseja atualizar: '))
    while id_cliente > len(clientes) or id_cliente < 1:
        print ('Cliente não encontrado')
        id_cliente = int(input('Digite o id do cliente que deseja atualizar: '))
    cliente = clientes[id_cliente - 1]
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')
    cliente['nome'] = nome
    cliente['email'] = email
    cliente['telefone'] = telefone
    print ('Cliente atualizado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal...')
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    main()

def inativar_cliente():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    print ('Inativar Cliente\n')
    id_cliente = int(input('Digite o id do cliente que deseja inativar: '))
    while id_cliente > len(clientes) or id_cliente < 1:
        print ('Cliente não encontrado')
        id_cliente = int(input('Digite o id do cliente que deseja inativar: '))
    cliente = clientes[id_cliente - 1]
    cliente['status'] = False
    print ('Cliente inativado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal...')
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    main()

def opcao_invalida():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    print ('Opção inválida')
    input('Digite uma tecla para voltar ao menu principal...')
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    main()

def finalizar_programa():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    print ('Programa finalizado')

def main():
    os.system('clear') # Limpa a tela do terminal, para Windows use 'cls'
    exibir_nome_programa()
    exibir_opcoes_clientes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()