import getpass
import os

accounts_list = {
    '001-01': {
        'password': '123456',
        'name': 'Fulano da Silva',
        'value': '10',
        'admin': False
    },
    '001-02': {
        'password': '123456',
        'name': 'Siclano da Silva',
        'value': '20',
        'admin': True
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5
}

while True:

    print ("***********************************************")
    print ("******* Paycash - Caixa Eletronico ************")
    print ("***********************************************")

    account_typed = input ('digite sua conta: ')
    password_type = getpass.getpass('digite sua senha: ')

    print(len(account_typed))
    print(password_type)


    if account_typed in accounts_list and password_type == accounts_list[account_typed]['password']:
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)
        print("***********************************************")
        print("******* Paycash - Caixa Eletronico ************")
        print("***********************************************")
        print (" 1 - Saldo")
        print (" 2 - Saque")
        if accounts_list[account_typed]['admin']:
            print('10 - incluir cedulas')
        option_typed = input("escolha uma das opções acima: ")
        if option_typed == '1':
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amount_typed = input('Digite q quantidade da cedula: ')
            money_bill_typed = input ('Digite a denominacao a ser incluida: ')
            money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = input (' Digite o valor a ser sacado: ')

            money_slips_user = {}
            value_int = int(value_typed)

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user ['100'] = value_int // 100
                value_int = value_int - ((value_int // 100) * 100)

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                 money_slips_user['50'] = value_int // 50
                 value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print (' o caixa não tem cedulas disponiveis para esse valor')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                print ('pegue as notas: ')
                print (money_slips_user)
    else:
        print ('conta invalida')

    input ('Pressione <ENTER> para continuar')

