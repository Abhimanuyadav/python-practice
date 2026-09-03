
#1
name = "Abhimanu"
city = 'New delhi'
favorite_language = "Python"
message = 'Coding is fun and practical!'

print("Name:", name)
print("City:", city)
print("Favorite Language:", favorite_language)
print("Message:", message)

#2
empty_str = ""

print("String content:", empty_str)
print("Length:", len(empty_str))
print("Data type:", type(empty_str))

#3
text = "Python Programming"

print("string:", text)
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Second-last character:", text[-2])

#4
text="programming"
print(text[0])
print(text[-1])
print(text[6])
print(text[-1])

# 5
text = "Python Programming"

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-len(text)])

# 6
full_name = "abhimanu yadav"

print(full_name[0])
print(full_name[-1])
print(full_name[5])

# 7
text = "Python Programming"

print(text[:6])
print(text[7:])
print(text[:])
print(text[:5])
print(text[-5:])

# 8
letters = "ABCDEFGHIJKL"

print(letters[::2])
print(letters[::3])
print(letters[1:9:2])
print(letters[::-1])

# 9
text = "Python Programming"

print(text[-5:])
print(text[-10:])
print(text[-1:-11:-1])

# 10
word = "Programming"

print(word[:3])
print(word[-3:])
print(word[::2])
print(word[::-1])
print(word[1:-1])

# 11
short_word = "Code"
sentence = "Python is easy"
sentence_with_spaces = "Python programming is fun"

print(len(short_word))
print(len(sentence))
print(len(sentence_with_spaces))

# Task 12
text = "Python Programming"
last_index = len(text) - 1

print(last_index)
print(text[last_index])

# 13
first_name = "abhimanu"
last_name = "yadav"

full_name = first_name + " " + last_name
print(full_name)

# 14
name = "abhimanu"
age = 21
city = "new delhi"
language = "Python"

sentence = name + " is " + str(age) + " years old, lives in " + city + ", and learns " + language + "."
print(sentence)

# 15
name = "Abhimanu"
age = 21

try:
    print(name + age)
except TypeError as error:
    print(error)

print(name + str(age))

# 16
symbol = "#"

print(symbol * 3)
print(symbol * 5)
print(symbol * 10)

# 17
star = "*"

print(star * 10)

# 18
text = "python programming language"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# 19
first_text = "Python"
second_text = "python"

print(first_text == second_text)
print(first_text.lower() == second_text.lower())

# 20
text = "Python is a programming language"

print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)

# 21
text = "Python is a programming language"

print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))

# 22
text = "Python is a programming language"

print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))

try:
    print(text.index("Java"))
except ValueError as error:
    print(error)

# 23
word = "banana"

print(word.count("a"))
print(word.count("n"))
print(word.count("b"))


# 24 
filename = "student_notes.pdf"
print(filename.startswith("student"))  
print(filename.endswith(".pdf"))       
print(filename.endswith(".txt"))   

# 25
text = "I am learning Java"
print(text.replace("Java", "Python"))

# 26
text="apple apple apple"
print(text.replace("apple", "mango",))

# 27
text="apple apple apple"
print(text.replace("apple", "mango", 1))

# 28
text="python"
print(text.upper)

#29
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# 30
userinput = input("abhimanu ")
cleanedname = userinput.strip()
print("Cleaned name:", cleanedname)


# 31
text = "Python is easy to learn"
words = text.split()
print(words)


# 32
fruits = "apple,banana,mango,orange"
fruit_list = fruits.split(",")
print(fruit_list)


# 33
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)


# 34
words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))


# 35
name = "Abhimanu"
age = 20
city = "Nirmal"

print(f"My name is {name}, I am {age} years old, and I live in {city}.")


# 36
a = 10
b = 20

print(f"The sum is {a + b}")


# 37
text = "Python"
print(text[2:5])
text = "Python"
text = "J" + text[1:]
print(text)
age = 20
print("Age: " + str(age))

text = "Python"
if "Java" in text:
    print(text.index("Java"))
else:
    print("Java not found")


# 38
original_name = input("Enter your full name: ")

cleaned_name = original_name.strip()

print("Original input:", original_name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))

if cleaned_name:
    print("First character:", cleaned_name[0])
    print("Last character:", cleaned_name[-1])

character = input("Enter a character to check: ")

if character in cleaned_name:
    print("Character exists in the name")
else:
    print("Character does not exist in the name")


# 39
sentence = input("Enter a sentence: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))

if sentence:
    print("First character:", sentence[0])
    print("Last character:", sentence[-1])

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())

if "Python" in sentence:
    print("Python exists in the sentence")
else:
    print("Python does not exist in the sentence")

character = input("Enter a character to count: ")
print("Number of times character occurs:", sentence.count(character))


# 40
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()

full_name = first_name + " " + last_name

print("Full name:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))

if full_name:
    print("First character:", full_name[0])
    print("Last character:", full_name[-1])

print("City:", city)
print("Course:", course)
print(f"Age: {age}")

if"Python" in course:
    print("Course contains Python")

    print("Course does not contain Python")

old_word = input("Enter word to replace in course: ")
new_word = input("Enter new word: ")

new_course = course.replace(old_word, new_word)
print("Updated course:", new_course)

print("Number of words in course:", len(course.split()))

