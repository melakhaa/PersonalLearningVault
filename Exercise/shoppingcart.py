item = str(input("Enter an item: "))
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

cost = quantity * price 

print(f"Total cost for {quantity} {item} is: $ {cost}")
