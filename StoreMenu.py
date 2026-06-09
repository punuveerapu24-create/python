
menu = {"popcorn": 130,
        "nachos": 100,
        "soda": 50,
        "fires": 80,
        "candy": 60,
        "maaza": 70,
        "pepsi": 50,
        }
Cart = []
total = 0

print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:10} : {value}")
print("------------------")
while True:
    food = input("Enter the food item you want to order (or 'q' to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        Cart.append(food)
print("-------CART-------")
for food in Cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total: {total}")