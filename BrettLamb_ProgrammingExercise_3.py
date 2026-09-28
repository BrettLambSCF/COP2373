from functools import reduce #imports the reduce function

#define our main function
def monthly_expenses():
    #create and empty list that will store all of their expenses
    expenses = []

    #store their amount of expenses inside the number_of_expenses variable
    number_of_expenses = int(input("How many different monthly expenses do you want to list? "))

    #the for loop will iterate as many times as the number of expenses they entered
    for i in range(number_of_expenses):
        print()
        name_of_expense = input("Please enter what the expense is: ")
        expense_amount = float(input("Please enter the amount/cost: $")) #float will convert their # into decimal
        expenses.append([name_of_expense, expense_amount]) #add their expense to the list of expenses

    #uses the reduce function to go through expenses list and combine the values together
    # x is the current total and y is the current expense, and 0 uses reduce() to start total at 0
    total = reduce(lambda x, y: x + y[1], expenses, 0)

    #uses the reduce() function again to get the expense with the highest amount
    highest = reduce(
        lambda x, y: x if x[1] > y[1] else y,
        expenses
    )

    # uses the reduce() function again to get the expense with the lowest amount
    lowest = reduce(
        lambda x, y: x if x[1] < y[1] else y,
        expenses
    )
    #all the calculations printed out
    print()
    print("Monthly Expense Information")
    print("---------------------------")
    print("Total expenses: $", format(total, ".2f"))
    print("Highest expense:", highest[0], "- $", format(highest[1], ".2f"))
    print("Lowest expense:", lowest[0], "- $", format(lowest[1], ".2f"))

monthly_expenses()