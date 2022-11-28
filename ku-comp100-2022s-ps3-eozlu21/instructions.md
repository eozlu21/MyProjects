# PS3
## Deadline: 01.05.2022 - 23:00 
In this assignment, you will learn how to apply recursion to solve different problems. 
Note that this assignment, like any other assignment, will be graded with **additional different** test cases. We will check your code to make sure that your solutions are recursive.

Implement all parts as functions, which takes necessary inputs and returns the expected outputs. You should not modify the main scope other than defining functions at dedicated `YOUR CODE HERE` sections and passing your arguments at dedicated `...` parts. **All problems should be solved with recursion, iterative solutions will not be accepted.** 
**Use of additional global variables is not allowed. Using nested functions to avoid using global variables is also not allowed.**


## Problem 1: Kevin's Banana Puzzle
Kevin loves to eat, live and dream bananas. During lunch break, Kevin visits a nearby shop that sells one banana at a certain price. Additionally, the shop lets you buy a banana if you can give the shop owner a certain number of banana peels. Kevin has a certain amount of money in his pocket, which he can use to buy a certain number of bananas. Kevin also likes to think about how many total bananas he can eat if he also exchanges the peels.

Your task is to write a recursive function that does this calculation for him because Kevin cannot think when there are bananas around. How many bananas can Kevin eat in total if he spends all his money to buy bananas and exchanges all the peels from the bananas he eats for more bananas?

- `money` is the amount  of money that Kevin has in his pocket
- `price` is the price at which the shop sells each banana
- `price_p` is the number of peels you can trade for an extra banana. You can think of `price_p` as the price of a banana in a different currency, price in peels.

You must implement your **recursive** functions in the provided `maxBananas.py` file.   
You may assume that all inputs and results will be integers.   

**Example:** Assume that `money = 5`, `price = 1`, and `price_p = 5`. Initially, with the money, Kevin can buy 5 bananas. After eating them, he will have 5 peels. Since `price_p = 5`, he can get another banana by giving the 5 peels he has. After that he will end up with a single peel which he can not exchange anymore. Then, Kevin could eat 6 bananas in total.


## Problem 2: Deal or No Deal - Remastered
In this question, we are considering a modified version of Deal or No Deal game (Var Mısın Yok Musun in Turkish). 

Suppose that we are given a line of closed boxes, each holding an amount of money inside. There is a single player. At each round, the player can either pick the first box or the last box of the line, these actions are labeled as `L` for left end (first box), `R` for right end (last box). Note that the player doesn't know what's inside the boxes, so the choice is quite random. But each choice affects the possible gain.

Assume the length of this line to be N, and the number of allowed choices to be K, where N>=K. N, K, and the list of boxes are all inputs to the program, they are not fixed variables.

You as "Hamdi Bey" have access to this line beforehand, and want to figure out the best way of selecting, so that you can plan to make reasonable offers during the game. Your task is to write a function that finds the sequence of actions that achieve the optimum gain. Your function should recursively traverse all possible action sequences, and find the one with the maximum gain. 

**Example:** Given the line as `[1, 100, 10, 20, 5]`, and `K=3`, let's calculate some of the possible action sequences:
```
R, R, R -> 5 + 20 + 10 = 35
R, R, L -> 5 + 20 + 1 = 26
R, L, R -> 5 + 1 + 20 = 26
R, L, L -> 5 + 1 + 100 = 106
L, R, R -> 1 + 5 + 20 = 26
L, R, L -> 1 + 5 + 100 = 106
L, L, R -> 1 + 100 + 5 = 106
L, L, L -> 1 + 100 + 10 = 111
```
The maximum gain in this case would be to the case of L, L, L. 


**Note:** You may notice that some sequences have the same gain, that's because it's the combination of actions that matters. `L, R, L` and `L, L, R` and `R, L, L` all give the same gain because they are simply 2L and 1R moves. Therefore, you might consider recalculating the same combination as inefficient, but formulating the problem as sequences instead of combinations can help you to implement the recursive logic easier.

