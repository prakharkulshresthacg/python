# 25.
# Create a program that checks whether a number is greater than 10 and less than 50.


num=16
print(num>10 and num<50)

# 26.
# Create a program that checks whether a number is less than 10 or greater than 100.

num1=55
print(num1<10 or num1>100)

# 27.
# Create a program using not that reverses the result of a comparison.

a=5
print(not a>10)

# 28.
# For each value, identify whether it is truthy or falsy:

# 0
# 1
# -5
# ""
# "Python"
# False
# True
# None

print(bool(0))        
print(bool(1))
print(bool(-5))
print(bool(""))
print(bool("Python"))
print(bool(False))
print(bool(True))
print(bool(None))

# 29.
# Use bool() to check the Boolean interpretation of:

# 0
# 10
# ""
# "Hello"
# None

print(bool(0))
print(bool(10))
print(bool(""))
print(bool("Hello"))
print(bool(None))

# 30.
# Create a small Python program that demonstrates the difference between data type and truthiness using:

# 0
# 1
# ""
# "Python"
# False
# None
# For each value, identify:

# Its data type.
# Its Boolean interpretation.

print(type(0), bool(0))
print(type(1), bool(1))
print(type(""), bool(""))
print(type("Python"), bool("Python"))
print(type(False), bool(False))
print(type(None), bool(None))