# IMPORTANT NOTE 1:
For each lab assignment, **you must include and sign (by writing your name and student id number) the following Pledge of Honor statement at the beginning of your main method source code file. After including this statement, make sure that you do the commit and push operation on GitHub. Otherwise, your lab solution will not be graded.**
```
/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: <Name Surname, Student id>
********************************************************************************/
```

## IMPORTANT NOTE 2: After you complete the tasks, do not forget to commit your changes and push them to your repository on Github.

## IMPORTANT NOTE 3: This README.md file only contains the instructions for PRELAB. You will also have INLAB questions.

INLAB QUESTIONS WILL BE ANNOUNCED AT COURSE WEBSITE AT THE START OF EACH LAB: [https://sites.google.com/a/ku.edu.tr/comp132/programming-labs](https://sites.google.com/a/ku.edu.tr/comp132/programming-labs).

# Lab-1: NumGuessr

You are asked to write a simple game application called **NumGuessr** for two users. Application generates a random number between 1-100. The users try to guess the number, and the user with the closest guess wins and gains points based on some criteria which is explained below. NumGuessr will be played for 3 rounds. Afterwards, the user who has the highest score will be printed on screen.

Inside the given Java project, you should create a package named **numguessr** and a class named **User** inside the package.

## User Class

### User Class Instance Variables:

User Class has the following private instance variables:

```java
String name;
int guessedNumber;
int totalScore;
```

### User Class Public Methods:

Define the constructor for this class:

```java
public User(String userName)
```

+ Initialize the **totalScore** to zero in the constructor.

Implement the getter and setter methods for both **totalScore** and **guessedNumber** variables and a getter method for the **name** variable.

Define **incrementTotalScore** method:

```java
public void incrementTotalScore(int points)
```

+ This method increases the **totalScore** by **points** amount.


## NumGuessr Class

Inside the **numguessr** package, you will create another class called **NumGuessr**.

**NumGuessr** class has the following private instance variables:
```java
User user1;
User user2;
```

### Numguessr Class Public Methods:

Define the constructor for this class:
```java
public Numguessr(User user1, User user2)
```

Define the **play** method:

```java
public void play(int numberToGuess)
```

+ This method will get users' guessed number and calculate the distances of the users' input with **numberToGuess**.

+ After printing **numberToGuess** to the users in an understandable manner, Assume **distance1** will be the user 1's distance to **numberToGuess** and **distance2** will be the user 2's distance to **numberToGuess**. The scoring criteria for users are as following:

    + If **distance1** is smaller than **distance2**, user 1 is rewarded with **distance2** points.

    + If **distance2** is smaller than **distance1**, user 2 is rewarded with **distance1** points.

+ In both of the cases above, you must print the winning user's name in an understandable manner. As an example:

    ```java 
    "Name of a user" + "won." 
    ```

    + If **distance1** equals to **distance2**, both users is rewarded with **101** points. You must print:
    ```java
    "Name of user 1"+ " and "+ "Name of user 2"+ " were the same distance to "+numberToGuess+"!"
    ```

    + If **distance1** or **distance2** equals to zero, the user who managed to guess the number will get **101** points. You must print:
    ```java
    "Name of user"+ " guessed the number correctly!"
    ```

    + If both **distance1** and **distance2** is zero, both users are rewarded with **202** points. You must print:
    ```java
    "Both "+"Name of user 1"+ " and "+ "Name of user 2"+ " guessed the number correctly!"
    ```

Here is an example:
![](https://github.com/Comp132Classroom/Fall2022-Lab1/blob/main/Example_round.jpg)

Define the **whoWon** method:

```java
public void whoWon()
```

+ This method will compare the points of both and print out the winner with how much points the winner earned which must look like:

```java
"Name of user" + "has won 3 rounds of NumGuessr with a total " + "Total score of user 1" + " points."
```
+ However; if both users got the same total score, the output must look like:

```java
"3 rounds of NumGuessr between " + "Name of user 1" + " and " + "Name of user 2" + " were resulted with a tie with both scoring " + "Score of a user" + " points.”
```

## Main Class

In **Main** class under package **main**, you should implement the **main** function with the following algorithm:

+ Get 2 user names from the terminal input and create 2 **User** objects.
+ Create a **Numguessr** object with the created **User** objects.
+ Play 3 rounds of **Numguessr** by getting guessed numbers from each of the users. Integers must be between 1 and 100 (both inclusive). You must print the following sentence before getting the input from each of the users. 

```java
    "Name of a user" + " enter a number between 1 and 100 (both inclusive)."
```
+ If a user puts a number outside of the range 1 and 100, you must print the following sentence.

```java
    "Wrong input is given. Try Again."
```
+ Do not forget to set a user's guessed number before playing a round of **Numguessr**.

+ To generate a random number between 1 and 100, you can use **getRandomNumber()** method which is already given to you in **Main** class. 

+ At the end of 3 rounds, print the result of the 3 **Numguessr** rounds.

## Sample Run 

```bash
User 1 Name:
Doğan
User 2 Name:
Müge

Doğan enter a number between 1 and 100 (both inclusive).
343 
Wrong input is given. Try Again.
47

Müge enter a number between 1 and 100 (both inclusive).
-29
Wrong input is given. Try Again.
2
Number to guess was: 7
Müge won.

Doğan enter a number between 1 and 100 (both inclusive).
76

Müge enter a number between 1 and 100 (both inclusive).
23
Number to guess was: 60
Doğan won.

Doğan enter a number between 1 and 100 (both inclusive).
11

Müge enter a number between 1 and 100 (both inclusive).
97
Number to guess was: 34
Doğan won.

Doğan has won the NumGuessr with a total of 100 points.
```
