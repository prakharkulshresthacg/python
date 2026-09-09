temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Very Cold")
elif temp <= 25:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")
