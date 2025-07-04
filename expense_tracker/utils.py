import csv
from .expenses import expense_dictionary

def save_expenses(expense_dictionary):
    csv_filename = "budgetBuddy_expenses.csv"
    fieldnames = ["date", "category", "amount", "description"]

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expense_dictionary.values()) 

