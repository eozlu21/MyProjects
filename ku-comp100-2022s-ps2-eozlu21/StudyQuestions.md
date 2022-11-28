# Study Questions
This part is for the lab but please continue working on the problems even if you cannot finish in the lab.
You can type your answers in "main.py".

## I. Tuples & Lists

### Q1 - reshape
Write a function that takes a tensor (a matrix with more dimensions than 2) shape as a tuple, merges the dimensions except the first one, and returns the resulting shape as a tuple. 

```
reshape( (16,3,28,28) ) -> (16, 2352)      # 3*28*28 = 2352
reshape( (16,40,1,64,64) ) -> (16, 163840) # 40*1*64*64 = 163840
```


### Q2 - replace last
Write a function that takes a list of tuples as input and replaces the last element of each tuple with the first element of that tuple.​

```
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90, 100)]
replace(l) -> [(10, 20, 10), (40, 50, 40), (70, 80, 90, 70)]
```

**Hint:** Note that the tuples can be of any size.  



### Q3 - removing elements from lists

Suppose you have a stack of books you need to study. Write a function to return the next book on top of the stack, and the rest of the books as a tuple.  
```
books = ["Chem","Physics","Writing","Programming","Math"]
next_to_read() -> ("Math", ["Chem","Physics","Writing","Programming"])
next_to_read() -> ("Programming", ["Chem","Physics","Writing"])
```

**Bonus:** 
- What if we want to study the books in order?  e.g. Chem first, then Math, ... 
- What if decide not to study Writing and remove it from the pile but we don't know where it is in the list? 
- What if we thought the pile is just too much, and randomly selected to remove the second book from the bottom? 

### Q4 - merge lists

Write a function that merges two lists in a zig-zag manner (one from l1, one from l2), and returns a single list. 

```
l1 = [1,3,5,7]
l2 = [20,40,60,80]
merge(l1, l2) -> [1,20,3,40,5,60,7,80]
```

**Bonus:** Modify your function so that it works on lists with different lenghts as well. In that case, you add all the remaining elements in the longer list in the end. You can assume that we always start with the first list. 

```
l1 = [1,3]
l2 = [20,40,60,80]
merge(l1,l2) -> [1,20,3,40,60,80]
```


### Q5 - minibatch

Suppose you are working on an artificial intelligence project which requires data. You are required to feed your list data into a model but as mini-batches of fixed batch size n. mini-batches are like smaller pieces of the original list. Write a function to convert a list into nested list of n minibatches.

```
data = [12, 24, 47, 5, 63, 105, 5, 95, 8, 14, 2, 7]
batch_size = 4 
minibatch(data) -> [[12, 24, 47, 5], [63, 105, 5, 95], [8, 14, 2, 7]]
```

**Note:** You may assume that the mini-batch size is divisible by the total length of the list.


**Bonus - The pythonic way:** Did you know that you can do that as a one-liner code in Python? It's not very readable and recommended only when you are comfortable with lists.



### Q6 - circular lists

Write a python program to check whether two lists are circularly identical.

For example, if we have the following lists:

```
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
```
Here, list1 and list2 are circularly identical becuase if you rotate the elements of list 1 like a treadmill, you get list 2 and vice versa. On the other hand list3 is not circularly identical to list1 and list2.​



## II. List Aliasing

### Q1
Consider the following functions:
```
def double_first1(a):
  a[0] *= 2
  return a
​
def double_first2(a):
  a[0] *= 2
​
def change_list1(a):
  a = [100, 200, 300]
  return a
​
def change_list2(a):
  a = [1000, 2000, 3000]
```

What will `l1`, `l2`, and `l3` be after the following operations?
```
l1 = [10, 20, 30]
l2 = double_first1(l1)
double_first2(l2)
l3 = change_list1(l1)
change_list2(l2)
```  


### Q2. Side Effects (Exam Question)

1. Make the necessary changes to the `print_halves` function in "side_effects.py" so that it prints the following:

```
1) input_list: [2, 4, 6, 8, 10]
1) output_list: [1, 2, 3, 4, 5]
```

2. Make the necessary changes to the `print_halves_2D` function in "side_effects.py" so that it prints the following:

```
2) input_list_2 : [[2, 4, 6, 8, 10], [20, 40, 60, 80, 100]]
2) output_list_2 : [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]
```

3. Make the necessary changes to the `remove_az` function in "side_effects.py" so that it prints the following:

```
3) Input list before: ["f", "z", "b", "d", "z", "a"]
3) Input list after: ["f",  b", "d"]
```


## III. Variable Scopes (Exam Question)


Modify the two functions in "variable_scopes.py" so that the program prints the following, without defining new variables or inserting new print statements.

```
1
Inside
2
Inside
=========
1
2
3
4
5
```
