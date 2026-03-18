expenses = []
print("Welcome to Expense Tracker :- ")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        date = input("Enter the Date (DD-MM-YYYY): ")
        category = input("Enter the category: ")
        description = input("Enter short description: ")
        amount = float(input("Enter the Amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            count = 1
            for eachExpense in expenses:
                print(f"Expense No {count}: {eachExpense['date']}, "
                      f"{eachExpense['category']}, "
                      f"{eachExpense['description']}, "
                      f"{eachExpense['amount']}")
                count += 1

    elif choice == 3:
        total = 0
        for eachExpense in expenses:
            total += eachExpense["amount"]
        print("Total Expenses = ", total)

    elif choice == 4:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")


