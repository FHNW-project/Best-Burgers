import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_ingredients(filename="csv lists/ingredients.csv"):
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
    #print buns list 
    print("Which bun do you want?")
    for number, item in buns.items():
        print (f"{number}. {item['name']} - CHF {item['price']:.2f} - {item['calories']} Kcal - Allergens: {item['allergens']}")
    #choice of the buns
    choice = input("Enter the number of your desired Bun: ").strip()
    while choice not in buns:
        print("Invalid choice, please be aware that only digits are accepted.")
        choice = input("Enter the number of your desired Bun: ").strip()
    #adding the selected bun to the ingredient list
    customburger_ingredients.append(buns[choice]["name"])
    print("")
    print("------------")
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

    #choice if customer desire a patty or not
    patty_choice = input("Would you like to add a patty to your burger? yes/no").strip().lower()
    # if yes print list of the patties
    if patty_choice == "yes" or "y" or "ye":
        for number, item in patties.items():
            print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")
    #choice of the patties
        choice = input("Enter the number of the desired Patty:").strip()
        while choice not in patties:
            print("Invalid choice, please be aware that only digits are accepted.")
            choice = input("Enter the number of the desired Bun:").strip()
    #adding the selected patty to the ingredient list
        customburger_ingredients.append(patties[choice]["name"])
        print("")
        print("------------")
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("")
    print("------------")
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

    #choice if customer want cheese or not
    print("Would you like to add a slice of cheese to your Burger? yes/no")
    cheese_choice = input("").strip().lower()
    #print of the list of available cheese
    if cheese_choice == "yes" or "ye" or "y":
        for number, item in cheeses.items():
            print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal -  Allergens: {item["allergens"]}")
    #choice of the cheese
        choice = input("Enter the corresponding number of the desired type of Cheese: ").strip()
        while choice not in cheeses:
            print ("Invalid choicce, please be aware that only digits are accepted.")
            choice = input("Enter the corresponding number of the desired type of Cheese: ").strip()
    #adding the selected cheese to the ingredient list
        customburger_ingredients.append(cheeses[choice]["name"])
        print("")
        print("------------")
    print("")
    print("------------")
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")




#code lines to test the definition
print("Let's create your Dream's Burger!")
place_order = customburger_function()
burger_order = (f'Burger ingredients:{", ".join(place_order)}.')