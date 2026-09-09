amount = float(input("Enter purchase amount: "))

if amount < 500:
    discount_percent = 0
elif amount <= 999:
    discount_percent = 5
elif amount <= 1999:
    discount_percent = 10
elif amount <= 4999:
    discount_percent = 15
else:
    discount_percent = 20

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount

print("Original amount:", amount)
print("Discount percentage:", discount_percent)
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)
