
#Q1
from unittest import result
from numpy import append


def reshape(my_tuple):
    total_result = 1
    new_tuple = (my_tuple[0], )
    for index in range(1,len(my_tuple)):
        total_result *= my_tuple[index]
    new_tuple += (total_result, )
    return new_tuple
#Q2
def replace(l):
    n = 0
    for tuple in l:
        new_tuple = ()
        for element in tuple[:len(tuple) - 1]:
            new_tuple += (element, )
        new_tuple += (tuple[0], )
        l[n] = new_tuple
        n += 1
    return l
#Q3
books = ["Chem","Physics","Writing","Programming","Math"]
def next_to_read():
    global books
    new_stack_of_books = ()
    new_stack_of_books += (books[len(books) - 1], )
    new_stack_of_books += (books[:len(books) - 1], )
    books = books[:len(books) - 1]
    return new_stack_of_books
#Q4
def merge_list(list1, list2):
    new_list = []
    for index in range(len(list1)):
        new_list.append(list1[index])
        new_list.append(list2[index])
    return new_list
#Q5
def minibatch(data_list, batch_size):
    batch_numbers = len(data_list) // batch_size
    result_list = []
    for batch in range(batch_numbers):
        new_list = []
        for i in range(batch_size):
            new_list.append(data_list[4*batch + i])
        result_list.append(new_list)
    return result_list
#Q6
def circular_check(l1,l2):
    if len(l1) != len(l2):
        return False
    l1_comp = l1 + l1
    l2_comp = l2 + l2
    for i1 in range(len(l1)):
        for i2 in range(len(l2)):
            if l1_comp[i1:i1 + len(l1)] == l2_comp[i2:i2 + len(l2)]:
                return True
    return False