menu = {"pizza":65,
        "nacho":96.5,
        "sandwich": 41.3,
        "water":5,
        "chips":34,
        "soda":6}

cart = []
total = 0

print("--------- Menu ---------")

for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("------------------------")

while True:
    food = input("Please enter food: (press q to quite): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- Total ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is ${total:.2f}")