**Note:** In case of equal maximum gain from different action sequences, your function can return either one. 


## Problem 3: Strictly Increasing Path in Grid
Consider an M by N grid and suppose that we are in the top-left cell of that grid.

|  1  |  4  |  3  |
|:---:|:---:|:---:|
|**5**|**6**|**7**|

At each step we can go the one of the left, right, up or down cells only if the that cell is **strictly greater than our current cell**. (We cannot move diagonally). We want to find all the paths that we can go from the top-left cell to the bottom-right cell.
In our example, these paths are: `1->4->6->7` and `1->5->6->7`

You are given this grid as a nested list where each sublists corresponds to a row in the grid.   
For our example the grid would be 
```
[[1,4,3],
 [5,6,7]]
 ```

Do not forget that the paths must be **strictly increasing**.  
You should add the found paths to the `all_paths` variable. In our example, all_paths should print:
```
[[1, 4, 6, 7], [1, 5, 6, 7]]
```

Note that you should not return anything, only append to the all_paths variable.


## Problem 4: First Letter, Last Letter

First Letter Last Letter is a simple talking game. At each round the player should come up with a word that starts with the last letter of the previous word. This game usually limits the word space with a category/subject, but for simplicity, we are going to avoid this constraint.  

For example, a short pass can look like this:
```
angel -> level -> light -> theme -> earth ... 
```

Two predefined word lists are given to you in words.py, one short and one long. The short one is there for helping you to debug during the implementation phase. Long list will be our main evaluation list while grading.


### Part 1: 

Your task is to write a function to find the longest possible sequence given a starter word. At each call, you should traverse the word list, find the words that start with the last letter of the previous word, and recursively call your function with the valid words added to the sequences. Each choice leads to a different next last letter, hence, a different sequence. In your function, you should check all possible sequences **recursively** and find the longest one. Your function should return a tuple where first element is the length of this sequence, and the second being the sequence itself as a list.  

**Note:** Each word can only be used once. 

Example testcases:
```
Game mode (1 for short, 2 for long): 1
Enter starter word: angel
5
['angel', 'level', 'light', 'theme', 'earth']
```
```
Game mode (1 for short, 2 for long): 2
Enter starter word: angel 
20
['angel', 'light', 'thank', 'knife', 'early', 'young', 'glass', 'style', 'earth', 'house', 'extra', 'among', 'group', 'pitch', 'human', 'night', 'theme', 'enter', 'rugby', 'yummy']
```

**Note:** If there are more than one sequence that have the max length, your function should return the first one found according to the order of the word list (i.e. alphabetical order).   

Example case in debug mode:

```
angel -> level -> light -> thank 
                        -> theme -> earth
                                 -> empty
      -> light -> thank
               -> theme -> earth
                        -> empty
```

In the example above, we have 2 sequences with max length 5
1. angel -> level -> light -> theme -> earth
2. angel -> level -> light -> theme -> empty

Since earth comes before empty, your function should output the first sequence. 


### Part 2:

In this part, we will make our solution more efficient using dictionaries. In Part 1, at each call, we were iterating over the whole vocabulary list and checking if the current word's first letter is the one we are looking for. This makes our solution slow. To have a more efficient solution, you can create a dictionary that has the first letter of the words as keys, and the corresponding words as values. For example for the short word list `['angel', 'earth', 'empty', 'level', 'light', 'thank', 'theme']`, the dictionary would be like this:

```
{'a': ['angel'], 
'e': ['earth', 'empty'], 
'l': ['level', 'light'], 
't': ['thank', 'theme']}
```

Using this dictionary, you can replace iterating over the list which is O(N) by dictionary lookup which is O(1). Implement `convert_to_dict()` function to obtain the corresponding dictionary, and `longest_sequence_fast()` which should be very similar to part 1 except some small modifications to work with dictionaries.

To see how this modification affects the speed of your solution, we added time function utility, which will measure the time spent executing your functions. You are also required to write comments about your opinions on the time outputs you obtain. 