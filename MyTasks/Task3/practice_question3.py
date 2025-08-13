
# task 11
# Given "apple,banana,orange", split the string into a list of fruits.
fruits = "apple banana orange"
print(fruits.split())  

# task1 12
# Ask the user for a sentence and print each word on a new line.
sentence = input("Enter a sentence to be printed on a new line: ")
print(*sentence.split(), sep="\n")


# task 13
# Replace all spaces in a string with underscores (_).
sentence = input("Enter a sentence to replace all the spaces with under_score: ")
print(sentence.replace(" ", "_"))  


# task 14
# Count how many times the letter "a" appears in "Banana".
fruit="Banana"
print(fruit.count("a"))

# task 15
# Check if a given string starts with "https://".
file_url = "https://www.sop.com"
print(file_url.startswith("https://"))