def load_accounts():
    accounts = {}
    try:
        with open("bank.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    accounts[int(parts[0])] = {"name": parts[1], "balance": float(parts[2])}
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts):
    with open("bank.txt", "w") as f:
        for acc_no, data in accounts.items():
            f.write(f"{acc_no},{data['name']},{data['balance']}\n")

def create_account():
    name = input("Enter Name: ")
    deposit = float(input("Enter Opening deposit: "))

    accounts = load_accounts()

    if deposit < 500:
        print("Minimum Rs.500 required")
        return

    if len(accounts) == 0:
        acc_no = 1001
    else:
        acc_no = max(accounts.keys()) + 1

    accounts[acc_no] = {"name": name, "balance": deposit}
    save_accounts(accounts)
    print(f"Account created. A/C No: {acc_no} | Balance: {deposit}
    
print("1. Create Account")
choice = input("Enter your choice: ")

if choice == "1":
    create_account()
    def load_accounts():
    accounts = {}
    try:
        with open("bank.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    accounts[int(parts[0])] = {"name": parts[1], "balance": float(parts[2])}
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts):
    with open("bank.txt", "w") as f:
        for acc_no, data in accounts.items():
            f.write(f"{acc_no},{data['name']},{data['balance']}\n")

accounts = load_accounts()
accounts[1001] = {"name": "Anil", "balance": 2000}
save_accounts(accounts)

acc_no = int(input("Enter A/C No: "))  # 1001
amount = float(input("Enter Withdraw Amount: "))  # 1500

accounts = load_accounts()
if accounts[acc_no]["balance"] - amount >= 500:
    accounts[acc_no]["balance"] -= amount
    save_accounts(accounts)
    print(f"Withdrawal successful. Balance: {accounts[acc_no]['balance']}")
else:
    print("Minimum Rs.500 balance required. Withdrawal cancelled.")
    accounts = {1001: {"name": "Anil", "balance": 2000}}

from_acc = int(input("Enter From A/C No: "))  # 1001
to_acc = int(input("Enter To A/C No: "))  # 9999
amount = float(input("Enter Transfer Amount: "))  # 100

if to_acc not in accounts:
    print(f"Account {to_acc} not found. Transfer cancelled.")
elif accounts[from_acc]["balance"] - amount < 500:
    print("Minimum Rs.500 balance required. Transfer cancelled.")
else:
    accounts[from_acc]["balance"] -= amount
    accounts[to_acc]["balance"] += amount
    print("Transfer successful.")
    accounts = {1001: {"name": "Anil", "balance": 2000},
            1002: {"name": "Ravi", "balance": 3000}}

from_acc = int(input("Enter From A/C No: "))  # 1002
to_acc = int(input("Enter To A/C No: "))  # 1001
amount = float(input("Enter Transfer Amount: "))  # 1000

if to_acc not in accounts:
    print(f"Account {to_acc} not found. Transfer cancelled.")
elif accounts[from_acc]["balance"] - amount < 500:
    print("Minimum Rs.500 balance required. Transfer cancelled.")
else:
    accounts[from_acc]["balance"] -= amount
    accounts[to_acc]["balance"] += amount
    print(f"Transfer successful.")
    print(f"{from_acc} balance: {accounts[from_acc]['balance']}
