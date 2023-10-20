import random

opciones:list=["rock","paper","sissors"]
print("Welcome to the classic Rock Paper Sissors! You will be face against the computer, the first one to win 3 times wins!!")

def rockpaper():
    i:int=0
    j:int=0
    while i!=3 and j!=3:
        choice:str=input("Type rock/paper/sissors or Q to quit ").lower()
        select:int=random.randint(0,2)
        computer:str=opciones[select]   
        if choice.lower()=="q":
            print("You have exit the game :(")
            quit()
        elif (computer=="rock" and choice=="paper") or (computer=="paper" and choice=="sissors") or (computer=="sissors" and choice=="rock"):
            print("Computers pick: "+computer)
            print("You won!!")
            i +=1
        else:
            print("Computers pick: "+computer)
            print("You lost!")
            j+=1
    if j==3:
        print("The computer won the game")
    else:
        print("You won the game")

rockpaper()
            
            
        