import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(columns[row], "|")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("Quanto você gostaria de depositar? \n$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('A quantidade depositada deve ser maior que 0')
        else:
            print('Número inválido, tente novamente.')
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Em quantas linhas você quer apostar? (1 - " + str(MAX_LINES) + ')  \n# ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('A quantidade deve ser maior que 0.')
        else:
            print('Número inválido, tente novamente.')

    return lines

def get_bet():
    while True:
        bet = input('Quando você deseja apostar em cada linha? \n$ ')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'A quantidade apostada deve estar entre ${MIN_BET} e ${MAX_BET}')
        else:
            print('Número inválido, tente novamente.')

    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'Você não depositou o suficiente para essa aposta.\n\tValor depositado: {balance}\n\tLinhas apostadas: {lines}')
        else:
            break
    print(f'Você está apostando ${bet} em {lines} linhas.\nO valor da aposta total é ${total_bet}')


main()