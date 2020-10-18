list_of_any_numbers = [7, 1, 5, 9, 8]
g = (i**2 for i in list_of_any_numbers)  # generator expression
print(next(g))         # -> 49
print(next(g))         # -> 1
print(next(g))         # -> 25
print(next(g))         # -> 81
print(next(g))         # -> 64
