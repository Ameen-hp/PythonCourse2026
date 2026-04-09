
secret_pin=2468
balance = 50000
my_pin = int(input("please enter your pin!"))
limit = 500000
if (my_pin == secret_pin):
    print("""       
                    welcome to the at machine
                    please choose the option
        ***********************************************
        *              1. check balance               *
        *              2. withdraw                    *
        *              3. deposite                    *
        *              4. transfer                    *
        *              5. exit                        *
        ***********************************************          


""")
    option = int(input("please enter the option"))
    if(option == 1):
        print("your current balance is ",balance)
    elif(option == 2):
        withdraw=int(input("how much do you want to withdraw?"))
        if(withdraw <= balance):
            print("your balance ",withdraw,"have been withdrawn")
            print("now  your current balance is ",(balance - withdraw))
        else:
            print("your current balance is less than your entered balance")
    elif(option == 3):
        print("do you want to deposite?")
        deposite = int(input("please enter your deposite"))
        if(deposite <= limit and deposite+balance <= limit ):
             print("your balance",deposite," successfully deposite");
             print("after deposting your current balance is ",(balance+deposite))

        else:
            print("your deposite is greater than your current balance")
    elif(option == 4):
        print("the service is currently unavailable") 
    elif(option == 5):
         print("you are exit");
                        
    else:
        print("you have enetered the wrong option! please try again")

    
else:
    print("your pin is incorrect!")    