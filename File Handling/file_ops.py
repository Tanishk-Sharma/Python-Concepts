# Create:
file_handler1 = open('magical_new_file.txt', 'w')
file_handler1.close()

# Read:
file_handler2 = open('foobar.txt', 'r')          # opening
content_str = file_handler2.read()               # reading all content into a string 
print(type(content_str))
print(content_str)
content_list = file_handler2.readlines()         # reading all content into a list 
file_handler2.close()  

# Update
file_handler3 = open('foobar.txt', 'a')
file_handler3.write('This is appended now.')
file_handler3.writelines(['Now', 'I', 'can', 'write', 'multiple', 'lines', 'at', 'once!!'])
file_handler3.close()

# Delete
import os
if os.path.exists('foobar.txt'):
  os.remove('foobar.txt')
