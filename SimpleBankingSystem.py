account = {}

def create_account():
    name = input("Enter name: ")
    balance = int(input("Enter initial balance: "))
    account["name"] = name
    account["balance"] = balance
    print("Account created!")

def check_balance():
    if account:
        print(f"{account['name']}'s balance: {account['balance']}")
    else:
        print("No account found. Create account first.")

def deposit():
    if account:
        amt = int(input("Enter amount to deposit: "))
        account["balance"] += amt
        print("Deposit successful!")
    else:
        print("Create account first.")

def withdraw():
    if account:
        amt = int(input("Enter amount to withdraw: "))
        if account["balance"] >= amt:
            account["balance"] -= amt
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Create account first.")

# Main Menu
print("Welcome to MyBank!")

while True:
    print("\n1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        check_balance()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        print("Thank you for using MyBank!")
        break
    else:
        print("Invalid option!")