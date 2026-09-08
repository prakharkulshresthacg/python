
# ============================================================
# Part 2 - Predict the Output
# ============================================================

# ----- Question 1 -----
# Predicted:
# P
# h
# n
# o
text = "Python"

print(text[0])
print(text[3])
print(text[-1])
print(text[-2])

# ----- Question 2 -----
# Predicted:
# Prog
# gramm
# Progr
# amming
text = "Programming"

print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])

# ----- Question 3 -----
# Predicted:
# Pto
# yhn
# nohtyP
text = "Python"

print(text[::2])
print(text[1::2])
print(text[::-1])

# ----- Question 4 -----
# Predicted:
# 11
# W
# d
text = "Hello World"

print(len(text))
print(text[5])
print(text[-1])

# ----- Question 5 -----
# Predicted:
# True
# False
# True
text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

# ----- Question 6 -----
# Predicted:
# 1
# -1
# 3
text = "banana"

print(text.find("a"))
print(text.find("z"))
print(text.count("a"))

# ----- Question 7 -----
# Predicted:
# PYTHON
# python
# Python
# Python
# pYTHON
text = "Python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# ----- Question 8 -----
# Predicted:
# I like Python
# original text is unchanged because strings are immutable
text = "I like Java"

print(text.replace("Java", "Python"))
print(text)  # unchanged, still "I like Java"

# ----- Question 9 -----
# Predicted:
# Hello World
# HelloHelloHello
text = "Hello"

print(text + " World")
print(text * 3)


# ============================================================
# Part 3 - String Creation and Basic Operations
# ============================================================

# ----- Task 1: Create Strings -----
my_name = 'Prakhar'
my_city = "Delhi"
fav_language = 'Python'
short_message = "Learning strings is fun!"

print(my_name)
print(my_city)
print(fav_language)
print(short_message)

# ----- Task 2: Empty String -----
empty_string = ""
print(empty_string)
print(len(empty_string))
print(type(empty_string))

# ----- Task 3: String Information -----
task3_text = "Python Programming"
print(task3_text)
print(len(task3_text))
print(task3_text[0])
print(task3_text[-1])
print(task3_text[2])
print(task3_text[-2])


# ============================================================
# Part 4 - Indexing
# ============================================================

# ----- Task 4: Positive Indexing -----
task4_text = "Programming"
print(task4_text[0])
print(task4_text[1])
print(task4_text[4])
print(task4_text[len(task4_text) - 1])

# ----- Task 5: Negative Indexing -----
print(task4_text[-1])
print(task4_text[-2])
print(task4_text[-3])
print(task4_text[-len(task4_text)])

# ----- Task 6: Indexing Challenge -----
full_name = "Prakhar Kulshrestha"
print(full_name[0])
print(full_name[-1])
first_space_index = full_name.find(" ")
print(full_name[first_space_index + 1])


# ============================================================
# Part 5 - Slicing
# ============================================================

# ----- Task 7: Basic Slicing -----
task7_text = "Python Programming"
print(task7_text[0:6])
print(task7_text[7:19])
print(task7_text[:])
print(task7_text[:5])
print(task7_text[-5:])

# ----- Task 8: Slicing with Step -----
task8_text = "ABCDEFGHIJKL"
print(task8_text[::2])
print(task8_text[::3])
print(task8_text[1:9:2])
print(task8_text[::-1])

# ----- Task 9: Slicing with Negative Indexes -----
task9_text = "Python Programming"
print(task9_text[-5:])
print(task9_text[-10:])
print(task9_text[-1::-2])

# ----- Task 10: Slicing Challenge -----
task10_text = "Slicing Practice"
print(task10_text[:3])
print(task10_text[-3:])
print(task10_text[::2])
print(task10_text[::-1])
print(task10_text[1:-1])


# ============================================================
# Part 6 - Length
# ============================================================

# ----- Task 11 -----
short_word = "cat"
sentence = "I love programming"
sentence_with_spaces = "  I love   programming  "

