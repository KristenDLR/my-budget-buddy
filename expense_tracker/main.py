# expense_tracker/main.py

from .expenses import add_expense, view_expenses, expense_dictionary
from consolemenu import SelectionMenu

def main():
    print("Welcome to the Expense Tracker!")

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
            add_expense()
        elif choice == 1:
            view_expenses(expense_dictionary)
        elif choice == 2:
            print("🔍 Budget tracking TBD")
        elif choice == 3:
            print("Save to CSV TBD")
        elif choice == 4:
            print("👋 Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
