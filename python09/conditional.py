# 1.
# Write a program that checks whether a number is greater than 10. If it is, print:

# Greater than 10

a=int(input("Enter a number: "))
if a>10:
 print("Greater than 10")


# 2.
# Write a program that checks whether a person's age is at least 18. If true, print:

# Adult


age=int(input("Enter your age: "))
if age>=18:
    print("Adult")

# 3.
# Take a number from the user and print Positive if the number is greater than 0.

num=int(input("Enter your number: "))
if(num>0):
    print("Positive")

# 4.
# Write an if statement that checks whether:

# marks >= 40
# and prints Pass.

marks=int(input("Enter your marks: "))
if(marks>=40):
    print("pass")


# 5.
# Take a number from the user and print Zero when the number is equal to 0.
num1=int(input("Enter a number: "))
if(num1==0):
    print("zero")


# 6.
# Write a program that checks whether a number is positive or not.

# Expected messages:

# Positive
# Not positive

num2=int(input("Enter a number: "))
if(num2>0):
    print("Positive")
elif(num2<0):
    print("Not positive")


# 7.
# Take a person's age and display:

# Adult
# if the age is at least 18; otherwise display:

# Minor

age1=int(input("Enter age: "))
if(age>=18):
    print("Adult")
else:
    print("Minor")



# 8.
# Write a program that checks whether a number is even or odd using %.

number=int(input("Enter the number: "))
if(number%2==0):
    print("Even")
else:
    print("odd")


# 9.
# Take marks from the user and display Pass if marks are at least 40; otherwise display Fail.


if(marks>=40):
    print("Pass")
else:
    print("Fail")


# 10.
# Take two numbers and print which one is greater using if-else.

a,b=map(int,input("Enter two numbers:").split())
if(a>b):
    print("a is greeater than b")
elif(a==b):
    print("both numbers are equal")
else:
    print("b is greater than a")


# 11.
# Write a program that displays:

# A
# B
# C
# D
# F
# according to these marks:

# 90 or above → A
# 75 to 89   → B
# 60 to 74   → C
# 40 to 59   → D
# Below 40   → F

marks1=int(input("Enter your marks: "))
if(marks1>=90):
    print("A")
elif(marks1>=75):
    print("B")
elif(marks1>=60):
    print("C")
elif(marks1>=40):
    print("D")
else:
    print("F")


# 12.
# Take a number from the user and display:

# Positive
# Negative
# Zero
# using if-elif-else.

num3=int(input("Enter a number: "))
if(num3>0):
    print("Positive")
elif(num3<0):
    print("Negative")
else:
    print("Zero")

# 13.
# Take a number representing a day:

# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# Display Other for any other value.

day=int(input("Enter a number: "))
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
elif(day==4):
    print("Thursday")
elif(day==5):
    print("Friday")
else:
    print("Other")


# 14.
# Take a student's marks and display:

# Excellent
# Good
# Pass
# Fail
# using appropriate ranges.

marks2=int(input("Enter your marks: "))
if(marks2>=90):
    print("Excellemt")
elif(marks2>=75):
    print("Good")
elif(marks2>=40):
    print("Pass")
else:
    print("Fail")


# 15.
# Take a number and display whether it is:

# 1
# 2
# 3
# or:
    # Other

num4=int(input("Enter your number: "))
if(num4==1):
    print("Number is 1")
elif(num4==2):
    print("Number is 2")
elif(num4==3):
    print("Number is 3")
else:
    print("Other")


# 16.
# Write a program that first checks whether a person is at least 18. If yes, check whether the person is at most 60.

# Display:

# Between 18 and 60
# when both conditions are satisfied.

age2=int(input("Enter your age: "))
if(age2>=18):
    if(age2<=60):
        print("Between 18 and 60")


# 17.
# Take marks from the user.

# First check whether the student passed (marks >= 40).

# If the student passed, check whether marks are at least 75.

# Display:

# Good
# or:

# Passed
# If the student did not pass, display:

# Failed

marks3=int(input("Enter your marks: "))
if(marks3>=40):
    if(marks3>=75):
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")


# 18.
# Write a nested condition that checks whether a number is positive. If it is positive, check whether it is greater than 100

num5=int(input("Enter the number: "))
if(num5>0):
    if(num>100):
        print("The number is greater than 100")

# 19.
# Take an age.

# First check whether the age is at least 18.

# If yes, check whether it is at least 60.

# Display an appropriate message for each case.

age3=int(input("Enter your age: "))
if(age3>=18):
    print("Adult")
    if(age3<=60):
        print("Between 18 and 60")

# 20.
# Write a nested condition that checks whether a number is non-zero and then checks whether it is positive or negative.

num6=int(input("Enter number: "))
if(num6!=0):
    if(num<0):
        print("Negative")
    else:
        print("Positive")


# 21.
# Take age and marks from the user.

# Print Eligible only when:

# age >= 18
# and
# marks >= 40

age4=int(input("Enter your age: "))
mark=int(input("Enter your marks: "))
if(age4>=18 and mark>=40):
    print("Elligible")


# 22.
# Take a number and print Special if:

# number < 10
# or
# number > 100

n=int(input("Enter the number: "))
if(n>100 or n<10):
    print("Special")


# 23.
# Take a user's age and Boolean variable has_id.

# Print Allowed only when:

# age >= 18
# and
# has_id is True

age5=int(input("Enter age: "))
has_id=bool(input("Person has id? "))
if(age5>=18 and has_id==True):
    print("Allowed")


# 24.
# Take two numbers and check whether:

# first number > 10
# and
# second number > 10
# Print Both are greater than 10 when true.

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if(n1>10 and n2>10):
    print("Both are greater than 10")


# 25.
# Take a number and check whether it is either:

# less than 0
# or
# greater than 100

n3=int(input("Enter number: "))
if(n3<0):
    print("Less than 0")
elif(n3>100):
    print("Greater tha 100")


# 26.
# Write a program using not that prints Open when:

# is_closed = False

is_closed=bool(input("Enter if True or False: "))
if(not(is_closed==True)):
    print("Open")


# 27.
# Take a number and check whether it is between 10 and 50 using and.

n4=int(input("enter number: "))
if(n4>10 and n4<50):
    print("Number is between 10 and 50.")


# 28.
# Take a number and check whether it is outside the range 10 to 50 using or.

n5=int(input("Enter number: "))
if(n5<10 or n5>50):
    print("Number is outside the range of 10 and 50")


# 29.
# Create a program with three Boolean values:

# is_student
# has_id
# has_ticket
# Print Allowed only when all three are true.

is_student=bool(input("Is student?"))
has_id1=bool(input("Has id?"))
has_ticket=bool(input("Has ticket?"))

if(is_student == True and has_id1==True and has_ticket==True):
    print("Allowed")


# 30.
# Create a small Eligibility Checker program.

# Take:

# age
# marks
# has_id
# The person is eligible only when:

# age >= 18
# and
# marks >= 40
# and
# has_id is True
# Display:

# Eligible
# if all conditions are satisfied; otherwise display:

# Not eligible
# Explain why and is appropriate for this problem.


age6=int(input("Enter your age: "))
marks4=int(input("Enter your marks: "))
Has_id=bool(input("Has id?"))
if(age6>=18 and marks4>=40 and Has_id==True):
    print("Eligible")
else:
    print("Not eligible")

#and is important because it lets us check if all these conditions are True and will only print only if all are True.