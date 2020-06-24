import random
print("*****WORD GUESSING GAME*****")

name = input("Enter your name: ")
print("Welcome, ", name)
level = input("Choose a level [1/2/3]: ")

#This is the level one of the game is you choose this level to play
def level_one():
    #The list of words that are to be guessed
    words = ["arts"," auto", "away", "baby", "back", "bags", "ball", "band"]
    
    word = random.choice(words)
    print("Guess the Word!")
    guesses = ""
    turns = 5
    
    while turns > 0:
        failed = 0
        for i in word:
            if i in guesses:
                print(i)
                
            else:
                print("*")
                failed += 1
                
        if failed == 0:
            print("Congradulations! You won!")
            print("The word is ", word)
            
            cont = input("Do you want to continue?<yes/no> ")
            if cont.lower() == "yes":
                level_two()
            else:
                break
            break
            
        guess_word = input("Enter a character: ")
        guesses += guess_word
        
        if guess_word not in word:
            turns -= 1
            print("Wrong! Try again!")
            print("You have ", + turns ," left" )
        
            if turns == 0:
                print("You Lose!")
                print("The word is ", word)
                
                
#This is the level two of the game is you choose this level to play
def level_two():
    words = ["heaven","banana", "monday", "silver", "orange", "thirty", "fourty", "future"]
    
    word = random.choice(words)
    print("Guess the Word!")
    guesses = ""
    turns = 10
    
    while turns > 0:
        failed = 0
        for i in word:
            if i in guesses:
                print(i)
                
            else:
                print("*")
                failed += 1
                
        if failed == 0:
            print("Congradulations! You won!")
            print("The word is ", word)
            cont = input("Do you want to continue?<yes/no> ")
            if cont.lower() == "yes":
                level_three()
            else:
                break
            break
            
        guess_word = input("Enter a character: ")
        guesses += guess_word
        
        if guess_word not in word:
            turns -= 1
            print("Wrong! Try again!")
            print("You have ", + turns ," left" )
        
            if turns == 0:
                print("You Lose!")
                print("The word is ", word)
                
                
        
#This is the level two of the game is you choose this level to play
def level_three():
    words = ["thursday","princess", "monday", "thousand", "", "children", "birthday", "virginia"]
    
    word = random.choice(words)
    print("Guess the Word!")
    guesses = ""
    turns = 12
    
    while turns > 0:
        failed = 0
        for i in word:
            if i in guesses:
                print(i)
                
            else:
                print("*")
                failed += 1
                
        if failed == 0:
            print("Congradulations! You won!")
            print("The word is ", word)
            break
            
        guess_word = input("Enter a character: ")
        guesses += guess_word
        
        if guess_word not in word:
            turns -= 1
            print("Wrong! Try again!")
            print("You have ", + turns ," left" )
        
            if turns == 0:
                print("You Lose!")
                print("The word is ", word)
 
#The line of codes to be executed before the function on the basis of your input    
if level == "1":
    #if you choose level one,
    level_one()
    
if level == "2":
    #if you choose level two,
    level_two()
    
if level == "3":
    #if you choose level three,
    level_three()

