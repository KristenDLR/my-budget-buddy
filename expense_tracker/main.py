# expense_tracker/main.py

from .expenses import add_expense

def main():
    print("Welcome to the Expense Tracker!")
    # show menu and route user input
    add_expense()

if __name__ == "__main__":
    main()
