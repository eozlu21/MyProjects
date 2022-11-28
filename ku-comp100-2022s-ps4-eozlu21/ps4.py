class Powers:
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
              'Psydrive': 120,
              'Crushing Blow': 80,
              'Ultra-Toxic Fang': 40,
              'Breaker Bazooka': 100,
              'Blue Flare': 120,
              'Cold Crush': 70,
              'Tail Whap': 30,

              "Absorb": 20,
              "Acid": 40,
              "Aurora Beam": 65,
              "Barrage": 15,
              "Bind": 15,
              "Bite": 60,
              "Blizzard": 110,
              "Body Slam": 85,
              "Bone Club": 65,
              "Bonemerang": 50,
              "Bubble": 40,
              "Bubble Beam": 65,
              "Clamp": 35,
              "Comet Punch": 18,
              "Confusion": 50,
              "Constrict": 10,
              "Crabhammer": 100,
              "Cut": 50,
              "Dig": 80,
              "Dizzy Punch": 70,
              "Double Kick": 30,
              "Double Slap": 15,
              "Double Edge": 120,
              "Dream Eater": 100,
              "Drill Peck": 80,
              "Earthquake": 100,
              "Egg Bomb": 100,
              "Ember": 40,
              "Explosion": 250,
              "Fire Blast": 110,
              "Fire Punch": 75,
              "Fire Spin": 35,
              "Flamethrower": 90,
              "Fly": 90,
              "Fury Attack": 15,
              "Fury Swipes": 18,
              "Gust": 40,
              "Headbutt": 70,
              "High Jump Kick": 130,
              "Horn Attack": 65,
              "Hydro Pump": 110,
              "Hyper Beam": 150,
              "Hyper Fang": 80,
              "Ice Beam": 90,
              "Ice Punch": 75,
              "Jump Kick": 100,
              "Karate Chop": 50,
              "Leech Life": 80,
              "Lick": 30,
              "Mega Drain": 40,
              "Mega Kick": 120,
              "Mega Punch": 80,
              "Pay Day": 40,
              "Peck": 35,
              "Petal Dance": 120,
              "Pin Missile": 25,
              "Poison Sting": 15,
              "Pound": 40,
              "Psybeam": 65,
              "Psychic": 90,
              "Rage": 20,
              "Razor Leaf": 55,
              "Razor Wind": 80,
              "Rock Slide": 75,
              "Rock Throw": 50,
              "Rolling Kick": 60,
              "Scratch": 40,
              "Self Destruct": 200,
              "Skull Bash": 130,
              "Sky Attack": 140,
              "Slam": 80,
              "Slash": 70,
              "Sludge": 65,
              "Smog": 30,
              "Solar Beam": 120,
              "Spike Cannon": 20,
              "Stomp": 65,
              "Strength": 80,
              "Struggle": 50,
              "Submission": 80,
              "Surf": 90,
              "Swift": 60,
              "Tackle": 40,
              "Take Down": 90,
              "Thrash": 120,
              "Thunder": 110,
              "Thunder Punch": 75,
              "Thunder Shock": 40,
              "Thunderbolt": 90,
              "Tri Attack": 80,
              "Twineedle": 25,
              "Vine Whip": 45,
              "Vise Grip": 55,
              "Water Gun": 40,
              "Waterfall": 80,
              "Wing Attack": 60,
              "Wrap": 15,

              }

  def __init__(self):
    self.powers = {}
  def add_power(self, new_power, all_powers = all_powers):
    if new_power not in self.powers:
      self.powers[new_power] = all_powers[new_power]
  def get_total_damage(self):
    if len(self.powers) > 0:
      return sum(self.powers.values())
    else:
      return 0

class Pokemon:
  def __init__(self,name, energy_type, cost, hp, weakness = (None , 1), powers = None,num_wins = 0, taken = False):
      self.name = name
      self.cost = cost
      self.hp = hp
      self.energy_type = energy_type
      self.num_wins = num_wins
      self.taken = taken
      if powers == None:
        powers = Powers()
      self.powers = powers
      self.weakness = weakness
  def __str__(self) -> str:
      return "name: " + self.get_name() + ", hp: " + str(self.get_hp()) + ", num_wins:  " + str(self.get_num_wins()) + ", taken: "
  def get_name(self):
    return self.name
  def set_name(self,name_to_set):
    self.name = name_to_set
  def get_energy_type(self):
    return self.energy_type
  def set_energy_type(self, energy_to_set):
    self.energy_type = energy_to_set
  def get_weakness(self):
    return self.weakness
  def set_weakness(self,weakness_to_set):
    self.weakness = weakness_to_set
  def receive_damage(self, damage, opponent_energy_type = None):
    if opponent_energy_type == self.weakness[0]:
      damage *= self.weakness[1]
    self.hp -= damage
  def get_hp(self):
    if self.hp > 0:
      return self.hp
    else:
      return "is defeated"
  def set_hp(self, hp_to_set):
    self.hp = hp_to_set
  def is_healthy(self):
    return self.hp > 0
  def add_power(self,power_to_add):
    self.powers.add_power(power_to_add)
  def make_attack(self):
    if len(self.powers.powers) > 0:
      return sum(self.powers.powers.values())
    else:
      return 0
  def get_powers(self):
    return self.powers
  def battle_step(self, enemy_pokemon):
    enemy_pokemon.receive_damage(self.make_attack(), self.get_energy_type())
    self.receive_damage(enemy_pokemon.make_attack(), enemy_pokemon.get_energy_type())
  def battle(self, enemy_pokemon):
    while enemy_pokemon.is_healthy() and self.is_healthy():
      self.battle_step(enemy_pokemon)
    if not (enemy_pokemon.is_healthy() or self.is_healthy()):
      #draw
      pass
    elif self.is_healthy():
      self.num_wins += 1
    else:
      enemy_pokemon.num_wins += 1
  def get_num_wins(self):
    return self.num_wins
  def get_taken(self):
    return self.taken


