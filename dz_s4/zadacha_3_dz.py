# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import datetime

START_BALANCE = 0
COMISSION = 0.015
MIN_COMISSION = 30
MAX_COMISSION = 600
INTEREST_ON_BALANCE = 0.03
TAX_RICH = 0.1
LIMIT_TAX_RICH = 5_000_000
MENU_ITEMS = ['пополнить', 'снять', 'выйти']


def menu():
    for num, pos in enumerate(MENU_ITEMS, start=1):
        print(f'{num} - {pos}')
    answer = int(input(': '))
    if answer > len(MENU_ITEMS) or answer < 1:
        return menu()
    else:
        return answer


def save_operations(amount, explanation):
    with open('journal.txt', 'a', encoding='UTF-8') as file:
        file.write(str(datetime.datetime.now()) + ' ' + str(amount) + ' ' + explanation + '\n')


def check_the_amount(text):
    amount = int(input(text))
    while amount <= 0 or amount % 50 != 0:
        print('Введите сумму больше 0 и кратную 50.')
        amount = int(input(': '))
    return amount


def put_money(balance):
    amount = check_the_amount('Сумма пополнения? ')
    balance += amount
    print(f'Баланс: {balance}')
    save_operations(amount, 'пополнение')
    return balance


def cash_withdrawals(balance, count_operation):
    amount = check_the_amount('Сумма снятия? ')
    comiss = MIN_COMISSION
    if MIN_COMISSION < (amount * COMISSION) < MAX_COMISSION:
        comiss = round(amount * COMISSION, 2)
    if (amount * COMISSION) > MAX_COMISSION:
        comiss = MAX_COMISSION
    if amount + comiss > balance:
        print(f'Комиссия за снятие: {comiss}. Недостаточно средств на счете')
    else:
        print(f'Комиссия за снятие: {comiss}.')
        balance -= (amount + comiss)
        print(f'Баланс: {balance}')
        save_operations(amount, 'снятие')
        count_operation += 1
    return balance, count_operation


def tax(balance):
    if balance > LIMIT_TAX_RICH:
        tax_amount = round(balance * TAX_RICH, 2)
        print(f'Налог на богатство: {tax_amount}')
        balance -= tax_amount
        print(f'Баланс: {balance}')
        save_operations(tax_amount, 'налог на богатство')
    return balance


def interest_of_balance(balance):
    amount_interest = round(balance * INTEREST_ON_BALANCE, 2)
    print(f'Проценты на остаток после каждой 3й операции: {amount_interest}')
    balance += amount_interest
    print(f'Баланс: {balance}')
    save_operations(amount_interest, 'проценты на остаток')
    return balance


def start():
    balance = START_BALANCE
    with open('journal.txt', 'w') as file:
        file.write(str(datetime.datetime.now()) + ' ' + str(balance) + '\n')
    count_operations = 0
    operation = 0
    while operation != MENU_ITEMS.index('выйти') + 1:
        if count_operations == 3:
            balance = interest_of_balance(balance)
            count_operations = 0
            balance = tax(balance)
        operation = menu()
        match operation:
            case 1:
                balance = put_money(balance)
                balance = tax(balance)
                count_operations += 1
            case 2:
                balance, count_operations = cash_withdrawals(balance, count_operations)
                balance = tax(balance)


start()