import json
from datetime import date
from datetime import datetime
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
                    print("=" * 20)
                    print("     DASHBOARD     ")
                    print("=" * 20)
                    choice = input("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transaction\n5. Change PIN\n6. Logout\nEnter choice :")
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
                        
                        try:
                            history = acc["Details"]["Transaction"]

                        except:
                            history = []

                        acc1.deposit(acc, amount, data, history)
                
                    elif choice == "3":
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
                        
                        try:
                            history = acc["Details"]["Transaction"]

                        except:
                            history = []
                        acc1.withdraw(acc, amount, data, history)

                    elif choice == "4" :
                        acc1.transaction_history(acc)

                    elif choice == "5":
                        while True:
                            new_pin = input("Enter PIN :")
                            if new_pin.isnumeric() and len(new_pin) == 4 :
                                break
                            else:
                                print("Invalid PIN.\nPlease enter again.")
                        acc1.change_pin(acc,data,new_pin)
                 

        if not found:
            print("Invalid PIN.\nPlease enter again.")
            
class Dashboard():
    def __init__(self):
        pass

    def show_balance(self, acc):
        print(f"Balance : {acc["Details"]["Balance"]}")
                
    def deposit(self, acc, amount, data , history):
        balance = acc["Details"]["Balance"]
        balance += amount
        acc["Details"]["Balance"] = balance
        time = datetime.now().time()

        time = time.strftime("%H:%M:%S")
        today_date = date.today()
        today_date = today_date.strftime("%d-%m-%Y")
        transaction = {
            "Time" : time,
            "Date" : today_date,
            "Type" : "Deposit",
            "Amount" : amount
        }
        history.append(transaction)
        acc["Details"].update({"Transaction" : history})
        with open("User.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"RS. {amount} was deposited successfully.")
        print(f"Your current balance is {balance}.")

    def withdraw(self, acc, amount, data, history):
        balance = acc["Details"]["Balance"]
        balance -= amount
        acc["Details"]["Balance"] = balance
        time = datetime.now().time()

        time = time.strftime("%H:%M:%S")
        today_date = date.today()
        today_date = today_date.strftime("%d-%m-%Y")
        transaction = {
            "Time" : time,
            "Date" : today_date,
            "Type" : "Withdraw",
            "Amount" : amount
        }
        history.append(transaction)
        acc["Details"].update({"Transaction" : history})
        with open("User.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"RS. {amount} withdraw successfully.")
        print(f"Your current balance is {balance}.")

    def transaction_history(self, acc):
        print("="*85)
        print(f"{'Date':<20}{'|':<5}{'Time':<20}{'|':<5}{'Type':<15}{'|':<5}{'Amount':<15}")
        print("="*85)
        for history in acc["Details"]["Transaction"] :
            print(f"{history['Date']:<20}{'|':<5}{history['Time']:<20}{'|':<5}{history['Type']:<15}{'|':<5}{history['Amount']:<15}")

        print("="*85)

    def change_pin(self, acc, data, new_pin):
        acc["Details"]["PIN"] = new_pin
        with open("User.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Your PIN is changed successfully.")

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
        print("*****| Account created successfully. |*****")
        print(f"Your account number is {acc_no}.")
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
    