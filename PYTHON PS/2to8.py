print("3. Word Score Calculator")

sentence = input("Enter a sentence: ")
words = sentence.split()

highest_word = ""
highest_score = -1
vowels = "aeiouAEIOU"

for word in words:
    score = 0

    for ch in word:
        if ch in vowels:
            score = score + 2
        elif ch.isalpha():
            score = score + 1
        elif ch.isdigit():
            score = score + 3
        else:
            score = score + 4

    print(word, "score is", score)

    if score > highest_score:
        highest_score = score
        highest_word = word

print("Word with highest score:", highest_word)
print()


print("4. Password Batch Validator")

for i in range(1, 6):
    password = input("Enter password for user " + str(i) + ": ")

    length_ok = False
    upper_ok = False
    lower_ok = False
    digit_ok = False
    special_ok = False

    if len(password) >= 8:
        length_ok = True

    for ch in password:
        if ch.isupper():
            upper_ok = True
        elif ch.islower():
            lower_ok = True
        elif ch.isdigit():
            digit_ok = True
        else:
            special_ok = True

    conditions = 0

    if length_ok:
        conditions = conditions + 1
    if upper_ok:
        conditions = conditions + 1
    if lower_ok:
        conditions = conditions + 1
    if digit_ok:
        conditions = conditions + 1
    if special_ok:
        conditions = conditions + 1

    if conditions == 5:
        print("Strong")
    elif conditions >= 3:
        print("Medium")
    else:
        print("Weak")

print()


print("5. Sentence Word Analyzer")

sentence = input("Enter a sentence: ")
words = sentence.split()

short_count = 0
medium_count = 0
long_count = 0

for word in words:
    length = len(word)
    print(word, "length is", length)

    if length <= 3:
        print("Short")
        short_count = short_count + 1
    elif length <= 6:
        print("Medium")
        medium_count = medium_count + 1
    else:
        print("Long")
        long_count = long_count + 1

print("Short words:", short_count)
print("Medium words:", medium_count)
print("Long words:", long_count)
print()


print("6. Number-String Conversion Challenge")

for i in range(1, 6):
    num = int(input("Enter number " + str(i) + ": "))
    num_str = str(num)

    even_count = 0
    odd_count = 0

    for digit in num_str:
        if digit == "-":
            continue

        digit_num = int(digit)

        if digit_num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

    print("Even digits:", even_count)
    print("Odd digits:", odd_count)

    if even_count > odd_count:
        print("Even occurs more")
    elif odd_count > even_count:
        print("Odd occurs more")
    else:
        print("Equal")

print()


print("7. Repeated Character Report")

text = input("Enter a string: ")
checked = ""

for ch in text:
    if ch not in checked:
        total = 0

        for x in text:
            if ch == x:
                total = total + 1

        if total > 1:
            if total == 2:
                print(ch, "-", total, "-", "Duplicate")
            elif total <= 4:
                print(ch, "-", total, "-", "Repeated")
            else:
                print(ch, "-", total, "-", "Highly Repeated")

        checked = checked + ch

print()


print("8. Shopping Cart Analyzer")

total_amount = 0
budget_count = 0
regular_count = 0
premium_count = 0
luxury_count = 0

for i in range(1, 9):
    price = float(input("Enter price of product " + str(i) + ": "))
    total_amount = total_amount + price

    if price < 500:
        print("Budget")
        budget_count = budget_count + 1
    elif price <= 1999:
        print("Regular")
        regular_count = regular_count + 1
    elif price <= 4999:
        print("Premium")
        premium_count = premium_count + 1
    else:
        print("Luxury")
        luxury_count = luxury_count + 1

average_price = total_amount / 8

print("Total amount:", total_amount)
print("Budget products:", budget_count)
print("Regular products:", regular_count)
print("Premium products:", premium_count)
print("Luxury products:", luxury_count)
print("Average product price:", average_price)
print()


print("9. Character Position Challenge")

text = input("Enter a string: ")

vowel_count = 0
consonant_count = 0
digit_count = 0
special_count = 0

for i in range(len(text)):
    ch = text[i]
    position = i + 1

    if position % 2 == 0:
        pos_type = "Even position"
    else:
        pos_type = "Odd position"

    if ch in vowels:
        char_type = "Vowel"
        vowel_count = vowel_count + 1
    elif ch.isalpha():
        char_type = "Consonant"
        consonant_count = consonant_count + 1
    elif ch.isdigit():
        char_type = "Digit"
        digit_count = digit_count + 1
    else:
        char_type = "Special character"
        special_count = special_count + 1

    print(ch, "-", position, "-", pos_type, "-", char_type)

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
print()


print("10. Number Pattern With Conditions")

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 3 == 0 and j % 5 == 0:
            print("Z", end=" ")
        elif j % 3 == 0:
            print("X", end=" ")
        elif j % 5 == 0:
            print("Y", end=" ")
        else:
            print(j, end=" ")
    print()
