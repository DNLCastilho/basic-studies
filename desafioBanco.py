menu = f"""
{'='*25} MENU {'='*25}\n

                [d] - Depositar
                [s] - Sacar
                [e] - Extrato
                [q] - sair\n
                          
{'='*23} SEU BANCO {'='*23}
"""


saldo = 0
limite = 500
extrato = " "
numero_saques = 0
limite_saques = 3


while True:
    print(menu)
    opcao = input('Escolha o que deseja realizar:')

    if opcao == 'd':  # DEPOSITO
        deposito = float(input(f'Informe o valor que deseja Depositar: '))
        if deposito <= 0:
            print('Valor inválido!')
        else:
            saldo += deposito
            extrato += f"""
            {'Deposito':<15} - R$ {deposito:.2f}\n
            """
            print(f' Operação realizada, valor depositado: R$ {deposito:.2f} ')

    elif opcao == 's':  # SAQUE
        valor_saque = float(input(f'Digite a quantia que deseja sacar:'))
        if valor_saque > saldo:
            print('Saque não realizado, Saldo insuficiente.')
        elif valor_saque > 500:
            print('Saque não realizado, Valor solicitado acima do limite por saque!;')
        elif limite_saques == 0:
            print('Saque não realiza, Limite diário de saques excedido')
        else:
            saldo -= valor_saque
            limite_saques -= 1
            extrato += f"""
            {'SAQUE':<15} - R$ {valor_saque:.2f}\n
            """
            print(f'Operação realizada, valor depositado: R$ {valor_saque:.2f} ')

    elif opcao == 'e':  # EXTRATO
        if extrato == " ":
            print('Não foram realizadas movimentações')
        else:
            print(f'=====================EXTRATO=====================\n' +
              extrato + f'Saldo: R$ {saldo:.2f}\n')

    elif opcao == 'q':  # SAIR
        print('Obrigado por usar SEU BANCO!')
        
        break
    else:
        print('Opção Inválida')
