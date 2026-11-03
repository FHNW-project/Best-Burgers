import csv

def load_ingredients(filename="ingredients.csv"):
    ingredients = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"] = float(row["price"])
            row["calories"]=int(row["calories"])
            ingredients.append(row)
    return ingredients

ingredients = load_ingredients()

def menu_for(category):
    items = [i for i in ingredients if i["category"] == category]
    return {str(number): item for number, item in enumerate(items, start=1)}

buns = menu_for("bun")
patties = menu_for("patty")
cheeses = menu_for("cheese")
vegetables = menu_for("vegetable")
sauces = menu_for("sauce")

#---------

def customburger_function():
    customburger_ingredients=[]

    #beginning custom order
    #print buns list and choose 
    print("Which bun do you want?")
    for number, item in buns.items():
        print (f"{number}. {item['name']} - CHF {item['price']:.2f} - {item['calories']} Kcal - Allergens: {item['allergens']}")

    choice = input("Enter the number of your desired Bun: ").strip()
    while choice not in buns:
        print("Invalid choice, please be aware that only digits are accepted.")
        choice = input("Enter the number of your desired Bun: ").strip()

    customburger_ingredients.append(buns[choice]["name"])
    print("")
    print("------------")
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

