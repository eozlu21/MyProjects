# IMPORTANT NOTE 1:
For each lab assignment, **you must include and sign (by writing your name and student id number) the following Pledge of Honor statement at 
the beginning of your main method source code file. After including this statement, make sure that you do the commit and push operation on GitHub. Otherwise, 
your lab solution will not be graded.**

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

## Lab-3 Prelab: Internship performance simulation



In this programming lab, you are given a scenario and a Java project. You are asked to implement multiple classes and methods, and test the correctness of your implementation by following the instructions given in the MainTest class. Please note that we may test your codes with other test cases as well.

Scenario: Our objective is to implement an **Internship performance simulation** that keeps track of interns, their trainings, and their performance. The application has some interns and trainings and each training has a list of interns who take that training.

The project will have two packages, one of which is provided for you. You need to create another package named simulation, including Intern class, Training class, and Simulation class under it. The MainTest class is already given under the test package.

## Intern class:
Every Intern has the following private fields: 

```
- name surname of Intern (String)
- id of Intern (String)
```

- Implement three constructors: no-argument constructor, one argument constructor (you are free to chose any one field), and two-argument constructor.
- Implement getter/setter methods as needed.

## Training class:
Every Training has the following private fields:
```
- title of Training (String)
- code of Training (String)
- an ArrayList of type Intern 
      to keep the interns' information who take the corresponding Training.
```

- Implement constructor Training(String title, String code) and the needed getter/setter methods.
- You should also implement the following methods:

```
- public void appendIntern(Intern intrn): 
      to add intern information who take the training to the ArrayList of Intern class
- public ArrayList<String> getInternList(): 
      to get the name of intern who takes the training and keep them in the ArrayList
```

## Simulation class:
Each Simulation has the following fields:
```
- performance table, which should be a 2D array. 
      The table should have the size of a x b, 
      where a is the number of interns and b is the number of trainings.
- an ArrayList of type Training to keep track of the trainings.
```

### You need to 


- Implement the constructor with the signature of  Simulation (int a, int b), 
    in which a is the number of interns and b is the number of trainings. 
- Implement the needed getter and setter methods.
- Implement the following methods:



- public void appendTraining(Training trn): adds training to the ArrayList of type Training. 
- public void simulateTable(): this method sets the performance table by initializing the scores of each intern for 
   each training randomly between 10 and 100. 

    - Please note that you need to consider a constant random seed as 1500. This method should have an output similar to the table in the sample output. The table should include the name of Trainings and the name of interns, as shown in the sample output.
    - Note: Each row includes the scores of an intern, and each column includes the scores of corresponding training (see Figure 1).
    - Note: public Random(long seed) Creates a new random number generator using a single long seed. The seed is the initial value of the internal state of the pseudorandom number generator which is maintained by method next(int). We use this to get the same output as shown in the sample output.



- public void showInternPerformance(): this method should calculate the average score of 
   each intern (the average of each row) and show it as illustrated in the sample output.
- public void showTrainingLevel(): this method should calculate the average scores of the corresponding 
   training (the average of each column) and show it as given in the sample output. 
   Also, for the average values greater than 65, you need to mention that the training "is above the threshold" and for 
   the rest, “is under the threshold”. Please check the sample output.


![matrix-1](https://files.catbox.moe/7k2dyq.jpg)
                                                             Figure 1
                                                             
## MainTest class:

In this class, you need to:
- Create seven Intern objects with the names and surnames: 
     Eda Yilmaz, Ali Korkmaz, Burak Hasan, Can Kuyucu, Ege Argun, Burcu Celebi, and Seyma Ece.
    - Note 1: While creating the objects, you should demonstrate the use all the constructors that are defined in the Intern class. 
    - Note 2: You are free to determine the ID yourself.
- Create five objects of type Training class, named as, Math, Java, Python, ML, and DS.
    - Note: You are free to determine the Code yourself.
- Add all the interns to all the trainings. 
- Create an object of Simulation class with the size of a x b, where a is the number of 
    interns(the number of rows) and b implies the number of trainings (the number of columns.)
- Add all the trainings to the simulation object.
- Call the simulateTable() method that fills in and displays the table. 
- Call the showInternPerformance() method that finds and displays the performance of interns as shown in the sample output.
- Call the showTrainingLevel() method that finds and displays the level of each training as shown in the sample output.

## Sample output

```
Name           Math  Java  Python  ML  DS   
---------------------------------------------
Eda Yilmaz    | 94  | 92  | 26  | 89  | 50 | 

Ali Korkmaz   | 51  | 77  | 22  | 76  | 72 | 

Burak Hasan   | 18  | 83  | 59  | 92  | 54 | 

Can Kuyucu    | 41  | 75  | 95  | 61  | 90 | 

Ege Argun     | 63  | 32  | 61  | 23  | 85 | 

Burcu Celebi  | 78  | 52  | 35  | 71  | 96 | 

Seyma Ece     | 23  | 95  | 93  | 84  | 64 | 

------------------------ Interns performance ---------------------------------

Eda Yilmaz  has the Average score of  70.0

Ali Korkmaz  has the Average score of  59.0

Burak Hasan  has the Average score of  61.0

Can Kuyucu  has the Average score of  72.0

Ege Argun  has the Average score of  52.0

Burcu Celebi  has the Average score of  66.0

Seyma Ece  has the Average score of  71.0

------------------------ Trainings performance ---------------------------------

The average of  Math  is 52.0, then, its level is below the threshold.
The average of  Java  is 72.0, then, its level is above the threshold.
The average of  Python  is 55.0, then, its level is below the threshold.
The average of  ML  is 70.0, then, its level is above the threshold.
The average of  DS  is 73.0, then, its level is above the threshold.

```


