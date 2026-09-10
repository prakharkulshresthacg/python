# A. Basic for Loop

# 1
for i in range(5):
    print("Hello")

# 2
for i in range(10):
    print(i, end=" ")
print()

# 3
for i in range(1, 11):
    print(i)

# 4
for i in range(10, 0, -1):
    print(i)

# 5
for i in range(5, 51, 5):
    print(i)


# B. range() Practice

# 6
for i in range(2, 21, 2):
    print(i)

# 7
for i in range(1, 20, 2):
    print(i)

# 8
for i in range(3, 19, 3):
    print(i)

# 9
for i in range(20, 1, -2):
    print(i)

# 10
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)


# C. Conditions with for

# 11
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

# 12
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

# 13
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)

# 14
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

# 15
n = int(input("Enter n: "))
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count = count + 1
print("Even count:", count)


# D. Calculation Problems

# 16
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum:", total)

# 17
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i
print("Sum of evens:", total)

# 18
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i
print("Sum of odds:", total)

# 19
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 20
n = int(input("Enter n: "))
product = 1
for i in range(1, n + 1):
    product = product * i
print("Product:", product)


# E. String Iteration

# 21
s = input("Enter a string: ")
for ch in s:
    print(ch)

# 22
s = input("Enter a string: ")
for ch in s:
    print(ch, end="")
print()

# 23
s = input("Enter a string: ")
count = 0
for ch in s:
    count = count + 1
print("Length:", count)

# 24
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch == "a":
        count = count + 1
print("Count of 'a':", count)

# 25
s = input("Enter a string: ")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for ch in s:
    if ch in uppercase_letters:
        count = count + 1
print("Uppercase count:", count)


# F. Nested for Loops

# 26
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()

# 27
for row in range(4):
    for col in range(5):
        print("*", end="")
    print()

# 28
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()

# 29
for row in range(1, 6):
    for num in range(1, row + 1):
        print(num, end="")
    print()

# 30
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()


# Final Practice Challenge

n = int(input("Enter n: "))
for row in range(1, n + 1):
    for num in range(1, row + 1):
        print(num, end="")
    print()
