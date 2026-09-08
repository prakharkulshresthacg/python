# 1.
# Write a Python program that asks the user for their name and prints the name.

name=input("Enter your name: ")
print("Your name is: ",name)

# 2.
# Write a program that asks the user for their city and displays:

# Your city is <city>

city=input("Enter your city: ")
print("Your city is: ",city)

# 3.
# Take a user's name and age using two separate input() statements and print both values.

name1=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Your name is: ",name1)
print("Your age is:",age)

# 4.
# What type of value does input() return by default?

#answer:string



# 5.
# Write a program that takes a value using input() and displays its type using type().

a=int(input("Enter a value: "))
print("The type of the value is: ",type(a))


# 6.
# Take first name and last name separately and display them together.

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print("Your full name is: ",first_name,last_name)


# 7.
# Take three pieces of information:

# name
# city
# college
# Store each in a separate variable and display them.


name2=input("Enter your name: ")
city2=input("Enter your city: ")
college=input("Enter your college name: ")
print(f"Your name is: {name2},Your city is: {city},Your college name is: {college}")


# 8.
# Write a program that takes two names on the same line and stores them in two variables using .split().

name3,name4=map(str,input("Enter two names:").split())


# 9.
# Suppose the user enters:

# Python Programming
# using one input() statement with .split().

# What values will the two variables receive?

#Answer:   Python,Programming



# 10.
# Write a program that takes three words from one line and displays them separately
 


word1,world2,world3=map(str, input("Enter three words: ").split())

# 11.
# Convert the string:

# "25"
# into an integer.

c=int("25")

# 12.
# Convert the string:

# "25.5"
# into a floating-point number.

d=float("25.5")

# 13.
# Convert the integer:

# 100
# into a string

e=str(100)

# 14.
# Take an integer from the user and print its type after conversion.

int1=int(input("Enter an integer: "))
print("The type of the value is: ",type(int1))


# 15.
# Take a floating-point number from the user and print its type after conversion.

float1=float(input("Enter a floating-point number: "))
print("The type of the value is: ",type(float1))


# 16.
# Why does this produce string concatenation instead of numeric addition?

# a = input()
# b = input()

# print(a + b)

#Answer: Because input() function takes input as string by default. So, when we use + operator with strings, it concatenates them instead of adding them numerically.



# 17.
# Correct the following program so that it performs numeric addition:

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# print(a + b)

new_a=int(input("Enter first number: "))
new_b=int(input("Enter second number: "))
print(new_a + new_b)

# 18.
# Create variables:

# name = "Rahul"
# age = 20
# Use an f-string to display:

# My name is Rahul and I am 20 years old.

name="Rahul"
age=20
print(f"My name is {name} and I am {age} years old.")



# 19.
# Create:

# a = 10
# b = 20
# Use an f-string to display their sum.

a=10
b=20
print(f"The sum of {a} and {b} is: {a+b}")


# 20.
# Take a user's name and age and display them in one sentence using an f-string.

name5=input("Enter your name: ")
age1=int(input("Enter your age: "))
print(f"Your name is {name5} and you are {age1} years old.")


# 21.
# Take the price of a product as a floating-point value and display it using exactly two decimal places.
price=float(input("Enter the price of the product: "))
print(f"The price of the product is: {price:.2f}")


# 22.
# What is the purpose of:

# :.2f
# inside an f-string?

#Answer: The purpose of :.2f inside an f-string is to format a floating-point number to display exactly two decimal places. The .2 specifies the number of decimal places, and the f indicates that the value is a floating-point number.


# 23.
# Write a program that takes:

# product name
# price
# quantity
# and displays all three values using f-strings.

product_name=input("Enter the product name: ")
product_price=float(input("Enter the product price: "))
product_quantity=int(input("Enter the product quantity: "))
print(f"Product name: {product_name}, Price: {product_price}, Quantity: {product_quantity}")


# 24.
# What will this display?

# print("A", "B", "C")


#Answer: It will display: A B C



# 25.
# Rewrite the following so that the values are separated by -:

# print("2026", "08", "19")


print("2026", "08", "19", sep="-")


# 26.
# Write two print() statements that produce:

# Hello World
# on the same line using end.

print("Hello",end=" ")
print("World")


# 27.
# Write a program that takes two integers from the user and displays:

# First number: <first>
# Second number: <second>
# Sum: <sum>
# Use f-strings for the output.

first_num=int(input("Enter the first number: "))
second_num=int(input("Enter the second number: "))
sum=first_num+second_num
print(f"First number: {first_num}, Second number: {second_num}, Sum: {sum}")



# 28.
# Write a program that takes the price and quantity of a product and calculates the total cost.

# Display:

# Price: ...
# Quantity: ...
# Total: ...
# Use appropriate type conversion and an f-string.

product_price=float(input("Enter the product price: "))
product_quantity=int(input("Enter the product quantity: "))
total_cost=product_price*product_quantity
print(f"Price: {product_price}, Quantity: {product_quantity}, Total: {total_cost}")


# 29.
# Write a program that takes a student's:

# name
# age
# marks
# where age is an integer and marks is a floating-point value.

# Display all information using a clear formatted message.

name6=input("Enter the student's name: ")
age2=int(input("Enter the student's age: "))
marks=float(input("Enter the student's marks: "))
print(f"Student's Name: {name6}, Age: {age2}, Marks: {marks}")


# 30.
# Create a small "Student Information" program that:

# Takes the student's name.
# Takes the student's age as an integer.
# Takes the student's height as a floating-point number.
# Takes the name of the city.
# Displays all information using f-strings.
# Displays the height with exactly two decimal places.

student_name=input("Enter the student's name: ")
student_age=int(input("Enter the student's age: "))
student_height=float(input("Enter the student's height: "))
student_city=input("Enter the name of the city: ")
print(f"Student's Name: {student_name}, Age: {student_age}, Height: {student_height:.2f}, City: {student_city}")