print(len(short_word))
print(len(sentence))
print(len(sentence_with_spaces))
# spaces count towards the length just like any other character

# ----- Task 12 -----
text = "Python Programming"
last_index = len(text) - 1
print(last_index)
print(text[last_index])


# ============================================================
# Part 7 - Concatenation
# ============================================================

# ----- Task 13: Full Name -----
first_name = "Prakhar"
last_name = "Kulshrestha"
full_name = first_name + " " + last_name
print(full_name)

# ----- Task 14: Sentence Creation -----
name = "Prakhar"
age = 25
city = "Delhi"
language = "Python"
sentence14 = "My name is " + name + ", I am " + str(age) + " years old, I live in " + city + " and I love " + language + "."
print(sentence14)

# ----- Task 15: String and Integer -----
# text = "Age: " + age   # This would raise a TypeError
age = 20
print("Age: " + str(age))


# ============================================================
# Part 8 - String Repetition
# ============================================================

# ----- Task 16 -----
symbol = "#"
print(symbol * 3)
print(symbol * 5)
print(symbol * 10)

# ----- Task 17: Pattern -----
print("*" * 10)


# ============================================================
# Part 9 - Case Conversion
# ============================================================

# ----- Task 18 -----
task18_text = "python programming language"
print(task18_text.upper())
print(task18_text.lower())
print(task18_text.capitalize())
print(task18_text.title())
print(task18_text.swapcase())

# ----- Task 19: Case-Insensitive Comparison -----
str_a = "Python"
str_b = "python"
print(str_a == str_b)
print(str_a.lower() == str_b.lower())


# ============================================================
# Part 10 - Searching
# ============================================================

# ----- Task 20: Membership -----
task20_text = "Python is a programming language"
print("Python" in task20_text)
print("programming" in task20_text)
print("Java" in task20_text)
print("language" in task20_text)

# ----- Task 21: find() -----
print(task20_text.find("Python"))
print(task20_text.find("programming"))
print(task20_text.find("language"))
print(task20_text.find("Java"))
# find() returns -1 when the text is not found

# ----- Task 22: index() -----
print(task20_text.index("Python"))
print(task20_text.index("programming"))
print(task20_text.index("language"))
# task20_text.index("Java")  # This would raise a ValueError
# index() raises a ValueError instead of returning -1 when not found

# ----- Task 23: Count Characters -----
task23_text = "banana"
print(task23_text.count("a"))
print(task23_text.count("n"))
print(task23_text.count("b"))

# ----- Task 24: Starts and Ends -----
filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))


# ============================================================
# Part 11 - Replacing
# ============================================================

# ----- Task 25: Replace a Word -----
task25_text = "I am learning Java"
new_task25_text = task25_text.replace("Java", "Python")
print(new_task25_text)

# ----- Task 26: Multiple Replacements -----
task26_text = "apple apple apple"
print(task26_text.replace("apple", "mango"))

# ----- Task 27: Limited Replacement -----
print(task26_text.replace("apple", "mango", 1))

# ----- Task 28: Check Immutability -----
task28_text = "Python"
task28_text.upper()
print(task28_text)  # unchanged, still "Python"
task28_text = task28_text.upper()
print(task28_text)  # now "PYTHON"


# ============================================================
# Part 12 - Whitespace
# ============================================================

# ----- Task 29 -----
task29_text = "   Python Programming   "
print(repr(task29_text.strip()))
print(repr(task29_text.lstrip()))
print(repr(task29_text.rstrip()))

# ----- Task 30: User Input -----
user_name = input("Enter your name: ")
cleaned_name = user_name.strip()
print("Cleaned name:", cleaned_name)


# ============================================================
# Part 13 - Split and Join
# ============================================================

# ----- Task 31: Split -----
task31_text = "Python is easy to learn"
words_list = task31_text.split()
print(words_list)

