# PS4
## Deadline: 22.05.2022 - 23:00
 
In this problem set, you will learn how to define and use classes and inheritance. This problem set consists of three parts.
 
In each part, you will work on implementing some classes. Slowly, we will build a simulation involving a Pokemon battle between two trainers.
Each trainer will have Pokemon and their collection of powers. Let's start with a single Pokemon.

Type your class definitions in "ps4.py" file and test your solution in "test_ps4.py". 
You can start with the examples below but remember to use other test cases as well **because we will use additional test cases when we grade your work**. Later, we will provide an example test script. Feel free to look at the test_ps4.py file to understand the specifics of the tests.
 
## Part 1: Pokemon
 
First, we will implement a class called `Pokemon`. This class will have basic information about a Pokemon with some functionality.
 
### Initialization
We will represent a `Pokemon` class with a set of properties including their name, cost, health points `hp`, number of wins, powers, and energy type. Let's explain each one of them one by one:
- `name` is a string provided as an argument.
- `cost` is a numeric value representing the Pokemon's value, for example, if a trainer wants to trade them later.
- `hp` and `num_wins` are also numeric values. We will use the default value of 0 for the initial number of wins.
- `energy_type` can be one of `Grass`, `Fire`, `Water`, `Lightning`, `Psychic`, `Fighting`, `Darkness`, `Metal`, `Fairy` and `Dragon` representing the type of the Pokemon.
- `powers` will be `None` for now. We will develop it in the next part.
- `weakness` will be a tuple `(energy_type, multiplier)` that describes an energy that a Pokemon is more vulnerable to. You can default this to `(None, 1)`.
 
Use the `__init__` method for initializing corresponding data attributes by using the `self` keyword to refer to a specific instance of the `Pokemon` class. Note that `name`, `energy_type`, `cost`, `hp`, are required to create a new `Pokemon` object but all the other attributes have some default values.
 
Let's also add some procedural attributes to the `Pokemon` object:
 
0. Write getter and setter methods by using the convention that we introduced in the class, e.g. `get_name` and `set_name` for the `name` attribute.
1. Write a function called `receive_damage`. This will take as input the value of damage received by this Pokemon and decrease the hp of the Pokemon by that amount.
2. Write a function `is_healthy` to check if a Pokemon is healthy, i.e. their health level is strictly greater than zero.
 
```
# initializing instances of the Pokemon class:

# a Pokemon named "Pikachu" whose cost is 100
pikachu = Pokemon(name='pikachu', energy_type='Lightning', cost=100, hp=60, weakness=('Fighting',2))
 
# a Pokemon named "Meloetta" whose cost is also 100
meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic',2))
 
# pikachu receiving a damage of magnitude 20
pikachu.receive_damage(20)
 
# the health level of pikachu should be 40 after the attack
print(pikachu.get_hp())
 
# check if pikachu is healthy
# it should print True since health level is 40 > 0
print(pikachu.is_healthy())
```
 
## Part 2: Powers
Powers is a collection of power moves that a Pokemon can make. All possible powers and their damages are stored in a dictionary and shared across different instances of the `Powers` class:
 
```
    all_powers = {'Quick Attack': 10,
                  'Outrage': 20,
                  'Electro Ball': 50,
                  'Bolt Strike': 120,
                  'Smack': 10,
                  'Acrobatics': 40,
                  'Fast Punch': 60,
                  'Extra Sensory': 20,
                  'Rock Tomb': 90,
                  'X Ball': 20,
                  'Psydrive': 120}
```
 
**Hint:** Remember class variables?
 
The type of the power defines the amount of damage that can be caused to other Pokemon (times a weakness multiplier that will be defined later). For example, a Quick Attack can cause 10 damage to another Pokemon(with no weakness)
 
a Powers instance can have at most one of any of the powers in the `powers` dictionary, for example, a Quick Attack and an Outrage but not two Quick Attack(s) or three Outrage(s). It can be a full power dictionary by having each of these powers.
 
1. Define a function called `add_power` which takes a power name as an argument and adds it to the `powers` dictionary. If it is already in the dictionary, it does not change anything.
 
