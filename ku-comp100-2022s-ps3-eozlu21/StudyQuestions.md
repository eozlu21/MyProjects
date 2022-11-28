# Study Questions
This part is for the lab but please continue working on the problems even if you cannot finish in the lab.
You can type your answers in "main.py".

## Arithmetic OPerations
1. **(10 points)** We give a basic implementation of a function `print_operation` in "q5.py". 
This function requires three string arguments: two numbers (`'4', '5'`), an aritmetic operation (one of `'+', '-'. '*', '/'`). 
It also has a default argument, a boolean which shows whether to return the result (`True`) or print it (`False`). 
It applies the given arithmetic operation to the two numbers, and prints or returns the result.

> print_operation("5", "2", "+")  # should print "5 + 2 = 7"

See the `#Part 1` below in the same file for some more example test cases.
​
Modify the function in Part 1 of "q5.py" by inserting necessary assertions and throwing relevant errors to handle the following cases:
- when the operation is not one of the pre-defined arithmetic operations (+-*/),
- the input strings cannot be converted to numbers,
- there is a zero division case,
- default case for any other error.

See `#Part 1` in "q5.py" for some example cases.

2. **(5 points)** Write an iterative function that takes as input a list of numbers and operations, all strings, to perform in a chain. 
This means that the output of the first opeartion becomes the first input number for the next operation from left to right:

```
["5", "2", "+", "3", "+", "2", "/"] corresponds to "5 + 2 + 3 / 2 = 5"
```

See `#Part 2` in "q5.py" for some example cases.

**Bonus (5 points)** Implement your solution to the second question recursively.

```
["5", "2", "+", "3", "+", "2", "/"] 
  can be reduced to [7, "3", "+", "2", "/"] 
  can be reduced to [10, "2", "/"]
  ...
```

You can use the same example cases from `#Part 2` in "q5.py" to test your implementation.


## Matrix Operations
Write a function `input_matrix()` that when called, asks a user to enter four floating-point numbers representing a 2x2 square matrix in **column** order, i.e. if the entered numbers are a, b, c, and d, then they represent this matrix:

```
M = [ a, c
      b, d ]
```

Prompt and warn the user with the appropriate exception until they enter four valid floats.

The function must return the matrix as a tuple with four elemetns in column order:

`(a, b, c, d)`

2. Write a function `inverse(M)` that takes a 2x2 matrix as a tuple with 4 elements in column order as input, and returns its inverse.

You can compute the determinant of the matrix `|M|` and its inverse `M_inv` as follows: 

```
|M| = a*d - b*c

M_inv = (1/|M|) * [ d, -c
                   -b, a ]
```
Then, return the result as a tuple with four elements in column order: 

`(d/|M|, -b/|M|, -c/|M|, a/|M|)`

In your your code, catch the cases where the determinant is 0 and raise an exception with the following error message:

> "Determinant is 0, the inverse does not exist."

** Note that in the `inverse(M)` function, you must not use any `if` statements. (use exceptions).**



3. Write a function `matmul(M1, M2)` to implement the matrix multiplication operation for 2x2 matrices by assuming that a matrix is represented as a tuple with four elements in column order, e.g. 

`M = (a, b, c, d)` to represent 

```
M = [ a, c
      b, d ]
```

Given `M1 = (a1, b1, c1, d1)` and `M2 = (a2, b2, c2, d2)`, implement the `matmul` function to return a new tuple with four elements representing the result of the matrix multiplication operation:

```
M1 x M2 = [ a1, c1   x [ a2, c2
            b1, d1 ]     b2, d2 ]
        
        = [ a1*a2+c1*b2, a1*c2+c1*d2
            b1*a2+d1*b2, b1*c2+d1*d2 ]
    

matmul(M1, M2) = (a1*a2+c1*b2, b1*a2+d1*b2, a1*c2+c1*d2, b1*c2+d1*d2) 
```

4. In this part, we want to verify that the inverse matrix computed in the second question, `M_inv`, is indeed the inverse of `M` by multiplying the two matrices and asserting that the result is approximately equal to the 2x2 identity matrix I:

```
M x M_inv ≈ I = [ 1, 0
                  0, 1 ]

matmul(M, M_inv) ≈ (1, 0, 0, 1)
```

Write a function `almost_identity(M, epsilon)` that takes a 2x2 matrix `M` as a tuple in column order form, and a small positive number `epsilon`. It checks the absolute difference between each element of the matrix `M` with the corresponding element of the identity matrix. If any of the absolute differences is greater than epsilon, it should print an error message using an `assert` statement:

> "This matrix is not equal to the identiy matrix."

otherwise it should print:

> "This matrix is approximately equal to the identiy matrix."


Note that the matrix `M = (a, b, c, d)` is approximately equal to the identiy matrix if the following conditions are met:

```
|a-1| < epsilon and |b| < epsilon and |c| < epsilon and |d-1| < epsilon
```


Use this function to check whether the result of multiplication of the original matrix and its inverse is approximately equal to the identiy matrix. 

** Note that in the `almost_identity(M, epislon)` function, you must not use any `if` statements (use the `assert` statement). **

## More Matrix Operations
We will represent a 2D matrix as a nested list, i.e. a list of lists. 

For example:
`a = [[1, 2, 3], [4, 5, 6]]` represents a 2x3 matrix (2 rows and 3 columns) where each inner list is a row:
```
[[1, 2, 3],
 [4, 5, 6]]
```

