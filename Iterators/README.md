# Iterators

### Iterators are used to traverse or 'iterate' through a collection in Python.

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

Under the hood, the iterator object simply accesses the '<b>__iter__()</b>' and '<b>__next__()</b>' method defined inside the class and raises a StopIteration when there are no values to be returned.
We can also create our own class implementing the '<b>__iter__()</b>' and '<b>__next__()</b>' methods and can access its elements using an iterator object!
