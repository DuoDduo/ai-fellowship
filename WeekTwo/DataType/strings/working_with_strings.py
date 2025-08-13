# Strings in python

# single quotes
name='Ada'
print(name)

# Double quotes
greeting="Hello"
print(greeting)

# Triple quotes (for multi-lins strings)
story = '''Once upon a time,
there was a coder named Ada.'''
print(story)

# string with numbers and symbols
password="p@ssword123"
print(password)

# indexing
word="Python"
print(word[0])#P
print(word[-1])#n

#Slicing
word ="Python"
print(word[0:4])
print(word[2:])
print(word[:3])
print(word[::2])   # Pto
print(word[::-1])

#Concantenation
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World

# Repetition
word = "Hi! "
print(word * 3)  # Hi! Hi! Hi!

# String Searching and Checking
# Membership
text="Python programming"
print("Python" in text)
print("Java" in text)

# find()/rfind()
text="Hello World"
print(text.find("o"))
print(text.rfind("o"))

# #index()/rindex()
text = "Hello World"
print(text.index("World"))   # 6

# startswith()/endswith()
filename="data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))

# string methods
# Creating and manipulating strings.
    # upper()
    # lower()
    # title()
    # strip()
    # replace


    