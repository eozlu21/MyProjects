from ps4 import Pokemon, Powers, EvolvedPokemon, Trainer
# Pokemon(name, energy_type, cost, hp, weakness=(None, 1))
def test_p1_1():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  assert pikachu.get_name() == 'Pikachu'
  print("Passed test 1.1")

def test_p1_2():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  pikachu.set_name('JigglyPuff')
  assert pikachu.get_name() == 'JigglyPuff'
  print("Passed test 1.2")

def test_p1_3():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  assert pikachu.get_energy_type() == 'Lightning'
  print("Passed test 1.3")

def test_p1_4():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  pikachu.set_energy_type('Water')
  assert pikachu.get_energy_type() == 'Water'
  print("Passed test 1.4")

def test_p1_5():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  assert pikachu.get_weakness() == ('Water',2)
  print("Passed test 1.5")

def test_p1_6():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  pikachu.set_weakness(('Grass', 2))
  assert pikachu.get_weakness() == ('Grass',2)
  print("Passed test 1.6")

def test_p1_7():
  # test receive damage
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  pikachu.receive_damage(20)
  assert pikachu.get_hp() == 40
  print("Passed test 1.7")

def test_p1_8():
  # test is healthy +
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  pikachu.receive_damage(20)
  assert pikachu.is_healthy()
  print("Passed test 1.8")

def test_p1_9():
  # test is healthy 0 or -
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water',2))
  pikachu.receive_damage(60)
  assert not pikachu.is_healthy()
  pikachu.set_hp(60)
  pikachu.receive_damage(80)
  assert not pikachu.is_healthy()
  print("Passed test 1.9")

# all_powers = {'Quick Attack': 10,
#                   'Outrage': 20,
#                   'Electro Ball': 50,
#                   'Bolt Strike': 120,
#                   'Smack': 10,
#                   'Acrobatics': 40,
#                   'Fast Punch': 60,
#                   'Extra Sensory': 20,
#                   'Rock Tomb': 90}
def test_p2_1():
  powers = Powers()
  powers.add_power('Outrage')
  powers.add_power('Quick Attack')
  assert 'Outrage' in powers.powers.keys()
  assert 'Quick Attack' in powers.powers.keys()
  assert 'Bolt Strike' not in powers.powers.keys()
  print("Passed test 2.1")

def test_p2_2():
  powers = Powers()
  powers.add_power('Outrage')
  powers.add_power('Quick Attack')
  assert powers.get_total_damage() == 30
  print("Passed test 2.2")

def test_p2_3():
  powers = Powers()
  powers.add_power('Quick Attack')
  powers.add_power('Outrage')
  powers.add_power('Bolt Strike')
  assert powers.get_total_damage() == 150
  print("Passed test 2.3")

# testing Powers in Pokemon
def test_p2_4():
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water', 2))
  assert pikachu.powers != None
  assert type(pikachu.powers) == Powers
  assert pikachu.powers == pikachu.get_powers()
  assert type(pikachu.powers.powers) == dict
  print("Passed test 2.4")

def test_p2_5(): # testing pokemon.add_power
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water', 2))
  pikachu.add_power('Quick Attack')
  pikachu.add_power('Electro Ball')
  assert pikachu.powers.powers.get('Quick Attack', 0) == 10
  assert pikachu.powers.powers.get('Electro Ball', 0) == 50
  assert pikachu.powers.powers.get('Bolt Strike', 0) == 0
  print("Passed test 2.5")

def test_p2_6(): # testing pokemon.make_attack()
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Water', 2))
  pikachu.add_power('Quick Attack')
  pikachu.add_power('Electro Ball')
  assert pikachu.make_attack() == 60
  print("Passed test 2.6")

def test_p3_1():
  raichu = EvolvedPokemon(name='Raichu', energy_type='Lightning', cost=800, hp=90, weakness=('Fighting', 2),
                          damage_booster=30, damage_reducer=0)
  assert raichu.get_damage_booster() == 30
  assert raichu.get_damage_reducer() == 0
  print("Passed test 3.1")

def test_p3_2():
  landorus = EvolvedPokemon('Landorus', 'Fighting', 400, 110, ('Psychic',2))
  landorus.set_damage_booster(20)
  landorus.set_damage_reducer(20)
  assert landorus.get_damage_reducer() == 20
  assert landorus.get_damage_reducer() == 20
  assert landorus.get_energy_type() == 'Fighting'
  assert landorus.get_weakness() == ('Psychic',2)
  print("Passed test 3.2")

