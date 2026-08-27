import  random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLUMNS = 3

symbol = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def working_of_sm(columns, number_of_lines, get_bet, values):
    winnings = 0
    winning_lines = []
    for line in range(number_of_lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* get_bet
            winning_lines.append(line +1 )
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbol):
    all_symbol = []
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for row in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append((column))
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The number should be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def lines():
    while True:
        lines = input("Enter the number of lines (1-"+ str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def bet():
    while True:
        amount = input("Enter the amount to bet on each line: $")
        # cope = deposit()
        if amount.isdigit():
            amount = int(amount)
            # if amount > cope:
            #     print("Your balance isn't capable")
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount should be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def game(balance):
    number_of_lines = lines()
    while True:
        get_bet = bet()
        total_bet = get_bet * number_of_lines
        if total_bet > balance:
            print("Your balance isn't capable to bet that amount.")
        else:
            # print(f"You are betting ${get_bet} on {number_of_lines} lines. Total bet is equal to ${total_bet}")
            break
    print(f"You are betting ${get_bet} on {number_of_lines} lines. Total bet is equal to ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol)
    print_slot_machine(slots)
    winnings, winning_lines = working_of_sm(slots, number_of_lines, get_bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += game(balance)
    print(f"You are left with ${balance}")
main()