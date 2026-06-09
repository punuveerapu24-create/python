foods = []
prices = []
sum = 0
while True:
    food = input("Enter a food (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price of the {food}: "))

        foods.append(food)
        prices.append(price)

print("YOUR CART:")

for food in foods:
    print(food, end=" ")

for price in prices:
    sum += price

print()
print(sum)

