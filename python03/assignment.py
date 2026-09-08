#D. Practical Problems


#24. Create variables for the following information using appropriate values:
#Student name, Student age, Student height, Whether the person is a student,
#Student result (no result currently available). Then identify the type of each.

student_name = "Rahul"
student_age = 18
student_height = 5.7
is_student = True
student_result = None

print(type(student_name))     #<class 'str'>
print(type(student_age))      #<class 'int'>
print(type(student_height))   #<class 'float'>
print(type(is_student))       #<class 'bool'>
print(type(student_result))   #<class 'NoneType'>


#25. Create three variables: a -> 50, b -> 50.0, c -> "50"
#Use type() to identify the type of each variable.

a = 50
b = 50.0
c = "50"

print(type(a))   #<class 'int'>
print(type(b))   #<class 'float'>
print(type(c))   #<class 'str'>

#Explanation: teeno ki value dikhne mein 50 hi hai magar type alag hai.
#50 bina point ke integer hai, 50.0 point ke saath float hai,
#aur "50" quotes ke andar hai isliye wo string hai.


#26. Create two variables: a -> True, b -> "True"
#Use type() and explain why their types are different.

a = True
b = "True"

print(type(a))   #<class 'bool'>
print(type(b))   #<class 'str'>

#Explanation: True bina quotes ke Python ka keyword hai jo boolean value hai,
#uski sirf do values hoti hai True aur False.
#"True" quotes ke andar hai isliye wo sirf characters ka group yaani string hai.
#Python ke liye wo koi special meaning nahi rakhta, "abc" jaisa hi ek text hai.


#27. Create two variables: a -> None, b -> "None"
#Use type() and explain the difference.

a = None
b = "None"

print(type(a))   #<class 'NoneType'>
print(type(b))   #<class 'str'>

#Explanation: None Python ka keyword hai jo batata hai ki koi value hai hi nahi
#(khali/absent value), uska type NoneType hota hai.
#"None" quotes ke andar likha hai isliye wo 4 letters ka text hai yaani string,
#aur uski length 4 hai, wo khali nahi hai.


#28. Create a variable called value. First assign an integer, check type,
#then reassign a string and check type again. Explain what changed.

value = 100
print(type(value))   #<class 'int'>

value = "hundred"
print(type(value))   #<class 'str'>

#Explanation: pehle value ke andar integer 100 tha isliye type int aaya.
#Reassign karne ke baad value ab string ko refer kar rahi hai isliye type str ho gaya.
#Python mein variable ka apna koi fix type nahi hota, type us value ka hota hai
#jo variable us waqt refer kar raha hai. Isko dynamic typing kehte hai.


#29. Create a small Python program that stores information about a product:
#name (string), quantity (integer), price (float), availability (Boolean),
#discount information (None). Use type() to identify every value.

product_name = "Notebook"
product_quantity = 25
product_price = 45.50
is_available = True
product_discount = None

print("Name:", product_name, type(product_name))            #<class 'str'>
print("Quantity:", product_quantity, type(product_quantity)) #<class 'int'>
print("Price:", product_price, type(product_price))         #<class 'float'>
print("Available:", is_available, type(is_available))       #<class 'bool'>
print("Discount:", product_discount, type(product_discount)) #<class 'NoneType'>


#30. Create a small program that demonstrates the difference between:
#10, 10.0, "10", True, "True", None, "None"

print(type(10))       #<class 'int'>
print(type(10.0))     #<class 'float'>
print(type("10"))     #<class 'str'>
print(type(True))     #<class 'bool'>
print(type("True"))   #<class 'str'>
print(type(None))     #<class 'NoneType'>
print(type("None"))   #<class 'str'>

#Explanation:
#10       -> int      : bina decimal point ke pura number
#10.0     -> float    : decimal point ke saath number
#"10"     -> str      : quotes ke andar hai isliye text, isse calculation nahi hoga
#True     -> bool     : keyword hai, boolean ki do values mein se ek
#"True"   -> str      : quotes ke andar hai isliye sirf text
#None     -> NoneType : value ka na hona batata hai
#"None"   -> str      : quotes ke andar hai isliye 4 letter ka text

#Main point: quotes lagate hi koi bhi cheez string ban jaati hai,
#chahe wo number ho, True ho ya None ho.
