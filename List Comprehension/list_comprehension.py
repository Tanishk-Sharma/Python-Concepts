# Lets have a list of Natural numbers initialized upto 10
list_of_natural_numbers_initialized = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('A list initialized with elements: ', list_of_natural_numbers_initialized)

# Now, let us create the same list using list comprehension:
list_of_natural_numbers_comprehension = [natural_number for natural_number in range(11)]

print('A list created with list comprehension: ', list_of_natural_numbers_comprehension)

# Let us try to create a list of only even natural numbers from the list_of_natural_numbers_initialized:
list_of_natural_even_numbers_comprehension = [natural_number for natural_number in list_of_natural_numbers_initialized if natural_number%2==0]

print('A list of Natural even numbers created with list comprehension: ', list_of_natural_even_numbers_comprehension)

# Let us try to create a list of squares of natural numbers from the list_of_natural_numbers_initialized:
list_of_squared_natural_numbers_comprehension = [natural_number**2 for natural_number in list_of_natural_numbers_initialized]

print('A list of squared Natural numbers created with list comprehension: ', list_of_squared_natural_numbers_comprehension)
