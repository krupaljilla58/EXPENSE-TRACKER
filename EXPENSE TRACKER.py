import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Rent, etc.): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

# View summary
def view_summary():
    total = 0
    category_summary = {}

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            category = row["Category"]

            total += amount
            category_summary[category] = category_summary.get(category, 0) + amount

    print("\n--- Expense Summary ---")
    print(f"Total Spending: ₹{total:.2f}")

    print("\nCategory-wise Spending:")
    for cat, amt in category_summary.items():
        print(f"{cat}: ₹{amt:.2f}")

    if category_summary:
        highest = max(category_summary, key=category_summary.get)
        print(f"\nHighest Spending Category: {highest}")

    print()

# Main menu
def main():
    initialize_file()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