2. Define a function called `get_total_damage` to calculate the total amount of damage that can be caused by the powers in the `powers` dictionary. In order to calculate that, get separate damage values of each power in the `powers` dictionary and sum them up and return the total.
 
For example, if there is a Quick Attack and an Outrage in a `powers` dictionary, the total damage will be 30
 
```
# create a Powers object
powers = Powers()
 
# add some powers to it
powers.add_power('Quick Attack')
powers.add_power('Outrage')
powers.add_power('Bolt Strike')
 
# calculate the total damage that can be caused by the powers object
damage = powers.get_total_damage()
print(damage) # should print 150
```
 
Coming back to the `Pokemon` class, each `Pokemon` will have a `Powers` object in their internal representation.
To achieve that, do the following:
 
1. Modify the constructor such that the powers of the pokemon is initialized with an empty `Powers` object instead of `None`.
 
2. Write a function called `add_power` which takes as input a power name, one of `Quick Attack`,`Outrage`,`Bolt Strike`... etc, and adds the power to the powers of that Pokemon.

3. A Pokemon can make an attack using all their powers. Write a function called `make_attack` for the `Pokemon` object which returns the sum of damages that can be caused by all the powers that the Pokemon has.
 

Example use case:
```
# using the pikachu object defined above
# add some powers to the powers of pikachu
pikachu.add_power('Quick Attack')
pikachu.add_power('Electro Ball')
 
# check the damage that pikachu can make
pikachu_damage = pikachu.get_powers().get_total_damage()
print(pikachu_damage) # should print 60
 
# pikachu makes an attack
# this should also print 60 because the total damage is 60 for pikachu
print(pikachu.make_attack())
```
 
## Part 3: Evolved Pokemon
 
Let's extend the `Pokemon` class to have an evolved form: `EvolvedPokemon`. In that case, the pokemon can have an increased attack damage by a `damage_booster` and the received damage will be reduced by `damage_reducer`. The default values can be 0 for each. These two numeric attributes represent the `EvolvedPokemon` class. 
 
In the `EvolvedPokemon` class:

1. First implement setters and getters for these new attributes.
2. Override the methods `make_attack` and `receive_damage` of the `Pokemon` class to represent these effects, i.e. add the effect of `make_attack` by `damage_booster` and subtract the incoming `damage` by `damage_reducer`.
 
 
For example:
```
# create an EvolvedPokemon named `Raichu` whose cost is 800 and energy_type is `Ligtning`
# damage_booster is 20 and damage_reducer is 20
raichu = EvolvedPokemon(name='Raichu', energy_type='Lightning', cost=800, hp=90, weakness=('Fighting',2), damage_booster=30, damage_reducer=0)
 
# create a EvolvedPokemon named `Landorus` whose energy_type is 'Fightning', cost is 400, hp is 110, weakness is ('Psychic',2))
landorus = EvolvedPokemon('Landorus', 'Fighting', 400, 110, ('Psychic',2))
 
# set the damage_multiplier and damage_reducer with set methods
landorus.set_damage_booster(20)
landorus.set_damage_reducer(20)
 
# add some powers to landorus
landorus.add_power('Extra Sensory')
landorus.add_power('Rock Tomb')
 
# check the damage of landorus
landorus_damage = landorus.get_powers().get_total_damage()
print(landorus_damage) # should print 110
 
# when landorus makes an attack, it should be increased by the damage_booster of landorus which is 20
print(landorus.make_attack()) # will print 130
 
# when landorus receives a damage, it should be reduced by the damage_reducer of landorus which is 20
print(landorus.get_hp()) # will print 110 (initial hp)
landorus.receive_damage(50)
print(landorus.get_hp()) # will print 110 - 50 + 20 = 80
```
 
## Part 4: Battling
 
With the `make_attack` and `receive_damage` methods defined, we can now define the method for a fight between two Pokemon.
The battle between two Pokemon will continue as long as both of them have hp > 0 (**Hint:** Use `is_healthy` method of the `Pokemon` to check that.).
At each step, both pokemon will attack each other and receive damage from each other.
 
