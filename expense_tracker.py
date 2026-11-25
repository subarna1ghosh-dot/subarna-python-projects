# -----------------------------------
# Personal Expense Tracker (CLI App)
# Created by: Subarna Ghosh
# -----------------------------------

expenses = []

print("Welcome to Expense Tracker!")

while True:
    print("\n======= MENU =======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Exit")
    print("=====================")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food, Travel, Shopping, etc.): ")
        description = input("Enter short description: ")
        try:
            amount = float(input("Enter amount (INR): "))
        except ValueError:
            print("\nInvalid amount! Please enter a valid number.")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("\nExpense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("\nNo expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            for i, e in enumerate(expenses, start=1):
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | Rs.{e['amount']:.2f}")
            print("---------------------")

    elif choice == "3":
        total = sum(e["amount"] for e in expenses)
        print(f"\nTotal Spending = Rs.{total:.2f}")

    elif choice == "4":
        if len(expenses) == 0:
            print("\nNo expenses recorded yet.")
        else:
            summary = {}
            for e in expenses:
                cat = e["category"]
                summary[cat] = summary.get(cat, 0) + e["amount"]

            print("\nSpending by Category:")
            for cat, amt in summary.items():
                print(f"{cat}: Rs.{amt:.2f}")

    elif choice == "5":
        print("\nThanks for using Expense Tracker! Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")
