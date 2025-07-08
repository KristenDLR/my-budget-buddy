
def track_budget(expense_dictionary):
    try:
        # trying to compare string, need to converted to float
        monthly_budget = float(input("Enter the total amount you want to budget this week: $"))
    except ValueError:
        # validate type
        print("Invalid input. Please enter a number.")
        return

    total = sum(expense["amount"] for expense in expense_dictionary.values())
    difference = monthly_budget - total

    print(f"\n📊 Total spent: ${total:.2f}")
    print(f"🎯 Budget: ${monthly_budget:.2f}")

    if total > monthly_budget:
        print(f"⚠️ You have exceeded your budget by ${abs(difference):.2f}!")
    else:
        print(f"✅ You have ${difference:.2f} remaining in your budget.")
