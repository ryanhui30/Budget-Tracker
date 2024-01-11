from expense import Expense
import calendar
import datetime

def main():     # main function
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense
    expense = get_expense()

    # Write expense to a file
    save_expense(expense, expense_file_path)

    # Read file and summarize expenses
    summarize_expense(expense_file_path, budget)

def get_expense():
    print(f"🎯 Getting User Expense")

    expense_name = input("Enter expense name: ")    # input function takes in expense name
    expense_amount = float(input("Enter expense amount: "))   # take input and cast as float

    print(f"You've entered {expense_name}, {expense_amount}")     # prints expense name

    expense_categories = [      # categories list
        "🍜 Food",
        "🛖 Home",
        "💻 Work",
        "🎉 Fun",
        "🧢 Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):      # enumerate function gives tuple response, index of the item and the value of the time
            print(f"    {i + 1}. {category_name}")

        valued_range = f"[1 - {len(expense_categories)}]"       # string to store range of values
        selected_index = int(input(f"Enter a category number {valued_range}: ")) - 1    # gets category input

        if selected_index in range(len(expense_categories)):    # check if selected index is in range of expense categories list
            selected_category = expense_categories[selected_index]      # get selected category based off expense category and the selected index
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)   # new expense contains 3 information parts
            return new_expense      # return new expense with 3 parts
        else:
            print("Invalid category. Please try again!")

def save_expense(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:        # open file and add to file
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")     # write expense values file

def summarize_expense(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = []       # create expenses list

    with open(expense_file_path, "r") as f:     # open file as read only
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",") # strip empty lines, split line into parts
            line_expense = Expense(name = expense_name, amount = float(expense_amount), category = expense_category)
            expenses.append(line_expense)

    amount_by_category = {}     # create amount by category dictionary
    for expense in expenses:    # loop through expense in expenses
        key = expense.category      # key for dictionary
        if key in amount_by_category:       # check if key already exists
            amount_by_category[key] += expense.amount       # if it does, add it to new expenses
        else:
            amount_by_category[key] = expense.amount        # new entry equals starting amount

    print("Expenses By Category: ")
    for key, amount in amount_by_category.items():       # get key and value in dictionary
        print(f"    {key}: ${amount:.2f}")      # display expenses by category

    print(amount_by_category)

    total_spent = sum([x.amount for x in expenses])       # calculate total spent by summing every expense in expenses
    print(f"💰 Total spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent     # calculates remainng budget
    print(f"📉 Budget remaining: ${remaining_budget:.2f}")

    # Calculates budget per day based off the day of the month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days
    print(green(f"🌞 Budget Per Day: ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":      # only be true when running expense tracker directly and not from inmport
    main()




