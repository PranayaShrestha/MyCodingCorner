import random

print("***** ROCK PAPERS SCISSORS*****")

#introduction
name = input("Enter your name: ")
print("Hello there!", name)
print("Lets Play!")

main = True
while main == True:        
    options = ["rock", "paper", "scissors"]
    option = random.choice(options)
    
    user_option = input("Enter you choice: ")
    user_choice = user_option.lower()
    
    if user_choice == option:
        print("Its a tie!")
        leave = (input("Do you want to quit?<yes/no>"))
        if leave.lower() == "yes":
            main = False
        else:
            continue
        
    elif user_choice == "rock":
        if option == "paper":
            print("You lose 'cause paper covers rock!")
            leave = (input("Do you want to quit?<yes/no>"))
            if leave.lower() == "yes":
                main = False
            else:
                continue
        
        else:
            print("You win 'cause rock smashes scissors!")
            leave = (input("Do you want to quit?<yes/no>"))
            if leave.lower() == "yes":
                main = False
            else:
                continue
            
    elif user_choice == "paper":
        if option == "rock":
            print("You win 'cause paper covers rock!")
            leave = (input("Do you want to quit?<yes/no>"))
            if leave.lower() == "yes":
                main = False
            else:
                continue
            
        else:
            print("You lose 'cause scissors cuts paper!")
            leave = (input("Do you want to quit?<yes/no>"))
            if leave.lower() == "yes":
                main = False
            else:
                continue
            
    elif user_choice == "scissors":
        if option == "rock":
            print("You lose 'cause rock smashes scissors!")
            leave = (input("Do you want to quit?<yes/no>"))
            if leave.lower() == "yes":
                main = False
            else:
                continue
            
        else:
            print("You win 'cause scissors cuts paper!")
            leave = (input("Do you want to quit?<yes/no>"))
            if leave.lower() == "yes":
                main = False
            else:
                continue
            
    else:
        print("You chose an invalid option!")
        leave = (input("Do you want to quit?<yes/no>"))
        if leave.lower() == "yes":
            main = False
        else:
            continue
        break