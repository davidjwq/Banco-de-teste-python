# Banco de teste

print("Banco de teste")
print("--------------")

# Validando o nome
nome = input("Digite seu nome: ")

while len(nome) < 3:
    print("Nome Inválido! Muito curto.")
    nome = input("Digite seu nome: ")

# Validando o CPF
cpf = input("Digite seu CPF: ")

while len(cpf) != 11:
    print("CPF Inválido! Digite Novamente.")
    cpf = input("Digite seu CPF: ")

print(f"Olá, {nome}! Seja bem-vindo ao Banco de Teste.")
print(f"CPF: ***.***.{cpf[-6:-2]}-{cpf[-2:]}")

# Variáveis do banco
saldo = 1000
saques = 0
opcao = '0'
extrato = []   # lista vazia para guardar as movimentações

while opcao != '5':

    print("")
    print("Escolha uma das opções abaixo.")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Chat")
    print("5 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        print(f"Seu saldo é de R$ {saldo}")

    elif opcao == '2':
        if saques >= 3:
            print("Limite de saques atingido!")
        else:
            tentativas = 0
            saque = float(input('Digite o valor do saque: '))

            while (saque <= 0 or saque > saldo) and tentativas < 3:
                print('Valor inválido!')
                tentativas = tentativas + 1
                if tentativas < 3:
                    saque = float(input('Digite o valor do saque: '))

            if saque > 0 and saque <= saldo:
                saldo = saldo - saque
                saques = saques + 1
                extrato.append(f"Saque: R$ {saque}")   # guarda a movimentação
                print(f'Saque realizado com sucesso! Seu novo saldo é de: R$ {saldo}')
            else:
                print('Não foi possível realizar o saque.')

    elif opcao == '3':
        print("----- Extrato -----")
        if len(extrato) == 0:
            print("Nenhuma movimentação realizada.")
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f"Saldo atual: R$ {saldo}")
        print("--------------------")

    elif opcao == '4':
        print("Chat ainda não implementado, Desculpe.")

    elif opcao == '5':
        print(f"Obrigado por usar o Banco de Teste, {nome}. Até logo!")

    else:
        print("Opção inválida! Tente novamente.")