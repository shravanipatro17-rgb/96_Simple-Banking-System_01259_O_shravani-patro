import os

# Minimum balance
MIN_BALANCE = 500

# File name
FILE_NAME = "bank.txt"

# Dictionary to store account details
accounts = {}


# Load accounts from file
def load_accounts():
    global accounts

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 3:
                    acc_no = int(data[0])
                    name = data[1]
                    balance = float(data[2])

                    accounts[acc_no] = {
                        "name": name,
                        "balance": balance
                    }


# Save accounts to file
def save_accounts():
    with open(FILE_NAME, "w") as file:
        for acc_no, details in accounts.items():
            file.write(
                f"{acc_no}|{details['name']}|{details['balance']}\n"
            )


# Generate unique account number
def generate_account_number():
    if not accounts:
        return 1001

    return max(accounts.keys()) + 1


# Create new account
def create_account():
    name = input("Enter customer name: ").strip()

    if not name:
        print("Invalid name!")
        return

    try:
        deposit = float(input("Enter opening deposit: "))

        if deposit < MIN_BALANCE:
            print("Minimum opening balance must be Rs.500.")
            return

        if deposit <= 0:
            print("Invalid deposit amount.")
            return

        acc_no = generate_account_number()

        accounts[acc_no] = {
            "name": name,
            "balance": deposit
        }

        save_accounts()

        print("Account created successfully!")
        print("A/C No:", acc_no)
        print("Balance:", accounts[acc_no]["balance"])

    except ValueError:
        print("Invalid input! Enter a valid amount.")


# Deposit money
def deposit_money():
    try:
        acc_no = int(input("Enter account number: "))

        if acc_no not in accounts:
            print("Account not found.")
            return

        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid deposit amount.")
            return

        accounts[acc_no]["balance"] += amount

        save_accounts()

        print("Deposit successful.")
        print("New Balance:", accounts[acc_no]["balance"])

    except ValueError:
        print("Invalid input!")


# Withdraw money
def withdraw_money():
    try:
        acc_no = int(input("Enter account number: "))

        if acc_no not in accounts:
            print("Account not found.")
            return

        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        balance = accounts[acc_no]["balance"]

        if balance - amount < MIN_BALANCE:
            print("Insufficient balance!")
            print("Minimum balance of Rs.500 must remain.")
            return

        accounts[acc_no]["balance"] -= amount

        save_accounts()

        print("Withdrawal successful.")
        print("Balance:", accounts[acc_no]["balance"])

    except ValueError:
        print("Invalid input!")


# Transfer money
def transfer_money():
    try:
        sender = int(input("Enter sender account number: "))
        receiver = int(input("Enter receiver account number: "))

        if sender not in accounts:
            print("Sender account not found. Transfer cancelled.")
            return

        if receiver not in accounts:
            print(f"Account {receiver} not found. Transfer cancelled.")
            return

        if sender == receiver:
            print("Cannot transfer to the same account.")
            return

        amount = float(input("Enter transfer amount: "))

        if amount <= 0:
            print("Invalid transfer amount.")
            return

        sender_balance = accounts[sender]["balance"]

        if sender_balance - amount < MIN_BALANCE:
            print("Insufficient balance! Transfer cancelled.")
            return

        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        save_accounts()

        print("Transfer successful.")
        print(sender, "balance:", accounts[sender]["balance"])
        print(receiver, "balance:", accounts[receiver]["balance"])

    except ValueError:
        print("Invalid input!")


# Balance enquiry
def balance_enquiry():
    try:
        acc_no = int(input("Enter account number: "))

        if acc_no not in accounts:
            print("Account not found.")
            return

        print("\nAccount Details")
        print("Account Number:", acc_no)
        print("Account Holder:", accounts[acc_no]["name"])
        print("Available Balance:", accounts[acc_no]["balance"])

    except ValueError:
        print("Invalid account number!")


# Main menu
def main():

    load_accounts()

    while True:

        print("\n================================")
        print("       SIMPLE BANKING SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Balance Enquiry")
        print("6. Exit")
        print("================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_account()

            elif choice == 2:
                deposit_money()

            elif choice == 3:
                withdraw_money()

            elif choice == 4:
                transfer_money()

            elif choice == 5:
                balance_enquiry()

            elif choice == 6:
                print("Thank you for using Simple Banking System!")
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

        except ValueError:
            print("Please enter a valid menu choice.")


# Program execution
if __name__ == "__main__":
    main()
