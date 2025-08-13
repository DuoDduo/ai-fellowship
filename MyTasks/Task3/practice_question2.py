
# Task 6
#  Check if a given string contains the substring "python" (case-insensitive).
text = "Python is a Programming language"
print( "python" in text.lower())

# Task7
# Write a program to reverse a string without using slicing ([::-1]).
reverse_text = "python"
print( ''.join(reversed(reverse_text)))

# Task 8
#  Given a string with extra spaces, remove the leading and trailing spaces.
text ="     Taiwo    "
print(text.strip())

# task 9
# 9. Ask the user to enter a sentence and print the number of vowels in it.
sentence = input("Introduce yourself in one sentence: ")
vowels_count = ( sentence.lower().count("a") + sentence.lower().count("e") + sentence.lower().count("i") + sentence.lower().count("o") + sentence.lower().count("u"))
print("Number of vowels:", vowels_count)

# task 10
#  Convert a string "1234" to an integer and multiply it by 2.
number = "1234"
print(int(number)*2)
