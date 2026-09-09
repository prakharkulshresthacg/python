num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num > 0 and num % 2 == 0:
    print("Positive Even")
elif num > 0 and num % 2 != 0:
    print("Positive Odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even")
else:
    print("Negative Odd")
