print("=" * 50)
print("🏧 ADVANCED ATM MANAGEMENT SYSTEM 🏧")
print("=" * 50)

users = {}

while True:
    print("\nMAIN MENU")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter Username: ")

        if username in users:
            print("❌ User already exists!")
            continue

        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email: ")
        pin = input("Create 4 Digit PIN: ")

        users[username] = {
            "mobile": mobile,
            "email": email,
            "pin": pin,
            "balance": 1000,
            "history": []
        }

        print("✅ Registration Successful!")

    elif choice == "2":
        username = input("Username: ")
        pin = input("PIN: ")

        if username not in users:
            print("❌ User Not Found!")
            continue

        if users[username]["pin"] != pin:
            print("❌ Incorrect PIN!")
            continue

        print(f"\n✅ Welcome {username}")

        while True:
            print("\n" + "=" * 40)
            print("ATM MENU")
            print("=" * 40)
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Account Details")
            print("6. Logout")

            atm_choice = input("Select Option: ")

            if atm_choice == "1":
                print(f"💰 Current Balance: ${users[username]['balance']}")

            elif atm_choice == "2":
                amount = input("Enter Amount To Deposit: ")

                if amount.isdigit():
                    amount = int(amount)

                    if amount > 0:
                        users[username]["balance"] += amount
                        users[username]["history"].append(
                            f"Deposited ${amount}"
                        )

                        print("✅ Deposit Successful")
                        print(
                            f"New Balance: ${users[username]['balance']}"
                        )
                    else:
                        print("❌ Amount must be greater than 0")

                else:
                    print("❌ Invalid Amount")

            elif atm_choice == "3":
                amount = input("Enter Amount To Withdraw: ")

                if amount.isdigit():
                    amount = int(amount)

                    if amount <= 0:
                        print("❌ Amount must be greater than 0")

                    elif amount > users[username]["balance"]:
                        print("❌ Insufficient Balance")

                    else:
                        users[username]["balance"] -= amount

                        users[username]["history"].append(
                            f"Withdrawn ${amount}"
                        )

                        print("✅ Withdrawal Successful")
                        print(
                            f"Remaining Balance: ${users[username]['balance']}"
                        )

                else:
                    print("❌ Invalid Amount")

            elif atm_choice == "4":
                print("\n📜 TRANSACTION HISTORY")

                if len(users[username]["history"]) == 0:
                    print("No Transactions Found")

                else:
                    for transaction in users[username]["history"]:
                        print("•", transaction)

            elif atm_choice == "5":
                print("\n👤 ACCOUNT DETAILS")
                print("Username :", username)
                print("Email    :", users[username]["email"])
                print("Mobile   :", users[username]["mobile"])
                print("Balance  :", users[username]["balance"])

            elif atm_choice == "6":
                print("👋 Logged Out Successfully")
                break

            else:
                print("❌ Invalid Choice")

    elif choice == "3":
        print("🙏 Thank You For Using Our ATM")
        break

    else:
        print("❌ Invalid Choice")