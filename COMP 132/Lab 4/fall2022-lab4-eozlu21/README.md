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


# Lab-4 Prelab: New Twitter 

In this lab, you will be practicing **Inheritance and its related concepts**. **Inheritance** is one of the key aspects that make Object-Oriented Programming (OOP) possible and incentivizes code **reuse** by modeling an **“is-a” relation** between an existing class (**Superclass**) and derived classes (**Subclasses**).

To practice with the concepts of Inheritance, you are going to implement an imaginary Twitter-like application that reflects a few new features (such as editing a tweet) on top of existing Twitter features (such as sending a tweet).

There are three packages which are:


- **main**: including Main class
- **twitter**: including Twitter and Tweet classes
- **user**: including User, VerifiedUser, and RegularUser classes

There are going to be 6 classes which are: 

- **Main** class is given to you. You don't need to change anything in this class for prelab.
- **Twitter** class contains users and tweets.
- **Tweet** class represents a tweet.
- **User** class is a **superclass** that specifies the common internal data of a user.
- **VerifiedUser** class is a **subclass** that specifies a user with a blue tick. 
- **RegularUser** class is a **subclass** that specifies a regular user.

**NOTE:** For each class implementation, you need to decide which access modifiers should be used for instance variables (e.g. private, protected, or public). In some of the classes, you need to decide on which data types and names you should use for those variables as well. 

## Tweet class

Every Tweet has the following field:

```
- content of Tweet (String)
```

- Implement constructor Tweet(String content). 
- Implement getter/setter methods if needed.
- You should also implement the following methods:

```
- public void edit(String newContent): 
      sets the content of Tweet to newContent
      
- public String toString(): 
      returns the String representation of the Tweet
```

## User class

Every User has the following fields (you need to decide on which fields are private, protected, or public): 

```
- username of User (String)
- id of User (int)
- tweets of User (ArrayList of Tweet)
```

- Implement constructor User(String username). 
- Each user has a unique id as a private field. (HINT: you can use a static variable to keep track of which id to assign to the new user)
- Implement getter/setter methods if needed.
- You should also implement the following methods:

```
- public void displayTweets():
        displays the tweets of the user
        
- public void sendTweet(String content):
        creates a new tweet with the given content and adds it to the tweets list.
```

## VerifiedUser class

Verified users can edit their tweets but cannot delete them.

- Implement constructor VerifiedUser(String username). Do not forget to call super class constructor.
- You should also implement the following methods:

```
- public void editTweet(int id, String newContent):
        edits the tweet with the given id.
```        
Note: Here, id refers to the index of the tweet in the corresponding ArrayList.  
```
- public void displayTweets():
      overrides the super class method by printing the "(Verified)" 
      before printing the name of the user and its tweets.
```

## RegularUser class

Regular users cannot edit their tweets but can delete them.

- Implement constructor RegularUser(String username). Do not forget to call super class constructor.
- You should also implement the following methods:

```
- public void deleteTweet(int id):
        deletes the tweet with the given id.
        
- public void displayTweets(): 
        overrides the superclass method by printing the "(Regular)" 
        before printing the name of the user and its tweets.
```

## Twitter class

Twitter has the following fields:

```
- list of users (ArrayList)
```

- Implement constructor Twitter().
- You should also implement the following methods:

```
- public User addUser(String username, String type):
      Creates a new user object with the given type and adds it to the users' list. 
      The String type is either Verified or Regular. Returns the newly added user. 
      In case the given user type is invalid, the method should display: 
      ” No such user type: “type.” “
      
- public int calculateRevenue():
       Calculates the revenue. Each verified user pays 8 dollars a month. 
       
- public void displayAllTweets(): Displays all the tweets.
```

## Sample output

```
(Regular) Muhammet:
Tweet: Weather is so nice today!
Tweet: I wanna hang out with my friends.
Tweet: My paper has been published, I am so happy :D.

(Verified) Dogan:
Tweet: I have homework deadline for tonight.
Tweet: This weekend is my birthday.
Tweet: I will celebrate my birthday at yacht; who wants to join?

(Regular) Muge:
Tweet: I will watch my favorite TV show.
Tweet: My car is not working.

(Verified) Vahideh:
Tweet: I miss my family.
Tweet: I will return home after my last exam.

(Verified) Kerem:
Tweet: I will join Dogan's birthday.

(Verified) Canberk:
Tweet: I also will join Dogan's birthday party.

------------------------------------
(Regular) Muhammet:
Tweet: Weather is so nice today!
Tweet: I wanna hang out with my friends.
Tweet: My paper has been published, I am so happy :D.

(Verified) Dogan:
Tweet: I will go swimming with Burak.
Tweet: This weekend is my birthday.
Tweet: I will celebrate my birthday at yacht; who wants to join?

(Regular) Muge:
Tweet: I will watch my favorite TV show.

(Verified) Vahideh:
Tweet: I miss my family.
Tweet: I will return home after my last exam.

(Verified) Kerem:
Tweet: I will join Dogan's birthday.

(Verified) Canberk:
Tweet: I also will join Dogan's birthday party.

------------------------------------
(Regular) Muhammet:
Tweet: Weather is so nice today!
Tweet: My paper has been published, I am so happy :D.

(Verified) Dogan:
Tweet: I will go swimming with Burak.
Tweet: This weekend is my birthday.
Tweet: I will celebrate my birthday at yacht; who wants to join?

(Regular) Muge:
Tweet: I will watch my favorite TV show.

(Verified) Vahideh:
Tweet: I also wanna join Dogan's birthday.
Tweet: I will return home after my last exam.

(Verified) Kerem:
Tweet: I will join Dogan's birthday.

(Verified) Canberk:
Tweet: I also will join Dogan's birthday party.

------------------------------------
Revenue for this month: 32$
------------------------------------
No such user type: Special

```