class EvolvedPokemon(Pokemon):
  def __init__(self, name, energy_type, cost, hp, weakness=(None, 1), damage_reducer = 0, damage_booster = 0, num_wins=0, powers=None):
      super().__init__(name, energy_type, cost, hp, weakness, powers, num_wins)
      self.damage_reducer = damage_reducer
      self.damage_booster = damage_booster
      if powers is None:
        powers = Powers()
      self.powers = powers
  def make_attack(self):
      return super().make_attack() + self.damage_booster
  def receive_damage(self, damage, opponent_energy_type = None):
    if opponent_energy_type == self.weakness[0]:
      damage *= self.weakness[1]
    self.hp -= (damage - self.damage_reducer)
  def get_damage_booster(self):
    return self.damage_booster
  def get_damage_reducer(self):
    return self.damage_reducer
  def set_damage_booster(self, new_damage_booster):
    self.damage_booster = new_damage_booster
  def set_damage_reducer(self, new_damage_reducer):
    self.damage_reducer = new_damage_reducer
    

      

class Trainer:
  def __init__(self,name, xp):
    self.name = name
    self.xp = xp
    self.pokemons = []
  def add_pokemon(self, new_pokemon):
    if not new_pokemon.taken and self.xp >= new_pokemon.cost:
      self.xp -= new_pokemon.cost
      new_pokemon.taken = True
      self.pokemons.append(new_pokemon)
    elif self.xp < new_pokemon.cost:
      print(self.name + " does not have enough xp to get " + new_pokemon.name + "! " + self.name + " has only " + str(self.xp) + " xp.") 
  def are_all_defeated(self):
    return_bool = True
    if not self.pokemons == []:
      for pokemon in self.pokemons:
        if pokemon.hp > 0:
          return_bool = False
          break
    return return_bool
  def fight(self, enemy_trainer):
    while not self.are_all_defeated() and not enemy_trainer.are_all_defeated():
      pokemon1 = self.pokemons[0]
      pokemon2 = enemy_trainer.pokemons[0]
      pokemon1.battle(pokemon2)
      if not pokemon1.is_healthy():
          self.pokemons.remove(pokemon1)
      if not pokemon2.is_healthy():
        enemy_trainer.pokemons.remove(pokemon2)
    if self.are_all_defeated():
      print(enemy_trainer.name + " wins the fight!")
    elif enemy_trainer.are_all_defeated():
      print(self.name + " wins the fight!")
    



if __name__ == '__main__':
  pikachu = Pokemon(name='pikachu', energy_type='Lightning', cost=100, hp=60, weakness=('Fighting', 2))
  pikachu.add_power('Quick Attack')
  pikachu.add_power('Electro Ball')

  raichu = EvolvedPokemon('Raichu', 'Lightning', 800, 90, weakness=('Fighting', 2), damage_booster=30, damage_reducer=0)
  raichu.add_power('Quick Attack')
  raichu.add_power('Electro Ball')

  meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic', 2))
  meloetta.add_power('Smack')
  meloetta.add_power('Acrobatics')

  landorus = EvolvedPokemon('Landorus', 'Fighting', 400, 110, ('Psychic', 2), 20, 20)
  landorus.add_power('Smack')
  landorus.add_power('Acrobatics')

  # create a trainer
  ash = Trainer('Ash', 200)

  # add some pokemon to ash
  ash.add_pokemon(pikachu)
  ash.add_pokemon(raichu)  # Should print "Ash does not have enough xp to get Raichu! Ash has only 100 xp."

  # create another
  gary = Trainer('Gary', 1000)

  # add some pokemon to gary
  gary.add_pokemon(landorus)

  ash.fight(gary)  # Should print "Gary wins the fight!"