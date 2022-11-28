
# PS1 - Your Dream House
## Deadline: March, 13th at 23:00
## Introduction

In this problem set, you will use Python control flow to solve a computational problem, by using *Bisection Search*. In total, you will solve **four** different problems. For each part, you should write your code in the file ps1{name of the part}. For example, for part D, it should be "ps1d.py".

Suppose that you get a high-paid SW engineer job in FAANG (Facebook, Amazon, Apple, Netflix, and Google). You would like to save for a house in the suburbs that you always dreamed of. In each part of this problem set, we will explore different kinds of mini problems with the same goal in mind: buying your dream house!

We provide some example test cases whose results will appear on GitHub actions after you commit your work. You can do multiple commits, only the latest one before the deadline will be graded. Note that **there will be additional test cases** that we will use when grading your solutions, so the points you see when you commit will not be your final grade.

---

## Parts
1. Buying the house in an unrealistic scenario
2. Buying the house with a bank loan
3. Good news: Salary raise!
4. The fastest way to save for the house

---

## PART A. Buying the house in an unrealistic scenario

In this part, you will calculate how many months it takes to buy your dream house with the given inputs such as your monthly salary, what percentage of the salary you will save each month, and the cost of the house.

The reason we call it an unrealistic scenario is that we assume neither the house's price nor your salary changes during this time.

* Call the cost of the house `total_cost`.
* Call your saving `current_savings` which will start from `0`.
* Call your monthly salary `monthly_salary`.

**Write a program that calculates how many months it will take to save the total cost of your dream house. Your program should ask the user to enter the following variables:**

* Monthly salary (`monthly_salary`)
* Percentage saved (`percentage_saved`)
* The total cost of the house (`total_cost`)

### Hints

Here is an outline for you to start:

* Ask the user for the inputs.
* Initialize the variables.
* Calculate how many months it will take to buy the dream house.
* Print out what you found.

### Example Case

>>>   
Enter your monthly salary: 12000    
Enter the percentage to save, as a decimal: .2   
Enter the cost of the dream house: 180000    
Number of months: **75**   
>>>


## PART B. Buying the house with a bank loan

In this part, again you will calculate the same thing with a small difference. Assume that you decided to use a cash loan from the bank to buy the house immediately. As a result, you will pay an interest fee which happens to be compounded monthly on the debt to be paid, this ends up being more expensive than paying the initial price. You will ask for the same inputs from the user, and an extra monthly interest rate variable. Here, you can assume that your monthly savings are directly paid to the bank. You will use this monthly interest rate to update the debt to be paid, monthly.

Algorithmically, you should:

* First, make the payment depending on the variable `percentage_saved`, then update the total debt with `percentage_increase`.

Write a program that calculates how many months it will take to save the total cost of your dream house. Your program should ask the user to enter the following variables:   

* Monthly salary (`monthly_salary`)
* Percentage saved (`percentage_saved`)
* The total cost of the house (`total_cost`)
* The interest rate of the house's remaining debt (`percentage_increase`)

### Example case

>>>   
Enter your monthly salary: 12000   
Enter the percentage to save, as a decimal: 0.2   
Enter the cost of the dream house: 180000    
Enter monthly interest rate applied to the debt, as a decimal: .012
Number of months: **185**   180
>>>

**Note:** To prevent the infinite loops in case of monthly increase exceeds your payments, you can keep the monthly interest rate smaller.

## PART C. Good news: Salary raise!

In this part, again you will calculate the same thing with a small difference. Every 6 months, your monthly salary will increase. For example, at the start, assume that your salary is 5000$ and with a 5% increase every 6 months, your salary will become 5250$ at the beginning of the 7th month and it will become 5512.5$ at the beginning of the next year (13th month). You will ask for the same inputs in Part B with one additional one which is the percentage salary raise and you will calculate the same output as in the PART A and PART B.

Write a program that calculates how many months it will take to save the total cost of your dream house. Your program should ask the user to enter the following variables:   

* Monthly salary (`monthly_salary`)   
* Percentage saved (`percentage_saved`)   
* The total cost of the house (`total_cost`)
* The interest rate of the house's remaining debt (`percentage_increase`)
* The percentage salary raise of your monthly salary (`percentage_salary_increase`)

### Example case

>>>   
Enter your monthly salary: 12000  
Enter the percentage to save, as a decimal: .2   
Enter the cost of the dream house: 180000   
Enter the increase monthly interest rate to the house's price, as a decimal: .012
Enter the percentage salary raise, as a decimal: .1   
Number of months: **69**
>>>

## PART D. The fastest way to save for the house

In this part, we will explore the bisection search we learned in class. In the first three parts, you explored the effects of the raises in your salary and the interest rates. Now, you need to find how much you need to save each month to be able to buy the house in 4 years (48 months). What is the percentage of the salary you need to save to achieve this?

You will write a program that calculates the percentage of the monthly salary you need to save each month to buy your dream house. You **must** use the bisection search for this.

Your program should ask the user for the following inputs:   

* Monthly salary (`monthly_salary`)
* The total cost of the house (`total_cost`)
* The interest rate of the house's remaining debt (`percentage_increase`)
* The percentage salary raise of your monthly salary (`percentage_salary_increase`)

It should output the "Best saving rate" and "The number of steps in bisection search".

### Hints

* Since hitting an exact value of the house will be difficult, we simply want your total savings at the end of 4 years to be within 1000$ of the cost of the house.    

* You need to count the steps in the bisection search because it is needed in the output.    

* We do not want you to worry about the difference between float values, for example, between 3.081% and 3.079%. Therefore, we can search for an integer value between 0 and 10000 and then convert it to a decimal percentage using simple float division. By searching this range, we simply limit the number of possibilities and we prevent the infinite loops caused by the infinite number of values between 0 and 1. The reason we use 0 to 10000 is to account for two additional decimal places in the range 0% and 100%. Your code should print out a decimal: for example, 0.030 for 3.08%.     

* In the cases where it is not possible to save with the current salary and the cost of the house, you should notify the user that it is not possible to save for this house in 48 months.


**Note: Since there are multiple ways to implement bisection search, the number of steps in the output may not match perfectly with the example cases.**   

### Example cases

>>>   
Enter your monthly salary: 12000    
Enter the cost of the dream house: 180000    
Enter monthly interest rate applied to the debt, as a decimal: .012
Enter the percentage salary raise, as a decimal: .1  
The best saving rate: **0.301**      
The number of steps in bisection search: **7**   
>>>   


>>>   
Enter your monthly salary: 6000
Enter the cost of the dream house: 350000    
Enter monthly interest rate applied to the debt, as a decimal: .02
Enter the percentage salary raise, as a decimal: .05   
**It is not possible to buy the house in four years**
>>>    

---