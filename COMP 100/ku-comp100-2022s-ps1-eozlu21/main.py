#Q1

number = int(input("Enter an integer: "))
if number > 0:
    print(str(number) + " is positive.")
elif number == 0:
    print(str(number) + " is zero.")
else:
    print(str(number) + " is negative.")

#Q2

num = int(input("Enter an integer: "))
if num % 2 == 1:
    print(str(number) + " is odd.")
else:
    print(str(number) + " is even.")

#Q3

val1 = int(input("Enter the first integer: "))
val2 = int(input("Enter the second integer: "))
difference = val1 - val2
if val1 - val2 < 0:
    absolute = True
else:
    absolute = False
if absolute:
    print(-difference)
else:
    print(difference)

#Q4

a = int(input("Enter a number to compare: "))
b = int(input("Enter the first number to compare: "))
c = int(input("Enter the second number to compare: "))

if a > b and a > c:
    print(str(a) + "is greater than both.")
elif a > b or a > c:
    print(str(a) + "is greater than at least one of them.")

#Q5

condition = False
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 + num2 == 10 or num1 == 10 or num2 == 10:
    condition = True
print(condition)

#Q6

for char in "Comp100_is_fun!":
    print(char)

#Q7

for char in "Comp100_is_fun!":
    if not char == "_":
        print(char)
    else:
        print(" ")

#Q8


new_word = ""
for char in "Comp100_is_fun!":
    if not char == "_":
        new_word = new_word + char
    else:
        new_word = new_word + " "
print(new_word)

#Q9

str1 = "abc"
str2 = "12"
for char2 in str2:
    for char1 in str1:
        print(char1 + char2)

#Q10

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue
    else:
        sum += i
print("Sum of all odd numbers from 1 to 100 is " + str(sum))

#Q11

count = 0
current_num = 1
while count < 15:
    if current_num % 3 == 0 and current_num % 2 == 1:
        count += 1
        current_num += 1
    else:
        current_num += 1
print("15 numbers have been found.")

#Q12

str_ind = "Coding is fun! For now."
exclamation_found = False
index_num = 0
new_str = ""
while not exclamation_found:
    if str_ind[index_num] == "!":
        exclamation_found = True
        new_str = new_str + str_ind[index_num]
    else:
        new_str = new_str + str_ind[index_num]
    index_num += 1
print(new_str)

#Q13

str_ind = "Coding is fun! For now."
index_num = 0
new_str = ""
while True:
    if str_ind[index_num] == "!":
        new_str = new_str + str_ind[index_num]
        break
    else:
        new_str = new_str + str_ind[index_num]
    index_num += 1
print(new_str)
