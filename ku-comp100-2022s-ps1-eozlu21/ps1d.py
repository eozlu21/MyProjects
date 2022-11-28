salary = int(input("Enter your monthly salary: "))
total_cost = int(input("Enter the cost of the dream house: "))
percentage_increase = float(input("Enter monthly interest rate applied to the debt, as a decimal: "))
percentage_salary_increase = float(input("Enter the increase monthly interest rate to the house's price"
                                         ", as a decimal: "))

upper_limit = 10000
lower_limit = 0
percentage_saved = (upper_limit + lower_limit) / 2
number_of_bisection_steps = 0
total_money_saved = 0
number_of_months = 0
epsilon = 1000
possible = True

while True:
    remaining_cost = total_cost  # reset remaining cost
    monthly_salary = salary  # reset monthly salary to get rid of raise
    for month in range(1, 49):
        if month % 6 == 1 and month != 1:
            monthly_salary = monthly_salary * (1 + percentage_salary_increase)
        remaining_cost = remaining_cost - monthly_salary * (percentage_saved / 10000)
        remaining_cost = remaining_cost * (1 + percentage_increase)
    if remaining_cost > epsilon and percentage_saved == 10000:
        print("It is not possible to buy the house in four years")
        possible = False
        break
    elif -epsilon < remaining_cost < epsilon:
        break
    elif remaining_cost > epsilon:
        lower_limit = percentage_saved
        percentage_saved = (upper_limit + percentage_saved) / 2
        number_of_bisection_steps += 1
    elif remaining_cost < -epsilon:
        upper_limit = percentage_saved
        percentage_saved = (lower_limit + percentage_saved) / 2
        number_of_bisection_steps += 1
if possible:
    print("Best savings rate: " + str(round((percentage_saved / 10000),3)))
    print(("Steps in bisection search: " + str(number_of_bisection_steps)))