def test_p3_3():
  landorus = EvolvedPokemon('Landorus', 'Fighting', 400, 110, ('Psychic', 2), 20, 20)
  landorus.add_power('Extra Sensory')
  landorus.add_power('Rock Tomb')
  assert landorus.make_attack() == 130
  landorus.receive_damage(40)
  assert landorus.get_hp() == 90 # because 110-(40-20) = 90
  print("Passed test 3.3")

def test_p4_1(): # testing battle steps, and weakness
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Fighting', 2))
  pikachu.add_power('Quick Attack')
  pikachu.add_power('Electro Ball')

  meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic', 2))
  meloetta.add_power('Smack')
  meloetta.add_power('Acrobatics')

  pikachu.battle_step(meloetta)
  assert not pikachu.is_healthy() # pikachu is defeated in one step because of his weakness to the Fighting energy of meloetta
  assert meloetta.get_hp() == 20
  print("Passed test 4.1")

def test_p4_1(): # testing battle steps, and weakness
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Fighting', 2))
  pikachu.add_power('Quick Attack')
  pikachu.add_power('Electro Ball')

  meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic', 2))
  meloetta.add_power('Smack')
  meloetta.add_power('Acrobatics')

  pikachu.battle_step(meloetta)
  assert not pikachu.is_healthy() # pikachu is defeated in one step because of his weakness to the Fighting energy of meloetta
  assert meloetta.get_hp() == 20
  print("Passed test 4.1")

def test_p4_2(): # testing battle steps, and weakness
  pikachu = Pokemon('Pikachu', 'Lightning', 100, 60, weakness=('Fighting', 2))
  pikachu.add_power('Quick Attack')
  pikachu.add_power('Electro Ball')

  meloetta = Pokemon('Meloetta', 'Fighting', 100, 80, ('Psychic', 2))
  meloetta.add_power('Smack')
  meloetta.add_power('Acrobatics')

  #print('Before the battle:')
  assert pikachu.get_hp() == 60
  assert meloetta.get_hp() == 80

  pikachu.battle(meloetta)

  #print('After the battle:')
  assert not pikachu.is_healthy()
  assert pikachu.get_num_wins() == 0
  assert meloetta.get_hp() == 20
  assert meloetta.get_num_wins() == 1
  print("Passed test 4.2")

def test_p5_1(): # testing trainer fight
  gary = Trainer('Gary', 1000)
  ash = Trainer('Ash', 1000)

  raichu = EvolvedPokemon(name='Raichu', energy_type='Lightning', cost=800, hp=90, weakness=('Fighting', 1.2),
                          damage_booster=30, damage_reducer=0)
  raichu.add_power('Quick Attack')
  raichu.add_power('Electro Ball')

  landorus = EvolvedPokemon('Landorus', 'Fighting', 400, 110, ('Psychic', 2), 20, 20)
  landorus.add_power('Extra Sensory')
  landorus.add_power('Rock Tomb')

  ash.add_pokemon(raichu)
  gary.add_pokemon(landorus)

  ash.fight(gary)

  assert landorus.get_hp() == 40
  assert landorus.get_num_wins() == 1
  assert landorus.get_taken()

  assert not raichu.is_healthy()
  assert raichu.get_num_wins() == 0
  assert raichu.get_taken()
  print("Passed test 5.1")


if __name__ == '__main__':
  test_p1_1()
  test_p1_2()
  test_p1_3()
  test_p1_4()
  test_p1_5()
  test_p1_6()
  test_p1_7()
  test_p1_8()
  test_p1_9()

  test_p2_1()
  test_p2_2()
  test_p2_3() # testing power.add_power () and power.get_total_damage()
  test_p2_4() # testing pokemon.powers(and .powers)'s types
  test_p2_5() # testing pokemon.add_power
  test_p2_6() # testing pokemon.make_attack()

  test_p3_1() # testing evolvedpokemon setters and getters
  test_p3_2() # testing evolvedpokemon setters and getters and inherited methods
  test_p3_3()  # testing evolvedpokemon override methods

  # Battling
  test_p4_1()
  
  # Trainer & Fighting
  test_p5_1()

