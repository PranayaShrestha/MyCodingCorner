import sys


print("***SAMURAI ADVENTURE***")

#Introduction
name = input("Hello there traveller! Who might you be ?")
print("Dojo Master: Welcome, " + name + ".")
print("You must be the samurai who came for the mission,")
print("But I must warn you that the mission you have signed for is very dangerous")


cont = input("Do you want to continue?<Y/N> ")
if cont.lower() == "y":
    pass
else:
    sys.exit()

#items    
skill = 0
print("Your current skill: ", skill)
knife = ["inchanted knife, khukuri, table knife"]
swords = ["cursed sword, banjai blade, jabimaru VI, normal blade"]

#moves
moves = ["front slash, showdow blade, dark thunder, triple kill storm", "lighting slash","shogun strike"]

#the training quest
training = True

while training:
    print("Dojo Master: The mission that you have signed for is to defeat Danjo,")
    print("the evil rouge monk whose soul have been corrupted by the devil himself.")
    print("He is very powerful samurai.Thus to defeat him, You must train")
    
    #the training part
    train = input("Do you like to train?<Y/N> ")
    if train.lower() == "y":
        print("For the sake of training you will use a normal blade.")
        print("Your duel partner is Linda, the bar maid.")
        print("Your moves: front slash,shadow blade,lighting slash.")
        print("Now then lets start.")
        
        while skill <= 50:
            m = input("Enter your move: ")
            move = m.lower()
            if move == "front slash":
                print("Nice try! But its not enough to hurt the monk.")
                skill += 8
            elif move == "shadow blade":
                print("Hmm, I see that you are a talented samurai.")
                skill += 20
            elif move == "lighting slash":
                print("Thats some next level move indeed!")
                skill += 25
            else:
                print("Sorry, that move is not allowed.")
            
            training = False
            
    else:
        print("Sorry my friend, without training you cannot face the demonic monk.")
        training = False
        sys.exit()

print("Your current skill: ", skill)

#the first mission after the training
main_quest = True

