# Lets have a list of Natural numbers upto 10
list_of_natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# As list is a Collection, it can be iterated using an Iterator object:
natural_numbers_iterator = iter(list_of_natural_numbers)

# Lets print the elements of the collection (List) using the iterator object and its method - next(ele)
print(next(s))      # -> 1
print(next(s))      # -> 2
print(next(s))      # -> 3
print(next(s))      # -> 4
print(next(s))      # -> 5
print(next(s))      # -> 6
print(next(s))      # -> 7
print(next(s))      # -> 8
print(next(s))      # -> 9
print(next(s))      # -> 10
print(next(s))      # -> We have exhausted out list hence, at this point the program will raise the 'StopIteration Error'
