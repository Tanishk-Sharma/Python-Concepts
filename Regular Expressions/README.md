# Regular Expressions AKA regex

Regular expressions are an algebraic way of representing a certain text.
Algebraic, because regex do have pre-defined rules to express the pattern of text we are looking for.

Using the pattern defined by a regex, we can do many powerful operations which would otherwise be very tedious.

This is a very big advantage of regex - simplify the text operations like:
* Filtering (Searching)
* Extracting
* Replacing
* Portable

Note: Regex are not specific to Python! They are a subject of their own. However, Python provides the wonderful library: 're' to harness the power of regex :)

## Program

While there are multiple methods that re module provides, some of them are:
compile()
search()
findall()
sub()
split()

In our program, we have a sample string that has a lot of text, but the important stuff is the email addresses.
Imagine a string of size of hundreds or even thousands of lines, and we want only the email addresses from it. Manual copy paste is an option, but not a smart one :)
re to the rescue. 

In our program here, we have made an algebraic way, or a rule-based way to represent a typical email address like:

<b>r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]{3}'</b>

Let's break it down:
* [a-zA-Z0-9]+ : any letter - lowercase or uppercase or a number, 1 or more in number (the '+' sign).
* @ : The @ symbol.
* . : the dot.
* [a-zA-Z0-9]{3} : any letter - lowercase or uppercase or a number, exactly 3 in number.

### Program output
<img src="https://user-images.githubusercontent.com/32167236/96588360-2fa26900-1301-11eb-83a5-3e16e80de407.png">
