balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Withdrawal amount must be greater than 0")
elif amount % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < 500:
    print("Cannot withdraw. Minimum balance of 500 must remain")
else:
    print("Withdrawal successful")
    print("Remaining balance:", balance - amount)