while main_quest:
    print("""
          Dojo Master:Since you have completed you training, the time for the first mission has come.
          The monk lives in the middle of the dense Kenzui forest filled with wild bears,
          you have to defeat them in oder to reach the monk.""")
    
    #buying weapons for the battle
    def getting_ready():
        print("""Dojo Master: Very Well. In oder to fight the bears you must be
              well prepared. Thus you must buy some items needed for the battle.""")
        
        gold = 500
        print("Your gold: ", gold)
        weapon = input("Choose a weapon:(swords/knifes)")
        
        if weapon.lower() == "swords" or "sword":
            print("The sword collection:", swords)
            c3 = input("Choose on sword: ")
            cont3 = c3.lower()
            
            if cont3 == "cursed sword":
                print("Cost: 250")
                gold -= 250
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                
            elif cont3 == "banjai blade":
                print("Cost: 230")
                gold -= 230
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                
            elif cont3 == "jabimaru vi":
                print("Cost: 200")
                gold -= 200
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                
            elif cont3 == "normal blade":
                print("Cost: 150")
                gold -= 150
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                
            else:
                print("Sorry, that weapon is not available for you.")
                
        elif weapon == "knifes" or "knife":
            print("The knife collection:", knife)
            c3 = input("Choose on knife: ")
            cont3 = c3.lower()
            
            if cont3 == "inchanted knife":
                print("Cost: 125")
                gold -= 125
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                
            elif cont3 == "khukuri":
                print("Cost: 115")
                gold -= 115
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                
            elif cont3 == "table knife":
                print("Cost: 100")
                gold -= 100
                print("Remaining gold: ", gold)
                
                print("moves:\n ", moves)
                 
            else:
                print("Sorry, that weapon is not available for you.")
               
    def mission():
        direction = ["left","right","forward"]
        print("""Dojo Master: Now that you have chose the weapon of your like,
              we must procced into the forest.""")
              
        ready = input("Are you ready?<Y/N>")
        if ready.lower() == "y":
            print(direction)
            direction1 = input("We have entered the forest, which direction shall we head?\n")
            
            damage = 0
            if direction1 in direction:
                print("There are 2 hungry bears in front of you!")
                print(moves)
                while damage <= 75:
                    action = input("enter your move:\n")
                    
                    
                    if action.lower() == "front slash":
                        print("Nice one! It surely hurt the bears but it wont be enough")
                        damage += 20
                    elif action.lower() == "shadow blade":
                        print("Powerful move indeed! We can see the damage!")
                        damage += 25
                    elif action.lower() == "dark thunder":
                        print("That surely stuned them, hit them harder.")
                        damage += 30
                    elif action.lower() == "triple kill storm":
                        print("You must be some kind of genius!")
                        damage += 35
                    elif action.lower() == "lighting slash ":
                        print("Powerful move indeed! It must have got him>")
                        damage += 40
                    elif action.lower() == "shogun strike":
                        print("Powerful move indeed! Give a finishing blow!")
                        damage += 50
                    else:
                        print("That wont work.")
                    
                    if damage > 75:
                        def final_mission():
                            print("Dojo Master:You have defeated all the bears now, lets move foward, shall we?")
                            forward = input("Do yo want to continue?<Y/N> ")
                            if forward.lower() == "y":
                                print("""Dojo Master:Ohh! Can you see that?!
                                      That monastry is where he lives we should go there. Lets go!""")
                                print("""Danjo:I see that you two moron were able to come this far.
                                      But I can see you lifespan through my eyes and its not that long.
                                      Matter of fact, it ends right here...""")
                                print("""Dojo Master:Kid, don't listen to him.
                                      You have to defeat him for the future of mankind.
                                      """)
                                
                                moves = ["front slash, showdow blade, dark thunder, triple kill storm", "lighting slash","shogun strike"]
                                battle = input("Are you ready?<Y/N> ")
                                if battle.lower() == "y":
                                    boss_damage = 0
                                    health = 100
                                    print("Your health: ",health)
                                    print(moves)
                                    while boss_damage <= 500:
                                        action2 = input("enter your move:\n")
                                        
                                        if action2.lower() == "front slash":
                                            print("Nice one! It surely hurt Danjo but it wont be enough."
                                                  "but you're bleeding a lot!")
                                            boss_damage += 20
                                            health -= 30
                                            print("Your Health: ", health)
                                        elif action2.lower() == "shadow blade":
                                            print("Powerful move indeed! We can see the damage!"
                                                  "But you are damaged too!")
                                            boss_damage += 25
                                            health -= 20
                                            print("Your Health: ", health)
                                        elif action2.lower() == "dark thunder":
                                            print("That surely stuned him, hit him harder."
                                                  "Avoid shots from him!")
                                            boss_damage += 30
                                            health -= 15
                                            print("Your Health: ", health)
                                        elif action2.lower() == "triple kill storm":
                                            print("You must be some kind of genius!"
                                                  "You might have a chance!")
                                            boss_damage += 35
                                            health -= 10
                                            print("Your Health: ", health)
                                        elif action2.lower() == "lighting slash ":
                                            print("Powerful move indeed! It must have got him")
                                            boss_damage += 40
                                            health -= 5
                                            print("Your Health: ", health)
                                        elif action2.lower() == "shogun strike":
                                            print("Powerful move indeed! He is getting hurt!")
                                            boss_damage += 50
                                            health -= 2
                                            print("Your Health: ", health)
                                        else:
                                            print("That wont work.")
                                        
                                        if boss_damage > 200:
                                            print("You have defeated danjo and completed you quest"
                                                  "You are a fine samurai. Hoping to see you soon kid!")
                                            print("reward: "
                                                  "gold: 5000"
                                                  "skill: 1200")
                                        else:
                                            pass
                                        
                                        if health == 0:
                                            print("You died!")
                                            sys.exit()
                                        else:
                                            pass
                                        
                                        
                                else:
                                   sys.exit()
                            else:
                                print("Dojo Master: Never thought you would chicken out at this stage...")
                                sys.exit()
                        
                        final_mission()
                    else:
                        pass
            
            else:
                print("You cannot go there")
        else:
            sys.exit()
            
        

    cont2 = input("Do you like continue into the forest?<Y/N>")
    if cont2.lower() == "y":
        getting_ready()
        mission()
        
        main_quest = False
        sys.exit()

    else:
        print("Very Well, hope to see you soon soldier. ")
        sys.exit()
        


    
    
                
        


