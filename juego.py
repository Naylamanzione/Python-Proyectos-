
print ("Welcome to my game!")
print ("You win the game by answering correctly 5/5 questions, Let's begin!")


def game ():
    i:int = 0
    playing:str=input("Do you want to play? ")
    if playing.lower() != "yes":
        print("You have exit the game :(")
    else:
        print("Okay,let's begin!")
        Question1:str=input("What continent is Argentina on? ")
        if Question1.lower() == "america" or  Question1.lower() == "south america":
            print ("Correct!")
            i +=1
        else:
            print ("Incorrect")
        Question2:str = input("What language is spoken in Argentina? ")
        if Question2.lower() != "español":
            print ("Incorrect")
        else:
            print ("Correct!")
            i+=1
        Question3:str=input("What's Argentinas most popular sport? ")
        if Question3.lower() != "soccer":
             print ("Incorrect")
        else:
            print ("Correct!")
            i+=1
        Question4:str=input("What's Argentinas most traditional beverage? ")
        if Question4.lower() == "mate" or Question4.lower() == "fernet":
            print ("Correct!")
            i+=1
        else:
            print ("Incorrect")
        print("Last Question! ")
        Question5:str=input("Who's one of the most famous argentinian soccer players? ") 
        if Question5.lower()=="messi" or Question5.lower()=="maradona":
            print ("Correct!")
            i+=1
        else:
            print ("Incorrect")
        if i==5:
            print("You win! \nYou got 5/5 questions")
        else:
            print("You lost \nYou got " + str(i)+"/5 questions")
    
            
             
game()
            
            
            