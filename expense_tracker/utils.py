import csv

def save_expenses(expense_dictionary):
    csv_filename = "budgetBuddy_expenses.csv"
    fieldnames = ["date", "category", "amount", "description"]

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expense_dictionary.values()) 

def load_expenses(csv_filename="budgetBuddy_expenses.csv"):
    expense_dict = {}
    try:
        with open(csv_filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader, start=1):
                expense_dict[idx] = {
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"]),
                    "description": row["description"]
                }
                print("Your expenses have been Saved in budgetBuddy_expenses.csv 💾")
    except FileNotFoundError:
        print("No previous expense file found. Starting fresh.")
    return expense_dict