# Generators

### A generator is, simply put, a way to access one part of a whole at a time.

## How does it help us?

### Generator lets us access parts of a collection instead of accessing the whole collection and unpacking it ourselves.

## When it comes to generators, we have:
* Generator functions
* Generator expression / Generator objects

## Generator functions:
### Any function in python containing a 'yield' keyword automatically becomes a generator function. 

Whenever a yield keyword is encountered while execution, the next element is returned from the object.
The function stops at this line and while resume from here only when called again.
This is how yield differs from return keyword - return will completely exit from the function, while yield marks a point to resume from when function gets called again.

The iter() and next() dunder methods, as well as raising of StopIteration Error are automatically added to the function when yield is mentioned
