import textwrap


def menu():
    menu_str = textwrap.dedent("""\
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """)
    return input(menu_str)


def depositar(valor_deposito, saldo, extrato, /):
    if valor_deposito <= 0:
        print('Valor inválido!')
    else:
        saldo += valor_deposito
        extrato += f"Deposito:\tR${valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    return saldo, extrato


def sacar(*, valor_saque, saldo, extrato, limite_saque, max_saques, saques_feitos):
    if valor_saque <= 0:
        print('Saque não realizado, valor informado é inválido')
    elif valor_saque > saldo:
        print('O saque não pode ser concluído porque o saldo é insuficiente.')
    elif valor_saque > limite_saque:
        print('O saque não pode ser concluído porque o valor solicitado está acima do limite por saque!')
    elif saques_feitos >= max_saques:
        print(
            'O saque não pode ser concluído porque o limite diário de saques foi excedido.')
    else:
        saldo -= valor_saque
        extrato += f"Saque:\t{valor_saque:.2f}\n"
        saques_feitos += 1
        print("\n=== Saque realizado com sucesso! ===")
    return saldo, extrato, saques_feitos


def extrato_mov(saldo, extrato):
    print(f"|{'='*25}EXTRATO{'='*25}|\n")
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"O saldo em sua conta é R$ {saldo:.2f}")
    print(f"|{'='*56}|\n")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")

    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            print("Já existe um usuário cadastrado com este CPF.")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento,
                    'CPF': cpf, 'endereço': endereco})


def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario (apenas números): ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


MAXIMO_SAQUES = 3
LIMITE_SALDO = 500
AGENCIA = "0001"

saldo = 0
extrato = ""
saques_feitos = 0
contas = []
usuarios = []

while True:
    opcao = menu()

    if opcao == 'd':
        valor_deposito = float(input('Insira o valor a ser depositado: '))
        saldo, extrato = depositar(valor_deposito, saldo, extrato)
        print(f"O Valor depositado foi de R${valor_deposito:.2f}")

    elif opcao == 's':
        valor_saque = float(input('Insira o valor a ser sacado: '))
        saldo, extrato, saques_feitos = sacar(
            valor_saque=valor_saque,
            saldo=saldo,
            extrato=extrato,
            limite_saque=LIMITE_SALDO,
            max_saques=MAXIMO_SAQUES,
            saques_feitos=saques_feitos)
        print(f"O valor sacado é de R$ {valor_saque:.2f}")

    elif opcao == 'e':
        extrato_mov(saldo, extrato)

    elif opcao == 'q':
        print(f"Obrigado por usar SEU BANCO!")
        break

    elif opcao == 'nu':
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
