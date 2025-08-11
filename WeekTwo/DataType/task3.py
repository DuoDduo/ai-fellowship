# Task 1
name=input("Welcome to Raiza's Hub, Please enter your name: ")
print(f"Welcome {name.upper()}, It's a delight to have you here")

# Task 2
text="Python"
print(text[0])
print(text[-1])

# Task 3
user_name= input("Welcome to cafe one, Please enter your user name: ")
print(f"Hello! {user_name}")

# Task 4
word="pronouns"
print(word.find(word[-1])+ 1)

# Task 5
message="Hello World!"
print(message.replace("World", "Python"))

# Task 6
text = "Python is a Programming language"
print( "python" in text.lower())

# Task7
reverse_text = "python"
print( ''.join(reversed(reverse_text)))

# Task 8
text ="     Taiwo    "
print(text.strip())

# task 9
sentence = input("Introduce yourself in one sentence: ")
vowels_count = ( sentence.lower().count("a") + sentence.lower().count("e") + sentence.lower().count("i") + sentence.lower().count("o") + sentence.lower().count("u"))
print("Number of vowels:", vowels_count)

# task 10
number = "1234"
print(int(number)*2)

# task 11
fruits = "apple banana orange"
print(fruits.split())  

# task1 12
sentence = input("Enter a sentence to be printed on a new line: ")
print(*sentence.split(), sep="\n")


# task 13
sentence = input("Enter a sentence to replace all the spaces with under_score: ")
print(sentence.replace(" ", "_"))  


# task 14
fruit="Banana"
print(fruit.count("a"))

# task 15
file_url = "https://www.sop.com"
print(file_url.startswith("https://"))