# ----- Task 32: Split with Separator -----
task32_text = "apple,banana,mango,orange"
fruits = task32_text.split(",")
print(fruits)

# ----- Task 33: Join -----
words = ["Python", "is", "easy"]
print(" ".join(words))

# ----- Task 34: Join with Different Separators -----
print("-".join(words))
print("/".join(words))


# ============================================================
# Part 14 - String Formatting
# ============================================================

# ----- Task 35: F-String -----
f_name = "Prakhar"
f_age = 25
f_city = "Delhi"
print(f"My name is {f_name}, I am {f_age} years old and I live in {f_city}.")

# ----- Task 36: Arithmetic Inside F-String -----
a = 10
b = 20
print(f"The sum is {a + b}")


# ============================================================
# Part 15 - Error Identification
# ============================================================

# ----- Task 37 -----

# A
# text = "Python"
# print(text[20])
# Error: IndexError: string index out of range
# Reason: "Python" only has 6 characters (indices 0-5), index 20 doesn't exist
# Corrected: print(text[5])  (or any valid index)

# B
# text = "Python"
# text[0] = "J"
# Error: TypeError: 'str' object does not support item assignment
# Reason: strings are immutable, individual characters cannot be reassigned
# Corrected: text = "J" + text[1:]

# C
# age = 20
# print("Age: " + age)
# Error: TypeError: can only concatenate str (not "int") to str
# Reason: cannot concatenate a string and an integer directly
# Corrected: print("Age: " + str(age))

# D
# text = "Python"
# print(text.index("Java"))
# Error: ValueError: substring not found
# Reason: index() raises an error when the substring does not exist in the string
# Corrected: print(text.find("Java"))  # returns -1 instead of raising an error


# ============================================================
# Part 16 - Practical Challenge
# ============================================================

# ----- Task 38: Name Processor -----
raw_name = input("Enter your full name: ")
cleaned = raw_name.strip()

print("Original input:", raw_name)
print("Cleaned name:", cleaned)
print("Uppercase:", cleaned.upper())
print("Lowercase:", cleaned.lower())
print("Title case:", cleaned.title())
print("Length:", len(cleaned))
print("First character:", cleaned[0])
print("Last character:", cleaned[-1])
check_char = "a"
print(f"Contains '{check_char}':", check_char in cleaned)


# ============================================================
# Part 17 - Practical Challenge
# ============================================================

# ----- Task 39: Sentence Analyzer -----
sentence_input = input("Enter a sentence: ")

print("Original sentence:", sentence_input)
print("Number of characters:", len(sentence_input))
print("Number of words:", len(sentence_input.split()))
print("First character:", sentence_input[0])
print("Last character:", sentence_input[-1])
print("Uppercase:", sentence_input.upper())
print("Lowercase:", sentence_input.lower())
print("Title case:", sentence_input.title())
print("Contains 'Python':", "Python" in sentence_input)
chosen_char = "e"
print(f"Occurrences of '{chosen_char}':", sentence_input.count(chosen_char))


# ============================================================
# Part 18 - Final Challenge
# ============================================================

# ----- Task 40: Student Information -----
student_first_name = input("Enter first name: ").strip()
student_last_name = input("Enter last name: ").strip()
student_city = input("Enter city: ").strip()
student_course = input("Enter course: ").strip()
student_age = input("Enter age: ").strip()

student_full_name = student_first_name + " " + student_last_name

print("Full name (title case):", student_full_name.title())
print("Full name (uppercase):", student_full_name.upper())
print("Full name (lowercase):", student_full_name.lower())
print("Length of full name:", len(student_full_name))
print("First character of full name:", student_full_name[0])
print("Last character of full name:", student_full_name[-1])
print("City:", student_city)
print("Course:", student_course)
print(f"Age: {student_age}")
print("Course contains 'Python':", "Python" in student_course)
replaced_course = student_course.replace("Basic", "Advanced")
print("Course with replacement:", replaced_course)
print("Number of words in course name:", len(student_course.split()))