1. To implement that, first define a method `battle_step` which takes as input the opponent pokemon object. A battle step means one attack from both sides to each other which will result in damage to both sides.
 
2. Define the function `battle` which performs battle steps until at least one of the pokemon has hp <= 0. You should increase the `num_wins` of a pokemon when the other pokemon is defeated.

3. If the energy_type of the attacking pokemon is the same as the weakness of the defending pokemon, the defending pokemon will receive a damage multiplied by the weakness as specified by the defending pokemon's weakness attribute
 
4. Implement a way of printing the `Pokemon` object so that you can see the status of the pokemon, e.g. name, hp if healthy else 'defeated', number of wins and the effective damage of all powers that pokemon.

```
pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Fighting', 2))
pikachu.add_power('Quick Attack')
pikachu.add_power('Electro Ball')

meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic', 2))
meloetta.add_power('Smack')
meloetta.add_power('Acrobatics')

print('Before the battle:')
print(pikachu) # Should print "name: Pikachu, hp: 60,  num_wins: 0, taken: False"
print(meleotta) # Should print "name: Meloetta,  hp: 80,  num_wins: 0,  taken: False"

pikachu.battle(meloetta)

print('After the battle:')
print(pikachu) # Should print "name: Pikachu, hp: is defeated, num_wins: 0, taken: False"
print(meleotta) # Should print "name: Meloetta, hp: 20, num_wins: 1, taken: False 
```
 
## Part 5: Trainer
Finally, to group everything together, we create an `Trainer` object. The trainer will have variables like `name`, `xp`, and `pokemons` which is a list of `Pokemon` objects. The xp can be traded to add new pokemon to the list of pokemon. A pokemon can only be added if the trainer can afford it, i.e. the cost of the pokemon is less than the xp of the trainer.
 
1. Update the `Pokemon` class by adding a new attribute `taken` which is `False` by default and set to `True` if they are added to a trainer.
 
2. Write a method `add_pokemon` in `Trainer` class to add a `Pokemon` object to the `pokemons` list of the trainer if the pokemon is not taken by another trainer before. New Pokemon should be added to the end of the list, this will be important in the battle. Do not forget to update the xp after adding a new pokemon and setting `taken` to `True` for the pokemon added.
 
3. Write a method `are_all_defeated` to check if all trainer's pokemon are defeated.
 
4. Write a method `fight` that stages a fight between a pokemon from each trainer one by one until at least one trainer's pokemon are all defeated. We will use the adding order of the pokemon like a queue, i.e. first added pokemon will battle first. Please assume that each pokemon will battle until they are defeated and the surviving pokemon will continue fighting the next pokemon from the other trainer. The first trainer whose pokemons are all defeated loses the fight. Print the winning trainer as the result of the fight. Do not forget to remove the defeated pokemon from the trainer's pokemons list.
 
For example:
```
pikachu = Pokemon(name='pikachu', energy_type='Lightning', cost=100, hp=60, weakness=('Fighting',2))
pikachu.add_power('Quick Attack')
pikachu.add_power('Electro Ball')

raichu = EvolvedPokemon(name='Raichu', energy_type='Lightning', cost=800, hp=90, weakness=('Fighting',2), damage_booster=30, damage_reducer=0)
raichu.add_power('Quick Attack')
raichu.add_power('Electro Ball')

meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic',2))
meloetta.add_power('Smack')
meloetta.add_power('Acrobatics')

landorus = EvolvedPokemon('Landorus', 'Fighting', 400, 110, ('Psychic',2), 20, 20)
landorus.add_power('Smack')
landorus.add_power('Acrobatics')


# create a trainer
ash = Trainer('Ash', 200)
 
# add some pokemon to ash
ash.add_pokemon(pikachu)
ash.add_pokemon(raichu) # Should print "Ash does not have enough xp to get Raichu! Ash has only 100 xp.""
 
# create another
gary = Trainer('Gary', 1000)
 
# add some pokemon to gary
gary.add_pokemon(landorus)

ash.fight(gary) # Should print # Should print "Gary wins the fight!"

```