## 1. (**10 points**) Safe Matrix Operations
In order to multiply two matrices of the same shape, you can multiply each element in one matrix with the corresponding element in the other matrix at the same position.
For example:
```
[[1, 2, 3],  x   [[3, 2, 1],  =  [[1x3, 2x2, 3x1],  =  [[3, 4, 3],
 [4, 5, 6]]       [6, 5, 4]]      [4x6, 5x5, 6x4]]      [24, 25, 24]]
```

This is called element-wise multiplication. Element-wise divison is done in a similar way.

We provide the code for this in "q5.py". However, things might not go as planned.
It may be possible that the two matrices to operate on are not of the same shape. Some rows may have different number of elements. It may be possible that some elements are not numerical values (or cannot be converted to numerical values) and hence cannot be mathematically operated on. It may be possible for some elements to be zero, leading to a division by zero. Look at the code and modify the `element_operate()` function by inserting appropriate assertions and catching relevant errors such that the test cases given below function as expected:

```
## Test 1.1: Element Multiply (*): normal execution
print("Test 1.1:", end = " ")
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = [[5, 6, 7, 8], [1, 2, 3, "4"]]
matrix_operation(a, b, "*") # should print "[[5.0, 12.0, 21.0, 32.0], [5.0, 12.0, 21.0, 32.0]]"

## Test 1.2: Element Multiply (*): inconsistent dimensions
print("Test 1.2:", end = " ")
a = [[1, 2, 3], [5, 6, 7]] # 2x3 matrix
b = [[5, 6, 7], [1, "2"]] # 2x# matrix
matrix_operation(a, b, "*") # should print "dimension mismatch"

## Test 1.3: Element Multiply (*): inconsistent dimensions
print("Test 1.3:", end = " ")
a = [[1, 2, 3], [5, 6, 7], [11]] # 3x# matrix
b = [[5, 6, 7], [1, 2, 3], [11]] # 3x# matrix
matrix_operation(a, b, "*") # should print "dimension mismatch"

## Test 1.4: Element Divide (/): zero element leads to division error
print("Test 1.4:", end = " ")
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = [[5, 6, 7, 8], [1, 2, 3, 0]]
matrix_operation(a, b, "/") # should print "cannot divide by zero"

## Test 1.5: Element Divide (/): non-numerical element leads to error
print("Test 1.5:", end = " ")
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = [[5, 6, "7a", 8], [1, 2, 3, 4]]
matrix_operation(a, b, "/") # should print "could not operate on non-numerical elements"
```
**Hint: ** You can use many assertions at various points in your code to check the sizes of the rows and columns etc. and catch all of them with one `except AssertionError` clause. Click [here](https://docs.python.org/3/library/exceptions.html) for more details.

## 2. (**10 points**) Safe Matrix Multiplication
In order to do matrix multiplication, the number of columns in the first matrix should be equal to the number of rows on the second matrix. For example, if `a` is a 2x3 (2 rows and 3 columns) matrix and `b` is a 3x1 (3 rows and 1 column), then the matrix multiplication (denoted with the '@' symbol) can be done as follows:

```
a = [[1, 2, 3],
     [4, 5, 6]] # 2x3 matrix
b = [[4],
     [3],
     [2]] # 3x1 matrix

result  =  [[1x4 + 2x3 + 3x2],  =  [[4  + 6  +  6],  =  [[16],
            [4x4 + 5x3 + 6x2]]      [16 + 15 + 12]]      [43]]
```

Essentially, what we do is take the sum of products of the i-th row in `a` and the j-th column in `b`, and put the result in the resulting matrix at the i-th row and j-th column.

This algorithm has been implemented for you in the `matrix_multiply()` function. 

This matrix multiplication will not work if the number of columns in `a` is different from the number of rows in `b`. It will also not work if the shape of any of the matrices `a` or `b` have inconsistent shapes i.e. different nuber of elements in each row. Modify the function `matrix_multiply()` by inserting appropriate assertions and catch relevant errors such that the test cases given below function as expected:

```
## Test 2.1: Matrix Multiply (@): normal execution
print("Test 2.1:", end = " ")
a = [[1, 2, 3],
     [4, 5, 6]] # 2x3 matrix
b = [[4, 3, 2, 1],
     [0, 0, 0, 0],
     [3, 7, 11, 15]] # 3x4 matrix
matrix_operation(a, b, "@") # should print "[[13, 24, 35, 46], [34, 54, 74, 94]]"

## Test 2.2: Matrix Multiply (@): inconsistent dimensions may lead to invalid indexing
print("Test 2.2:", end = " ")
a = [[1, 2, 3],
     [4, 5, 6]] # 2x3 matrix
b = [[4, 3, 2, 1],
     [0, 0, 0, 0],
     [3, 7, 11]] # 3x# matrix
matrix_operation(a, b, "@") # should print "dimension mismatch"

## Test 2.3: Matrix Multiply (@): invalid dimensions for matrix multiplication
print("Test 2.3:", end = " ")
a = [[1, 2, 3, 4],
     [4, 5, 6, 7]] # 2x4 matrix
b = [[4, 3, 2, 1],
     [0, 0, 0, 0],
     [3, 7, 11, 15]] # 3x4 matrix
matrix_operation(a, b, "@") # should print "dimension mismatch"

## Test 2.4: Matrix Multiply (@): This example may lead to a 2x4 result, but this should not happen because 'b' has inconsistent dimensions
print("Test 2.4:", end = " ")
a = [[1, 2, 3],
     [4, 5, 6]] # 2x3 matrix
b = [[4, 3, 2, 1],
     [0, 0, 0, 0, 1, 1],
     [3, 7, 11, 12, 13]] # 3x# matrix
matrix_operation(a, b, "@") # should print "dimension mismatch"
```