import json
class Account():
    def __init__(self):
        pass
        
    def create_account(self, full_name, CNIC, phone_no, PIN, init_bal):
        detail = {
            "Full Name" : full_name,
            "CNIC" : CNIC,
            "Phone No" : phone_no,
            "PIN" : PIN,
            "Initial Balance" : init_bal
        }
        acc_no = 1
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

        acc_no += 1

while True:
    print("=" * 20)
    print("   BANK MANAGEMENT   ")
    print("=" * 20)
    choice = input("\n1. Create Account\n2. Login\n3. Exit\nChoose option : ")

    if  choice == "1" :

        c1 = Account()
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
            init_bal = int(init_bal)
            if init_bal >= 0 :
                break

            else:
                print("Invalid balance.\nPlease enter again.")

        c1.create_account(full_name, CNIC, phone_no, PIN, init_bal)

    