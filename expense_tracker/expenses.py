import datetime
from consolemenu import SelectionMenu

expense_dictionary = {}
expense_id = 1

# check day is valid and return a datetime object
def checkDay_isValid(month, year):
    thirtyOne_dayMonth = [1, 3, 5, 7, 8, 10, 12]

    while True:
        try:
            day = int(input("Enter a day: "))

            if day < 1 or day > 31:
                print("Error: Day must be between 1 and 31.")
                continue

            if month == 2:
                if day > 29:
                    print("Error: February never has more than 29 days.")
                    continue
                elif day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    print(f"Error: {year} is not a leap year, so February has only 28 days.")
                    continue
            elif month not in thirtyOne_dayMonth and day > 30:
                print(f"Error: Month {month} only has 30 days.")
                continue

            return datetime.datetime(year, month, day)

        except ValueError:
            print("Invalid input. Please enter a valid numeric day.")



def add_expense():
    print("Enter date of expense:")

    # Get year
    while True:
        try:
            year = int(input("Enter a year (e.g., 2025): "))
            break
        except ValueError:
            print("Invalid input. Please enter a 4-digit year.")

    # Get month
    while True:
        try:
            month = int(input("Enter a month (1-12): "))
            if 1 <= month <= 12:
                break
            else:
                print("Error: Month must be between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a numeric month.")

    # Get and validate day using the helper function
    date_obj = checkDay_isValid(month, year)
    formatted_date = date_obj.strftime("%Y-%m-%d")
    print(f"Valid date: {formatted_date}")

    # Select a category
    categoryOptions = [
        "Housing", "Transportation", "Entertainment", "Health", "Personal Care",
        "Utilities", "Food and Drink", "Gifts", "Pets", "Debt/Retirement", "Miscellaneous"
    ]
    catogoryMenu = SelectionMenu(categoryOptions, title="Category", subtitle="Please choose an option:")
    catogoryMenu.show()
    choice = catogoryMenu.selected_option
    print(f"You selected: {categoryOptions[choice]}")

    # Get amount
    while True:
        try:
            amount = float(input("Enter the amount spent: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    # Get description
    description = input("Enter a brief description: ")

    global expense_id

    # Create the expense record
    newExpense = {
        "date": formatted_date,
        "category": categoryOptions[choice],
        "amount": amount,
        "description": description
    }

    # expense_dictionary.append(newExpense)
    expense_dictionary[expense_id] = newExpense
    expense_id += 1

    print("\nNew Expense Recorded:")
    print(newExpense)
    print(expense_dictionary)



# TODO: Store the dictionary in a CSV file, pre fill table from saved CSV
def view_expenses(expense_dict):
    print("\n{:<5} {:<15} {:<20} {:<10} {:<30}".format('ID', 'Date', 'Category', 'Amount', 'Description'))
    print("-" * 85)
    for id, expense in expense_dict.items():
        print("{:<5} {:<15} {:<20} ${:<9.2f} {:<30}".format(
            id,
            expense["date"],
            expense["category"],
            expense["amount"],
            expense["description"]
        ))
