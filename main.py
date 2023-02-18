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

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines)
    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
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
                print(column[row], end=" | ")
            else:
                print(column[row], end='')
        print()

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

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'Você não depositou o suficiente para essa aposta.\n\tValor depositado: {balance}\n\tLinhas apostadas: {lines}')
        else:
            break
    print(f'Você está apostando ${bet} em {lines} linhas.\nO valor da aposta total é ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'Você ganhou ${winnings}')
    print(f'Você ganhou em:', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Carteira atual: ${balance}')
        resposta = input('Confirme para jogar. (Q para sair)')
        if resposta.lower() == 'q':
            break
        balance += spin(balance)
    print(f'Você finalizou com ${balance}')

main()