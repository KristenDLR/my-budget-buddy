# expense_tracker/main.py

from expense_tracker.budget import track_budget
from expense_tracker.utils import load_expenses, save_expenses
from .expenses import add_expense, view_expenses
from consolemenu import SelectionMenu

def main():
    print("Welcome to the Expense Tracker!")

    expense_dictionary = load_expenses()

    while True:
        menu_options = [
            "Add expense",
            "View expenses",
            "Track budget",
            "Save expenses",
        ]

        menu = SelectionMenu(menu_options, title="Expense Tracker", subtitle="Choose an option:")
        menu.show()
        choice = menu.selected_option

        if choice == 0:
            add_expense(expense_dictionary)
        elif choice == 1:
            view_expenses(expense_dictionary)
        elif choice == 2:
            track_budget(expense_dictionary)
        elif choice == 3:
            save_expenses(expense_dictionary)
        elif choice == 4:
            print("👋 Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
