print("Welcome to BB Bank, your satifaction is our business")

bbb_costumers = {"Rita":"craZe@56", "Reama":"u2sabi419", "Rose":"4q10Q", "Regina":"Eko4sho", "Rebecca":"Ee2bigO"}

username = input("What is your name?\n")

if username in bbb_costumers:
    print("Hello again " + username + ", enter your password please.")
    password = input()
    if password == bbb_costumers[username]:
        print("These are the options available") 
        print("a. Check your balance")
        print("b. Make a deposit")
        print("c. Make a withdrawal")
        print("d. Make a transfer")
             
        n = True
        while n == True:    
            select_option = input("Kindy select an option.")
            account_balance = "50275"
            if(select_option == "a"):
                print("You selected Option %s" % select_option)
                print("Your account balance is N50,275.00")

                another_transaction = ("y", "n")
                another_transaction = input("Do you want to perfom another transaction?")             
                if another_transaction == "n":
                    print("Thank you for using BB Bank. Have a wonderful day!")
                    n = False
                                                           
            elif(select_option == "b"):
                print("You selected Option %s" % select_option)
                deposit = input("How much do wish to deposit?\n")
                print("You have deposited N" + deposit + ".")
                another_transaction = ("y", "n")
                another_transaction = input("Do you want to perfom another transaction?")
                if another_transaction == "n":
                    print("Thank you for using BB Bank. Have a wonderful day!")
                    n = False

            elif(select_option == "c"):
                print("You selected Option %s" % select_option)
                withdrawal = input("How much do wish to withdraw?\n")
                print("You are about to withdraw N" + withdrawal + ".")

                if withdrawal > account_balance:
                    print("Sorry, you have insufficienct funds")
                    another_transaction = ("y", "n")
                    another_transaction = input("Do you want to perfom another transaction?")   
                    if another_transaction == "n":
                        print("Thank you for using BB Bank. Have a wonderful day!")
                        n = False
                
                if withdrawal < account_balance:
                    print("Please take your cash")
                    another_transaction = ("y", "n")
                    another_transaction = input("Do you want to perfom another transaction?")   
                    if another_transaction == "n":
                        print("Thank you for using BB Bank. Have a wonderful day!")
                        n = False
                    
            elif(select_option == "d"):
                print("You selected Option %s" % select_option)
                transfer = input("How much do wish to transfer\n")

                if transfer > account_balance:
                    print("Sorry, you have insufficienct funds")
                    another_transaction = ("y", "n")
                    another_transaction = input("Do you want to perfom another transaction?")   
                    if another_transaction == "n":
                        print("Thank you for using BB Bank. Have a wonderful day!")
                        n = False
                
                if transfer < account_balance:
                    print("You have transfered N" + transfer + ".")
                    another_transaction = ("y", "n")
                    another_transaction = input("Do you want to perfom another transaction?")   
                    if another_transaction == "n":
                        print("Thank you for using BB Bank. Have a wonderful day!")
                        n = False
    else:
        print("You have entered an incorrect password, please try again?")   
else:
    print ("You have entered a wrong name, please try again?")