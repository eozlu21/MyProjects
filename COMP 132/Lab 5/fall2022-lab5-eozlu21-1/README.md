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

INLAB QUESTIONS WILL BE ANNOUNCED AT COURSE WEBSITE AT THE START OF EACH LAB: [https://sites.google.com/a/ku.edu.tr/comp132/programming-labs](https://sites.google.com/a/ku.edu.tr/comp132/programming-labs)

# Lab-5 Prelab: Star Wars 

In this programming lab, you are given a scenario and a Java template project. You are asked to implement multiple classes and methods and test the correctness of your implementation by following the instructions given in the TestMain class. The main concepts in this lab are **polymorphism** related which you will practice in this assignment. The project includes two packages (starWar and test), the TestMain class is given to you in the template project. You need to implement the other types (e.g., class, superclass, subclass, abstract class, and interface) in the starWar package. Please note that we may test your codes with other test cases as well.


Scenario: You are asked to implement a type hierarchy for a Game that is inspired by Star Wars. In the following, there are some general definitions and concepts which are helpful in understanding the whole story.


In the Star Wars universe, there is a concept called “force,” which is essentially the energy all living beings have. The force has 2 main sides: DARK SIDE and LIGHT SIDE. The ones who can control the force are called “Force Wielders”, and if a Force Wielder is using DARK SIDE, it is called “Sith”, and if s/he is using LIGHT SIDE it is called “Jedi”. Also, Jedis and Siths use weapons called “lightsabers”. Sith lightsabers always have RED color, whereas Jedi lightsabers have a different variety of colors, but these colors are mainly “BLUE, GREEN, PURPLE”. 


For the sake of simplicity, we will divide “Jedi”s into 2 groups called: Knight and Padawan. Padawan can be considered as a student, and Knight is the teacher. Both Knight and Padawan have a unique force ability to use.

“Sith”s are also divided into 2 main groups called: Master and Apprentice. As it can be understood from the names, Master is the teacher, and Apprentice is the student. Both Master and Apprentice have a unique force ability to use.

Jedis and Siths are enemies, and they fight with each other using their lightsabers or use their force abilities to change the outcome of the fight.


Figure 1 shows the Inheritance hierarchy diagram, which can help you to understand the relations between classes. 

![matrix-1](https://files.catbox.moe/bm1ok9.png)

                                        Fig1. Inheritance hierarchy diagram


## ForceWielder class:
This class is a general class (determine its type according to the description below and the concepts covered in the lectures) which has the following fields:
  - A type String which is the name of the force wielder,
  - A type int, which is the count of the battles that the wielder engaged in.
  - A type double, which is the health of the wielder
  - A type double, which is the amount of damage that the wielder’s lightsaber deals to an enemy.
  
You are asked to implement the following methods:

  - A constructor with parameters for all instance variables.
  - Corresponding getters/setters for every instance variable.
  - An abstract method named totalCredits with no parameters and return type.
  - A toString method to display the information of the entity. 

## Jedi class:
Jedi class contains the following fields:

  - A type String that specifies the color of the lightsaber a Jedi uses,
  - A type int, which will store total credits gained by the Jedi.
  - A type double, which is the amount of healing (forceHealAmount) to be given to a comrade which is always equal to double of the amount of damage that the lightsaber deals. The entities can heal each other with this item.

You are asked to implement the following methods:

  - A constructor with all parameters, including the superclass parameters
  - Getters/setters for every instance variable
  - A toString method to display the information of the entity.
  - public void totalCredits():  
  
  Since all Jedi objects are also ForceWielder objects, Jedi class should implement this method. In this method, First set the amount of credits to 310, then if the Jedi has engaged in a battle, add 15 more for each battle they engaged.


- public void saberFight(Sith s) method which:

  - First increments Jedi's engaged battle count. 
  - Then, if the health of the Sith is more than zero, the method will display "The Jedi “Jedi name” produced a damage worth of “damage of the Jedi’s lightsaber” against the Sith" “sith name.” 
  - Also, increase the amount of damage of the Jedi’s lightsaber, and decrease the amount of damage of the Sith’s lightsaber. 
  - Moreover, decrease the Health of Sith by 10.
  - If the health of the Jedi is zero or less, the method will display "The Jedi “Jedi name” has been defeated by the Sith" “sith name”.
  - In other cases, the method will display "The Jedi “Jedi name” defeated the Sith" “sith name”.

### Note: Each fight increases the amount of damage that the attacker’s lightsaber by 10 and decreases the amount of damage that the being attacked entity’s lightsaber by 10.

   
- public void revealLightsaber() method, which will act as follows:

  - If the color of the Jedi's lightsaber is blue, the method will display "Color generated from the lightsaber is purple."
  - If the color of the Jedi's lightsaber is green, the method will display "Color generated from the lightsaber is yellow."
  - If the color of the Jedi's lightsaber is magenta, the method will display "Color generated from the lightsaber is magenta."
  - In the case of other colors, the method will display "An Unknown color has been generated from the lightsaber."

## Sith class:
Sith class contains the following fields:

- A type String that specifies the color of the lightsaber a Sith uses. This variable must not be able to be changed.
- A type int, which will store total credits gained by the Sith.

You are asked to implement the following methods:

- A constructor with needed parameters.
- Initialize the color of its lightsaber to “red.”
- Getters/setters for every instance variable
- A toString method to display the information of the entity.
- public void totalCredits(): 
 
Since all Sith objects are also ForceWielder objects, Sith class should implement this method. In this method, first set the amount of credits to 310, then if the Sith has engaged in a battle, add 15 more for each battle they engaged.

- public void saberFight(Jedi j)  method which:

  - First increments Sith’s battlesEngaged. 
  - Then,  if the health of the Jedi is more than zero, the method will display "The Sith “sith name” produced a damage worth “damage of the Sith’s lightsaber” against the Jedi" “Jedi name.”  
  - Also, increase the amount of the damage of the Sith’s lightsaber, and decrease the amount of damage of the Jedi’s lightsaber.
  - Moreover, decrease the Health of Jedi by 10.
  - If the health of the Sith is zero or less,  the method will display "The Sith “sith name” has been defeated by the Jedi" “Jedi name”
  - In other cases, the method will display "The Sith “sith name” defeated the Jedi" “Jedi name”

### Note: Each fight increases the amount of damage that the attacker’s lightsaber by 10 and decreases the amount of damage that the being attacked entity’s lightsaber by 10.

## Knight class:
Knight class contains the following fields:

- A Padawan which the Knight teaches to.
- A type String, which is the name of a force ability and cannot be changed afterwards.

You are asked to implement the following methods:

- A constructor with needed parameters.
  Inside the constructor, Set the the name of the force ability to “Force Heal”.
- Corresponding getters and setters
- A toString method to display the information of the entity.
- healPadawan() method:
  - In this method, if the health of the Padawan is not 0, it increases the health of the padawan with the amount of forceHealAmount.

## Padawan class:
Padawan class contains the following fields:

- A Knight which the Padawan learns from.
- A type String, which is the name of a force ability and cannot be changed afterwards.

You are asked to implement the following methods:

- A constructor with needed parameters.
- Inside the constructor, set  the forceAbilityName to “Jedi Mind Trick.”
- Corresponding getters and setters 
- A toString method to display the information of the entity.
- confuseSith(Sith s): 

  - In this method, if the health of the Sith is not 0, it decreases the amount of lightsaberDamage of the Sith by 20%. 

- healKnight():  

  - This method asks for forceHeal if the health of the Knight is not zero, it increases the health of the Padawan with the amount of forceHealAmount. 
  - Then, displays the health amount of the Padawan.


## Master class:
Master class contains the following fields:

- An Apprentice which the Master teaches to.
- A type String, which is the name of a force ability and cannot be changed afterward.

You are asked to implement the following methods:

- A constructor with needed parameters.
- Inside the constructor, equalize the forceAbilityName to “Force Lightning.”
- Corresponding getters and setters
- A toString method to display the information of the entity.
- shockJedi(Jedi j): 

  - In this method, if the health of Jedi is not 0, decrease the health of the Jedi by 20%.
  - Afterward, decrease it with an additional 50% of by the damage that the master’s lightsaber deals.


## Apprentice class:
The Apprentice class contains the following fields:

- A Master which the Apprentice learns from.
- A type String, which is the name of a force ability and cannot be changed afterward.

You are asked to implement the following methods:

- A constructor with needed parameters.
- Inside the constructor, equalize the forceAbilityName to “Force Choke.”
- Corresponding getters and setters
- A toString method to display the information of the entity.
- chokeJedi(Jedi j): 

  - In this method, if the health of the Jedi is not 0, decrease the health of the Jedi by 50%. 
  - Afterward, decrease the health of the Jedi by the damage that the apprentice’s lightsaber deals. 

- betrayMaster(): 

  - In this method, if the health of the master is below 10% of his starting health, betray the master (set its health to 0). 
  - After betraying, set the health of the apprentice to 100. 

## Healable Interface:

An interface with the method called heal(), which Jedi and Sith use to heal themselves, meaning it increments the amount of health of a Jedi or Sith. A Jedi that uses this method will heal by 150 points. A Sith that uses this method will heal by 100 points.


## Sample output

```
-------------------------information--------------------------------
Jedi Name: Yoda 
   Number of battles engaged: 30 
   Health: 100.0 
   Damage of Lightsaber: 40.0

Knight Jedi Name: Obi-Wan Kenobi 
   Number of battles engaged: 12 
   Health: 100.0 
   Damage of Lightsaber: 25.0

Padawan Jedi Name: Anakin Skywalker 
   Number of battles engaged: 5 
   Health: 0.0 
   Damage of Lightsaber: 20.0

Name: Kont Dooku 
   Number of battles engaged: 20 
   Health: 150.0 
   Damage of Lightsaber: 20.0

Master Name: Darth Sidious 
   Number of battles engaged: 40 
   Health: 200.0 
   Damage of Lightsaber: 30.0

Apprentice Name: Darth Maul 
   Number of battles engaged: 15 
   Health: 175.0 
   Damage of Lightsaber: 25.0

--------------------------------------------------------------------
Color generated from saber clash is yellow
--------------------------------------------------------------------
The Jedi Yoda produced a damage worth 40.0 against the Sith Kont Dooku
The Sith Kont Dooku produced a damage worth 20.0 against the Jedi Yoda
--------------------------------------------------------------------
Color generated from saber clash is purple
Color generated from saber clash is purple
--------------------------------------------------------------------
Jedi Name: Yoda 
   Number of battles engaged: 31 
   Health: 500.0 
   Damage of Lightsaber: 40.0

Knight Jedi Name: Obi-Wan Kenobi 
   Number of battles engaged: 12 
   Health: 30.0 
   Damage of Lightsaber: 25.0

Padawan Jedi Name: Anakin Skywalker 
   Number of battles engaged: 5 
   Health: 0.0 
   Damage of Lightsaber: 20.0

Name: Kont Dooku 
   Number of battles engaged: 21 
   Health: 110.0 
   Damage of Lightsaber: 20.0

Master Name: Darth Sidious 
   Number of battles engaged: 40 
   Health: 200.0 
   Damage of Lightsaber: 30.0

Apprentice Name: Darth Maul 
   Number of battles engaged: 15 
   Health: 175.0 
   Damage of Lightsaber: 20.0

```


