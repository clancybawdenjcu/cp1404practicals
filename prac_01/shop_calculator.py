total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    price = float(input(f"Price of item {i}: "))
    total_price += price
if total_price > 100:
    total_price *= 1.1  # apply 10% discount if total equals over $100
print(f"Total price for {number_of_items} items is: ${total_price:.2f}")
