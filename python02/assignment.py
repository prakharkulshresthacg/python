#24. Create variables for the following information:
#Your name, Your age, Your city. Use meaningful variable names.

my_name = "Prakhar"
my_age = 18
my_city = "Lucknow"

print(my_name, my_age, my_city)


#25. Create variables for: Student name, Student roll number, Student branch
#Follow Python's recommended naming convention (snake_case).

student_name = "Rahul"
student_roll_number = 101
student_branch = "B.Tech"

print(student_name, student_roll_number, student_branch)


#26. Write a program that assigns a value to a variable called marks,
#then reassigns a new value to marks.
#Explain the value before and after reassignment.

marks = 75
print("Before reassignment:", marks)

marks = 90
print("After reassignment:", marks)

#Explanation: pehle marks ki value 75 thi. Jab humne marks = 90 likha to
#purani value 75 hat gayi aur variable ab 90 ko refer karta hai.
#Ek variable ek time pe sirf ek hi value store karta hai, last wali value rehti hai.


#27. Use multiple assignment to create the following variables in one statement:
#name -> "Rahul", age -> 18, city -> "Patna"

name, age, city = "Rahul", 18, "Patna"

print(name, age, city)


#28. Use one statement to assign the value 0 to three variables: x, y, z

x = y = z = 0

print(x, y, z)


#29. The following code contains invalid variable names:
#1student = "Rahul"      -> variable number se start nahi ho sakta
#student name = "Rahul"  -> variable name mein space nahi aa sakta
#class = "B.Tech"        -> class python ka keyword hai
#Rewrite all three using valid and meaningful variable names.

student_one = "Rahul"
student_name_two = "Rahul"
student_class = "B.Tech"

print(student_one, student_name_two, student_class)


#30. Create a small Python program that stores a student's name and age,
#reassigns the age to a new value, and then displays the current values.

#storing student details
student_full_name = "Rahul Sharma"
student_age = 17

#reassigning age with new value
student_age = 18

print("Name:", student_full_name)
print("Age:", student_age)
