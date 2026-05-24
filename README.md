# Bank Management System

A simple Bank Management System built with Python using OOP concepts and JSON file handling.

This project allows users to create bank accounts, login securely using PIN authentication, deposit and withdraw money, view transaction history, and manage account details.

---

# Features

- Create Bank Account
- Login System
- PIN Authentication
- Check Balance
- Deposit Money
- Withdraw Money
- Transaction History
- Change PIN
- Logout System
- JSON File Storage
- Input Validation

---

# Technologies Used

- Python
- OOP (Object-Oriented Programming)
- JSON
- File Handling
- Datetime Module

---

# Project Structure

```text
Bank_System/
│
├── Bank_system.py
├── User.json
└── README.md
```

---

# Main Menu

```text
1. Create Account
2. Login
3. Exit
```

---

# Dashboard Menu

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Change PIN
6. Logout
```

---

# How It Works

## Create Account

Users can create a bank account by entering:

- Full Name
- CNIC
- Phone Number
- 4-Digit PIN
- Initial Balance

Each account receives an account number.

---

## Login System

Users login using:

- Account Number
- PIN

After successful authentication, the dashboard menu opens.

---

# Banking Operations

## Check Balance
Displays the current account balance.

---

## Deposit Money
Users can add money to their account.

---

## Withdraw Money
Users can withdraw money if sufficient balance is available.

---

## Transaction History
Stores and displays:

- Transaction Type
- Date
- Time
- Amount

Example:

```text
Date                Time                Type           Amount
----------------------------------------------------------------
24-05-2026          10:15:30            Deposit        5000
24-05-2026          11:20:10            Withdraw       2000
```

---

## Change PIN
Users can update their account PIN.

---

# Data Storage

All account information is stored in a JSON file.

Example:

```json
[
    {
        "Account No": 1001,
        "Details": {
            "Full Name": "Ali",
            "CNIC": "1234567890123",
            "Phone No": "03001234567",
            "PIN": "1234",
            "Balance": 5000
        }
    }
]
```

---

# Concepts Practiced

This project helps practice:

- Classes and Objects
- JSON Handling
- File Handling
- Authentication Logic
- Input Validation
- Nested Dictionaries
- Menu-Driven Programs

---

# Future Improvements

- Transfer Money Feature
- PIN Encryption
- Account Lock System
- Admin Panel
- SQLite Database
- GUI Version

---

# How To Run

```bash
python Bank_system.py
```

---

# Requirements

- Python 3.x

No external libraries required.

---

# Author

Wajid Ali