# Lets have a list of Natural numbers upto 10
list_of_natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# As list is a Collection, it can be iterated using an Iterator object:
natural_numbers_iterator = iter(list_of_natural_numbers)

# Lets print the elements of the collection (List) using the iterator object and its method - next(ele)
print(next(natural_numbers_iterator))      # -> 1
print(next(natural_numbers_iterator))      # -> 2
print(next(natural_numbers_iterator))      # -> 3
print(next(natural_numbers_iterator))      # -> 4
print(next(natural_numbers_iterator))      # -> 5
print(next(natural_numbers_iterator))      # -> 6
print(next(natural_numbers_iterator))      # -> 7
print(next(natural_numbers_iterator))      # -> 8
print(next(natural_numbers_iterator))      # -> 9
print(next(natural_numbers_iterator))      # -> 10
print(next(natural_numbers_iterator))      # -> We have exhausted out list hence, at this point the program will raise the 'StopIteration Error'
