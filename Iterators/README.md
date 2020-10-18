# Iterators

### Iterators are used to traverse or 'iterate' through a collection in Python.
We can create an iterator object using the iter keyword on the collection.
For example, 
my_iterator__obj = iter(my_list)

### Collections in Python:
* Lists
* Tuples
* Array
* Sets
* Dictionaries

### Using the iterator object, we can only access one element of the collection at a time and only in one sequence.

## Program Output:
<img src="https://user-images.githubusercontent.com/32167236/96369114-b296b880-1175-11eb-8240-f2a3c0491caf.png">

## Under the hood

Under the hood, the iterator object simply accesses the dunder methods '<b>iter()</b>' and '<b>next()</b>' defined inside the class and raises a StopIteration when there are no values to be returned.
We can also create our own class implementing the dunder methods '<b>iter()</b>' and '<b>next()</b>' and can access its elements using an iterator object!
