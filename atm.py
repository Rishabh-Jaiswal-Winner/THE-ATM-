print("Welcome To The ATM")
balance = 1000
users = {}
current_user = None

while True:
    choice = input("1. Deposit\n2. Withdraw\n3. Register\n4. Exit\nChoose an Option: ") # Fixed \, to \n and prompt text
    if choice == "1" and current_user != None:
        deposit = input("Enter an Amount To Deposit: ")
        if deposit.isnumeric():
            deposit = int(deposit)
            if deposit > 0:
                balance += deposit
                print(f"Your New Balance Is {balance}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Please Enter A Valid Amount")
    elif choice == "2" and current_user != None: # Corrected this to be the withdraw option
        withdraw = input("Enter Amount To Withdraw: ")
        if withdraw.isnumeric():
            withdraw = int(withdraw)
            if balance >= withdraw and withdraw > 0:
                balance -= withdraw
                print(f"Your New Balance Is {balance}")
            else:
                print(f"Cannot Withdraw. Current balance: {balance}, requested: {withdraw}.")
        else:
            print("Please Enter A Valid Amount")
    elif choice == "3":
        mobile_number = input("Enter Your Mobile Number: ")
        name = input("Enter Your name: ")
        email = input("Enter Your email: ")

        d1 = {"email": email, "mobile_number": mobile_number}
        users[name] = d1
        print(name,"Has Been Registered To The Banks Id")
        current_user = users[name]
    elif choice == "4": # Corrected this to be the exit option
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3 or 4.")