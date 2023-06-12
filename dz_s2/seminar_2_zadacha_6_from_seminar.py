# Напишите программу банкомат.
# Начальная сумма равно нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия карты 50 уе
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 уе
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счете
# При привышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операций, даже ошибочной
# любое действие выводит сумму денег

BUDGET = 0
COMISSION = 0.015
INTEREST_ON_BALANCE = 0.03
TAX_RICH = 0.9

def atm(start_budget, bank_commmis, interest, tax):
    menu = ['пополнить', 'снять', 'выйти']
    answer = ''
    num_of_operations = 0
    bank_acc = start_budget
    while answer != menu.index('выйти') + 1:
        print(f'Остаток: {bank_acc}')
        if num_of_operations == 3:
            bank_acc = bank_acc + (bank_acc * interest)
            num_of_operations = 0
            print('3%:', bank_acc * interest, ' - ', bank_acc)
        for num, pos in enumerate(menu, start=1):
            print(f'{num} - {pos}')
        answer = int(input(': '))
        if bank_acc > 5000000:
            print(f'{round(bank_acc - bank_acc * tax, 3)} - налог 10%')
            bank_acc = bank_acc * tax
            print(f'Остаток: {round(bank_acc, 3)}')
        match answer:
            case 1:
                bank_acc += int(input('Сумма пополнения? '))
            case 2:
                amount = int(input('Сумма снятия? '))
                comiss = 30
                if (amount * bank_commmis) > 30 and (amount * bank_commmis) < 600:
                    comiss = amount * bank_commmis
                if (amount * bank_commmis) > 600:
                    comiss = 600
                if amount + comiss > bank_acc:
                    print(f'{round(comiss, 3)} - комиссия 1.5%. Недостаточно средств на счете')
                else:
                    bank_acc -= (amount + comiss)
                    print(f'{round(comiss, 3)} - комиссия 1.5%')
            case _:
                continue
    num_of_operations += 1


atm(BUDGET, COMISSION, INTEREST_ON_BALANCE, TAX_RICH)
