import csv
import os

class Expense:
    def __init__(self,date,category,amount,note):
        self.date= date
        self.category= category
        self.amount= amount
        self.note= note

    def __str__(self):
        return(
            f"Date:{self.date}\n"
            f"Category:{self.category}\n"
            f"Amount:{self.amount}\n"
            f"Note:{self.note}\n"
        )

class ExpenseTracker:
    def __init__(self):
        self.expenses=[]

    def add_expense(self,expense):
        self.expenses.append(expense)

    def list_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\nExpenses:")

        for expense in self.expenses:
            print(expense)
            print("-" * 30)


tracker = ExpenseTracker()

if not os.path.exists("expenses.csv"):
    with open("expenses.csv","w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["date","category","amount","note"])
        
try:
    with open("expenses.csv","r",newline="")as file:
        reader=csv.DictReader(file)

        for row in reader:
            expense = Expense(
                row["date"],
                row["category"],
                float(row["amount"]),
                row["note"]
            )

            tracker.add_expense(expense)
except (ValueError,KeyError):
    print("Warning:Some data in csv file could not be loaded.")
        
print("Personal Expense Tracker")

while True:
    print("\nMenu")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        note = input("Enter note: ")

        expense = Expense(
            date,
            category,
            amount,
            note
        )

        tracker.add_expense(expense)

        with open("expenses.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([
                expense.date,
                expense.category,
                expense.amount,
                expense.note
            ])

        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\nExpenses:")

            for element in expenses:
                print(f"Date: {element['date']}")
                print(f"Category: {element['category']}")
                print(f"Amount: {element['amount']}")
                print(f"Note: {element['note']}")
                print("-" * 30)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


tracker = ExpenseTracker()

tracker.add_expense(
    Expense(
        "2026-08-05",
        "Food",
        250,
        "Lunch"
    )
)

tracker.add_expense(
    Expense(
        "2026-08-05",
        "Travel",
        100,
        "Bus Fare"
    )
)

tracker.list_expenses()
