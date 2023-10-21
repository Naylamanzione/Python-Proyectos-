import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLUMS=3

symbol_value= {
    "A":2,
    "B":4,
    "C":6,
    "D":8   
    }

symbol_value= {
    "A":5,
    "B":4,
    "C":3,
    "D":2   
    }


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols:int, symbols:dict):
    # Hace aparecer los simbolos la cantidad de veces segun el symbol_count
    all_symbols = []
    for symbol, symbol_value in symbols.items(): #Toma los key y values del diccionario symbols como tuplas en una lista [(A,2)(B,4)] etc
        for _ in range(symbol_value):
            all_symbols.append(symbol)

     #cada column es una lista y cada row es la cantidad de elementos dentro de ella, columns=lista de listas 
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
                print(column[row], end="")

        print()
            
        
        


def deposit():
    while True:
        amount:str=input("Insert the amount you want to deposit: $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please insert a valid amount")
    return amount

def number_lines():
    while True:
        number_of_lines:str=input("Insert the number of lines you want to bet on (From 1 to " + str(MAX_LINES)+"): ")
        if number_of_lines.isdigit():
            number_of_lines=int(number_of_lines)
            if number_of_lines>0 and number_of_lines<=MAX_LINES:
                 break
            else:
                print("Please insert a valid amount (From 1 to " + str(MAX_LINES)+")")
        else:
            print("Please insert a valid amount (From 1 to " + str(MAX_LINES)+")")
    return number_of_lines

def bet_online():
    while True:
        bet:str=input("Insert the amount you want to bet on each line: $")
        if bet.isdigit():
            bet=int(bet)
            if bet>=MIN_BET and bet<=MAX_BET:
                break
            else:
                print(f'Your bet must be between ${MIN_BET}-${MAX_BET}')
        else:
            print("Please insert a valid amount")
    return bet


        
def main(balance):
    new_balance=balance
    lines=number_lines()
    bet=bet_online()
    total=bet*lines
    print(f'Your are betting ${bet} on {lines} lines. Total bet ${total}')
    
    while balance<total:
        print("Not enough funds")
        choice=input("Do you want deposite more or bet less? ")
        if choice.lower()=="deposite more":
            new_balance=deposit()
        else:
            bet=bet_online()
            total=bet*lines

    slots=get_slot_machine_spin(ROWS,COLUMS,symbol_value)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f'You won ${winnings}')
    print(f'You won on lines ',*winning_lines)
    if winnings==0:
        new_balance=new_balance-(bet*lines)
    else:
        new_balance +=winnings
    print(f"Your balance is ${new_balance}")
    return new_balance


            
def slots():
    print("Welcome to the Slots machine")
    start=input("Do you want to play? (Yes/No): ")
    if start.lower()=="no":
        quit()
    elif start.lower()=="yes":
        while True:
            balance=deposit()
            game=main(balance)
            play_again=input("Do you want to play again? (Yes/No): ")
            if play_again.lower()=="no":
              print("You have quit")
              quit()
    else:
        print("Insert valid input")
           
        
    
    
    
            
