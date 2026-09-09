a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    second_largest = a
elif (b > a and b < c) or (b < a and b > c):
    second_largest = b
else:
    second_largest = c

print("Second largest number is", second_largest)
