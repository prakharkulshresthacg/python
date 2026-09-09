cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if cost_price <= 0:
    print("Invalid cost price")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percent = profit / cost_price * 100
    print("Profit percentage =", profit_percent)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percent = loss / cost_price * 100
    print("Loss percentage =", loss_percent)
else:
    print("No profit and no loss")
