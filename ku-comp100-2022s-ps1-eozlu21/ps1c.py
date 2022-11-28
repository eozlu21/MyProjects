monthly_salary = int(input("Enter your monthly salary: "))
percentage_saved = float(input("Enter the percentage to save, as a decimal: "))
total_cost = int(input("Enter the cost of the dream house: "))
percentage_increase = float(input("Enter monthly interest rate applied to the debt, as a decimal: "))
percentage_salary_increase = float(input("Enter the increase monthly interest rate to the house's price"
                                         ", as a decimal: "))
total_money_saved = 0
number_of_months = 0
while total_cost > 0:
    if number_of_months % 6 == 1 and number_of_months != 1:
        monthly_salary = monthly_salary * (1 + percentage_salary_increase)
    total_cost = total_cost - monthly_salary * percentage_saved
    total_cost = total_cost * (1 + percentage_increase)
    number_of_months = number_of_months + 1
print("Number of months: " + str(number_of_months))
