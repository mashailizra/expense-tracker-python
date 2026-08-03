import csv
import os

expenses = []

if not os.path.exists("expenses.csv"):
    with open("expenses.csv","w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["date","category","amount","note"])
        
try:
    with open("expenses.csv","r",newline="")as file:
        reader=csv.DictReader(file)

        for row in reader:
            row["amount"]=float(row["amount"])
            expenses.append(row)
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

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "note": note
        }

        expenses.append(expense)

        with open("expenses.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([
                expense["date"],
                expense["category"],
                expense["amount"],
                expense["note"]
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
