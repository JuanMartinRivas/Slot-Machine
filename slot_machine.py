# Main file for my slot machine program
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def get_slot_machine_spin(rows, colums, symbols):  # Function for getting a random spin
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(colums):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def check_for_win(columns, lines, bet, values):  # Function for checking if the player won
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol_to_check != symbol:
                symbol = None
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line + 1)

    return winnings, winning_lines

def print_slot_machine_spin(columns):  # Function for printing the spin
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="\n")

def deposit():  # Function for depositing money
    while True:
        try:
            deposit_amount = int(input("How much would you like to deposit? $"))
            if deposit_amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a number.")

    return deposit_amount

def get_number_of_lines():  #Gets the number of lines to play
    while True:
        try:
            number_of_lines = int(input("How many lines would you like to play? "))
            if number_of_lines > 0 and number_of_lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a number.")
    
    return number_of_lines

def get_bet_amount():  #Gets the bet amount
    while True:
        try:
            bet_amount = int(input("How much would you like to bet on each line? $"))
            if bet_amount >= MIN_BET and bet_amount <= MAX_BET:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a number.")

    return bet_amount 

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You don't have enough money to make that bet. Your current balance is ${balance}.")
        else:
            break
    print (f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_for_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    if len(winning_lines) > 0:
        print(f"You won on lines {winning_lines}!")
    else:
        print("You didn't win on any lines.")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}.")
        if balance == 0:
            print("You have no money left. Goodbye.")
            break
        play = input("Would you like to play? (y/n) ")
        if play == "y":
            balance += spin(balance)
        elif play == "n":
            print("Goodbye.")
            break
        else:
            print("Please enter y or n.")

main()
