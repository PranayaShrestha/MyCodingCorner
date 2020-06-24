print("Welcome to Shrestha Finance")
print("***LETS GET STARTED***")

name = input("Enter your name: ")
print("Welcome, ",name)

print("What would you like to perform?")
choice = input("Taxation or Compound intrest? <T/I> ")

def intrest():
    try:
        sec_choice = input("Simple Intrest or Compound Intrest?<S/C> ")
        #calculates the simple intrest if user chooses "s"
        if sec_choice.lower() == "s":
            def simple_intrest():
                try:
                    print("SIMPLE INTREST CALCULATION")
                    principal = int(input("Enter to principal amount: "))
                    time = int(input("Enter the time period: "))
                    rate = int(input("Enter the suitable rate: "))
                    intr = (principal * rate * time) / 100
                    print("The required intrest is ", intr)
                    summ = int(intr + principal)
                    
                    #To add bonus amount if time is above 5 years
                    if time >= 5:
                        bonus_sum = int((105/100) * summ)
                        print("The sum amount to", bonus_sum , " in ", time, " at the rate of ", rate,"% plus bonus rate of 5%")
                    else:
                        print("The sum amount to", summ , " in ", time, " at the rate of ", rate,"%")
                        
                except ValueError:
                    print("Sorry invalid input!")
                    
                    
            simple_intrest()
                
        #To calculate the compound intrest if the user chooses "c"
        if sec_choice.lower() == "c":
            def compound_intrest():
                type_intrest = input("Annual compound intrest or Semi-annual compound intrest?<A/S> ")
                #for compounding annual compound intrest
                if type_intrest.lower() == "a": 
                    def annual_compound_intrest():
                        try:
                            principal = float(input("Enter to principal amount: "))
                            time = float(input("Enter the time period: "))
                            rate = float(input("Enter the suitable rate: "))
                            intr = principal * ((1 + (rate / 100)) ** time - 1) 
                            print("The required intrest is ", intr)
                            summ = int(intr + principal)
                                
                            if time >= 5:
                                bonus_sum = int((105/100) * summ)
                                print("The sum amount to", bonus_sum , " in ", time, " at the rate of ", rate,"% plus bonus rate of 5%")
                            else:
                                print("The sum amount to", summ, " in ", time, " at the rate of ", rate,"%")
                        except ValueError:
                            print("Sorry invalid input!")
                    
                    
                    annual_compound_intrest()
                
                #for compounding semi annual compound intrest            
                if type_intrest.lower() == "s":
                    def semi_compound_intrest():
                        try:
                            principal = float(input("Enter to principal amount: "))
                            time = float(input("Enter the time period: "))
                            rate = float(input("Enter the suitable rate: "))
                            intr = principal * ((1 + (rate / 200)) ** (time*2) - 1) 
                            print("The required intrest is ", intr)
                            summ = int(intr + principal)
                            print("The sum amount to", summ, " in ", time, " at the rate of ", rate,"% plus bonus rate of 5%")    
                        
                        except ValueError:
                            print("Sorry invalid input!")
                    
                    
                    semi_compound_intrest()
                    
            compound_intrest()
    except ValueError:
        print("Sorry invalid input!")

            
intrest()
