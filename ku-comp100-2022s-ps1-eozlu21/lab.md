## Logic and If Statements
You can work on the questions below in the file "main.py". 

### Q1: 
Take an integer input from the user, print if it's negative, positive, or zero. 

**Hint:** You can use the `input()` function to get input from the user. Don't forget to change the type of your variable to an integer to be able to perform mathematical operations. 

### Q2: 
Take an integer input from the user, print if it's odd or even. 

**Hint**: You can use the modulo operator `%`. 


### Q3:

Take two integer inputs, and print their difference. Introduce a boolean variable called `absolute`, if it's set to `True`, print the absolute difference instead.  

### Q4:
Use logical `and, or` statements to compare a number `a` to other two numbers `b` and `c`. We are especially interested in these two cases:
* if it is greater than both or
* if it is greater than at least one of them.


### Q5:
Take two integer inputs, `a` and `b`, return `True` if at least one of them is 10 `or` if their sum is 10. Try to implement it with a single `if` statement using the logical operator `or`.


## Loops  

### Q6:
Write a for loop that prints each character of the string `"Comp100_is_fun!"` in a separate line.  

### Q7: 
Repeat Q6 but replace every occurrence of underscore `"_"`  with a space `" "`.   

### Q8: 
Repeat Q7, but print all characters in one line. 
**Hint:** There are more than one way of solving this. The straightforward solution is creating a new string and printing it. If you want a fancy solution, you can modify the `end` argument of print() function. By default, it is newline (`\n`), which is why all the characters are printed in separate lines. 

### Q9: 
Suppose you have 2 strings:
```
str1 = "abc"
str2 = "12"
```
Print the concatenation of each character in `str1` with each character in `str2`, for example for the given input, you should print:
```
a1
b1
c1
a2
b2
c2
```  

### Q10:
Write a for loop to sum all the odd numbers from 0 to 100.  


### Q11:
Write a while loop to iterate over numbers ranging from 1 to an unknown endpoint. First, initialize a counter. At each iteration, if the current number is divisible by 3 and is odd, increase your counter by 1. Stop the loop when you find 15 numbers that meets the condition.   


### Q12: 
Write a `while` loop that prints the characters in a string until an exclamation mark `!` is seen. For example, for the following input

`"Coding is fun! For now."` 

It should print:

`"Coding is fun!"`

**Hints**: 
* Initialize a boolean variable as `True` before the loop. You will use this as your `while` loop condition. Change your boolean variable to `False` when you detect an `"!"` character in your `while` loop. As long as this variable is `True`, you print the character.
* You can access each character in your string using an integer `i`. For example, let `str = "Coding is fun! For now."`. If `i = 0`, then `str[i]` is the character `C`. If `i = 1`, then `str[i]` is the character `o`, and so on.


### Q13:
Repeat Q12. But this time, DO NOT use a boolean variable. 

**Hint**: Remember `break` statement?
