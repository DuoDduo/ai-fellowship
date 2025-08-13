# upper
name = "Ada Balogun"
print(name.upper())

# title
sentence = "python is amazing"
print(sentence.title())

# lower
sentence = "PYTHON IS AMAZING"
print(sentence.lower())

# strip
text ="     Abuja    "
print(text.strip())

# replace- replace occurences of a substring with another substring
message="I love Java"
print(message.replace("Java", "Python"))

# swapcase()- switches lowercase to uppercase and viceversa
text="Hello ABEOKUTA"
print(text.swapcase())

# lstrip()- removes whitespace (or specified characters) from the left side only.
text= "     Nigeria"
print(text.lstrip())

# rstrip()- removes whitespace (or specified characters) from the right side only.
text= "Nigeria    "
print(text.rstrip())

# split() - splits a string into  a list using a seperator(default is space)
fruits = "mango orange banana"
print(fruits.split())  

# splitlines() splits a string into a list at each newline(\n)
lines="Line 1\nLine2\nLine3"
print(lines.splitlines())

# join()- Joins a list of strings into one string with a specified separator
words=["I", "love", "Python"]
print(" ".join(words))

# center() centers the string within a specified width, padding with spaces or characters
text="Python"
print(text.center(20, '-'))

# ljust() left aligns the strring within a specified width, padding with spaces or characters.
text="Python"
print(text.ljust(10, "*"))


# rjust() left aligns the strring within a specified width, padding with spaces or characters.
text="Python"
print(text.rjust(10, "*"))

# zfill() pads a numeric string on the left until it reaches a given length
num="42"
print((num.zfill(5)))

# isalpha()- Checks if the string contains only letters
print("Lagos".isalpha())
print("Lagos123".isalpha)

# isdigit()- Checks if the string contains only digits.
print("12345".isdigit())
print("123a".isdigit())

# isalnum()- checks if the string contains only letters and digits
print("Python3".isalnum())
print("Python 3".isalnum())