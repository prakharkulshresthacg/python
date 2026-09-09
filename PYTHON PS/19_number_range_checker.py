num = float(input("Enter a number: "))

if num < 0:
    print("Negative")
elif num <= 10:
    print("Number is between 0 and 10")
elif num <= 50:
    print("Number is between 11 and 50")
elif num <= 100:
    print("Number is between 51 and 100")
else:
    print("Number is above 100")
