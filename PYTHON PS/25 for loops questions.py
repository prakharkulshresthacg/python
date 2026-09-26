# ==========================================
# Nested For Loops – Basic Python Problems
# Assignment: 25 For Loops Questions
# ==========================================


# ------------------------------------------
# 1. Print a 3x3 Star Grid
# ------------------------------------------
print("--- Question 1 ---")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# ------------------------------------------
# 2. Print Numbers in Rows
# ------------------------------------------
print("\n--- Question 2 ---")
for i in range(3):
    for j in range(1, 4):
        print(j, end=" ")
    print()


# ------------------------------------------
# 3. Print Row Numbers
# ------------------------------------------
print("\n--- Question 3 ---")
for i in range(1, 4):
    for j in range(3):
        print(i, end=" ")
    print()


# ------------------------------------------
# 4. Increasing Star Pattern
# ------------------------------------------
print("\n--- Question 4 ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------
# 5. Decreasing Star Pattern
# ------------------------------------------
print("\n--- Question 5 ---")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------
# 6. Increasing Number Pattern
# ------------------------------------------
print("\n--- Question 6 ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ------------------------------------------
# 7. Repeated Number Pattern
# ------------------------------------------
print("\n--- Question 7 ---")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# ------------------------------------------
# 8. Multiplication Tables from 1 to 5
# ------------------------------------------
print("\n--- Question 8 ---")
for i in range(1, 6):
    print(f"Table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()


# ------------------------------------------
# 9. Multiplication Grid
# ------------------------------------------
print("\n--- Question 9 ---")
for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


# ------------------------------------------
# 10. Print Squares in Rows
# ------------------------------------------
print("\n--- Question 10 ---")
for i in range(5):
    for j in range(1, 6):
        print(j * j, end=" ")
    print()


# ------------------------------------------
# 11. Alphabet Pattern
# ------------------------------------------
print("\n--- Question 11 ---")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# ------------------------------------------
# 12. Repeated Alphabet Pattern
# ------------------------------------------
print("\n--- Question 12 ---")
for i in range(5):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


# ------------------------------------------
# 13. Odd Number Pattern
# ------------------------------------------
print("\n--- Question 13 ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        odd_num = 2 * j - 1
        print(odd_num, end=" ")
    print()


# ------------------------------------------
# 14. Even Number Pattern
# ------------------------------------------
print("\n--- Question 14 ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        even_num = 2 * j
        print(even_num, end=" ")
    print()


# ------------------------------------------
# 15. 5x5 Star Square
# ------------------------------------------
print("\n--- Question 15 ---")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# ------------------------------------------
# 16. 5x5 Number Square
# ------------------------------------------
print("\n--- Question 16 ---")
for i in range(5):
    for j in range(1, 6):
        print(j, end=" ")
    print()


# ------------------------------------------
# 17. Row-wise Numbers
# ------------------------------------------
print("\n--- Question 17 ---")
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num = num + 1
    print()


# ------------------------------------------
# 18. Print 1 to 20 in 4 Rows
# ------------------------------------------
print("\n--- Question 18 ---")
count = 1
for i in range(4):
    for j in range(5):
        print(count, end=" ")
        count = count + 1
    print()


# ------------------------------------------
# 19. Print Coordinate Pairs
# ------------------------------------------
print("\n--- Question 19 ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()


# ------------------------------------------
# 20. Print All Number Combinations
# ------------------------------------------
print("\n--- Question 20 ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# ------------------------------------------
# 21. 10x10 Multiplication Grid
# ------------------------------------------
print("\n--- Question 21 ---")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


# ------------------------------------------
# 22. Repeated Number Pattern
# ------------------------------------------
print("\n--- Question 22 ---")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


# ------------------------------------------
# 23. Decreasing Number Pattern
# ------------------------------------------
print("\n--- Question 23 ---")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# ------------------------------------------
# 24. Reverse Number Pattern
# ------------------------------------------
print("\n--- Question 24 ---")
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end="")
    print()


# ------------------------------------------
# 25. Repeated Row Number Pattern
# ------------------------------------------
print("\n--- Question 25 ---")
for i in range(1, 6):
    for j in range(5):
        print(i, end="")
    print()
