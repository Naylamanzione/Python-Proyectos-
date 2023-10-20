
import random

print("Welcome to Guess the number!")
print("A number between 1 and 10 will be randomly asigned, try to guess it in the least amount of tries")

def  guessnumber():
    guess:int=0
    number:int=random.randint(1,10)
    i:int = 0
    playing:str=input("Do you want to play? ")
    if playing.lower() != "yes":
        print("You have exit the game :(")
    else:
        print("Okay,let's begin!")
        while guess!=number:
            guess:int=int(input("Make your guess: "))
            if guess>number:
                print("You were above the number")
                i +=1
            else:
                print("You were below the number")
                i +=1
        print("You guessed the number!!")
        if i==0:
            print("It took you "+str(i)+1+" try")
        else:
            print("It took you "+str(i)+" tries")

guessnumber()