monthly_salary = int(input("Enter your monthly salary: "))
percentage_saved = float(input("Enter the percentage to save, as a decimal: "))
total_cost = int(input("Enter the cost of the dream house: "))
total_money_saved = 0
number_of_months = 0
while total_money_saved < total_cost:
    total_money_saved = monthly_salary * percentage_saved + total_money_saved
    number_of_months += 1
print("Number of months: " + str(number_of_months))
