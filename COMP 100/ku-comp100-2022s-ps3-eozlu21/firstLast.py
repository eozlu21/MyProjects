import copy
from words import long_word_list, short_word_list
import time

def longest_sequence(beginning_word, selected_word_list:list):
  # your code here
  def valid_word_list(word_to_check, word_list):
    """Takes a single word as a string to check its first letter, returns all possible words as a list as output."""
    output_list = []
    for word in word_list:
        if word_to_check[-1] == word[0]:
            output_list.append(word)
    return output_list
  

  def sequence_creator(current_sequences):
    new_outer_sequence = []
    continue_bool = False
    for list1 in current_sequences:
      new_inner_sequence = []
      reference_selected_word_list = selected_word_list[:]
      for word1 in list1:
        if word1 in selected_word_list:
          reference_selected_word_list.remove(word1)
      words_to_add = valid_word_list(list1[-1],reference_selected_word_list)
      if words_to_add == []:
        continue
      for word2 in words_to_add:
        continue_bool = True
        new_inner_sequence.append(list1 + [word2]) 
      new_outer_sequence.extend(new_inner_sequence)
    if not continue_bool:
      return current_sequences
    else:
      return sequence_creator(new_outer_sequence)
    

  all_sequences1 = sequence_creator([[beginning_word]])
  longest_sequence1 = max(all_sequences1, key = len)
  return len(longest_sequence1), longest_sequence1
    
        
def convert_to_dict(selected_word_list):
  # your code here
  output_dict = {}
  for word in selected_word_list:
    output_dict[word[0]] = output_dict.get(word[0],[]) + [word]
  return output_dict

def longest_sequence_fast(beginning_word, selected_word_dict:dict):
  # your code here
  def sequence_creator(current_sequences):
    new_outer_sequence = []
    continue_bool = False
    for list1 in current_sequences:
      new_inner_sequence = []
      new_word_dict = {}
      for word1 in list1:
        if word1 in selected_word_dict[word1[0]]:
          if new_word_dict.get(word1[0], []) == []:
            new_word_dict[word1[0]] = [n for n in selected_word_dict[word1[0]] if n!= word1]
          if word1 in new_word_dict[word1[0]]:
            new_word_dict[word1[0]].remove(word1)
      for letter in selected_word_dict.keys():
        new_word_dict[letter] = new_word_dict.get(letter, selected_word_dict[letter])
      words_to_add = new_word_dict.get(word1[-1], [])
      if words_to_add == []:
        continue
      for word2 in words_to_add:
        continue_bool = True
        new_inner_sequence.append(list1 + [word2]) 
      new_outer_sequence.extend(new_inner_sequence)
    if not continue_bool:
      return current_sequences
    else:
      return sequence_creator(new_outer_sequence)
    

  all_sequences2 = sequence_creator([[beginning_word]])
  longest_sequence2 = max(all_sequences2, key = len)
  return len(longest_sequence2), longest_sequence2
  


if __name__ == "__main__":
  mode = int(input("Game mode (1 for short, 2 for long): "))
  assert mode in [1,2], "Invalid game mode"

  if mode == 1:
      vocab = short_word_list
  else:
      vocab = long_word_list

  starter_word = input("Enter starter word: ").strip()

  #part 1
  start = time.time()
  max_length1, seq1 = longest_sequence(starter_word, vocab) # pass your arguments in ...
  print(max_length1)
  print(seq1)
  end= time.time()
  print(round(end-start, 5), "seconds passed on method 1") 

  # part 2
  start = time.time()
  vocab_dict = convert_to_dict(vocab)
  max_length2, seq2  = longest_sequence_fast(starter_word, vocab_dict) # pass your arguments in ...
  print(max_length2)
  print(seq2)
  end= time.time()
  print(round(end-start, 5), "seconds passed on method 2") 

  assert max_length1 == max_length2 and seq1 == seq2, "result mismatch"

  # It is shortened by more than half, since it doesn't need to 
  # compile the list of all words that start with a certain letter everytime.
  # Since the increase in the time is exponential, eliminating a single action greatly reduces the time required.
