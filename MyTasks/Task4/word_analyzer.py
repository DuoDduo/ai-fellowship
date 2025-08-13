# Task 6
# - Ask the user to input a word.
word=input("Enter a word: ")
# - Print the length of the word.
print(len(word))


# - Check if it is all uppercase, all lowercase, or title case.
is_upper=word.isupper()
print(f"The word typed is in uppercase: {is_upper}")
is_lower=word.islower()
print(f"The word typed is in lowercase: {is_lower}")
is_title= word.istitle()
print(f"The word typed is in title format: {is_title}")

# - Reverse the word using slicing.
reversed_word=word[::-1]
print(reversed_word)