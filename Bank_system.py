import json
class Bank():
    def __init__(self):
        pass
        
    def create_account(self, full_name, CNIC, phone_no, PIN, init_bal, acc_no):
        detail = {
            "Full Name" : full_name,
            "CNIC" : CNIC,
            "Phone No" : phone_no,
            "PIN" : PIN,
            "Balance" : init_bal
        }

        acc = {
            "Account No" : acc_no,
            "Details" : detail
        }

        try:
            with open("User.json", "r") as f:
                history = json.load(f)

        except FileNotFoundError:
            history = []

        history.append(acc)    
        with open("User.json", "w") as f:
            json.dump(history, f, indent=4)

    def login(self, acc_no, PIN):
        try:
            with open("User.json" , "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            data = []
        print("Account not found.")
        found = False
        for acc in data:
            if acc["Account No"] == acc_no and acc["Details"]["PIN"] == PIN :
                found = True
                print("Login Successfully.")
                while True:
                    choice = input("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transfer Money\n5. Transaction\n6. Change PIN\n7. Logout\nEnter choice :")
                    acc1 = Dashboard()
                    if choice == "1":
                        acc1.show_balance(acc)

                    elif choice == "2":
                        while True:
                            amount = input("Enter Amount :")
                            try:
                                amount = int(amount)
                                if amount > 0:
                                    break
                                else:
                                    print("Invalid Amount.")
                            except ValueError:
                                print("Invalid Amount.")

                        acc1.deposit(acc, amount, data)
                
                
            
        if not found:
            print("Invalid PIN.\nPlease enter again.")
            
class Dashboard():
    def __init__(self):
        pass

    def show_balance(self, acc):
        print(f"Balance : {acc["Details"]["Balance"]}")
                
    def deposit(self, acc, amount, data):
        balance = acc["Details"]["Balance"]
        balance += amount
        acc["Details"]["Balance"] = balance
        with open("User.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"RS. {amount} was deposited successfully.")
        print(f"Your current balance is {balance}.")

acc_no = 1001
while True:
    print("=" * 20)
    print("   BANK MANAGEMENT   ")
    print("=" * 20)
    choice = input("\n1. Create Account\n2. Login\n3. Exit\nChoose option : ")

    if  choice == "1" :
        acc1 = Bank()
        full_name = input("Enter full name :")
        while True:
            CNIC = input("Enter CNIC :")
            try:
                with open("User.json", "r") as f:
                    data = json.load(f)

            except FileNotFoundError:
                data = []

            duplicate = False

            for acc in data:

                if acc["Details"]["CNIC"] == CNIC :
                    print("CNIC is already exist.")
                    duplicate = True

            if not duplicate:
                break                  
        phone_no = input("Enter phone no :")
        while True:
            PIN = input("Enter PIN :")
            if PIN.isnumeric() and len(PIN) == 4 :
                break
            else:
                print("Invalid PIN.\nPlease enter again.")

        while True:
            init_bal = input("Enter init_bal :")
            try:
                init_bal = int(init_bal)
                if init_bal >= 0 :
                    break
                else:
                    print("Invalid balance.\nPlease enter again.")
            except ValueError:
                print("Invalid balance.\nPlease enter again.")

            
            
            
        
        acc1.create_account(full_name, CNIC, phone_no, PIN, init_bal, acc_no)
        acc_no += 1


    elif choice == "2" :
        acc1 = Bank()
        acc_no = input("Enter Account no :")
        try:
            acc_no = int(acc_no)
            

        except ValueError:
            continue
            
        PIN = input("Enter PIN :")
        acc1.login(acc_no, PIN)

    elif choice == "3" :
        print("Exit!")
        break

    else:
        print("Invalid choice.\nPlease enter again.")
    