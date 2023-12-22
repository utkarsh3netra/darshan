menu = [
    {"name": "Spaghetti Carbonara", "price": 12, "ingredients": ["tomato", "pasta", "egg", "bacon"]},
    {"name": "Margherita Pizza", "price": 10, "ingredients": ["dough", "tomato", "cheese", "meat"]},
    {"name": "Salmon Salad", "price": 15, "ingredients": ["tomato", "salmon", "lettuce", "dressing"]},
    {"name": "Vegetable Stir Fry", "price": 8, "ingredients": ["tomato", "broccoli", "carrot", "pepper"]}
]
print(menu)
# 1 task
high_dish = menu[0]
for dish in menu[1:]:
    if dish["price"] > high_dish["price"]:
        high_dish = dish

print("\nhighest price dish is", high_dish)

# 2 task
veg_dish = []
for dish in menu:
    veg = True
    for ingredient in dish["ingredients"]:
        if ingredient in ["meat", "fish"]:
            veg = False
            break
    if veg:
        veg_dish.append(dish["name"])

print("\nVeg dish is", veg_dish)

# 3 task
ingredient_frequency = {}

for dish in menu:
    for ingredient in dish["ingredients"]:
        if ingredient in ingredient_frequency:
            ingredient_frequency[ingredient] += 1
        else:
            ingredient_frequency[ingredient] = 1

print("\ningredient frequency is : ", ingredient_frequency)
