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
    bun_choice = input("Enter the number of your desired Bun: ").strip()
    while bun_choice not in buns:
        print("Invalid choice, please be aware that only digits are accepted.")
        bun_choice = input("Enter the number of your desired Bun: ").strip()
    #adding the selected bun to the ingredient list
    customburger_ingredients.append(buns[bun_choice]["name"])
    print("")
    print("------------")
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

    #choice if customer desire a patty or not
    patty_question = input(f"Would you like to add a patty to your burger? yes/no:\n").strip().lower()
    # if yes print list of the patties
    while patty_question in ("yes" or "y" or "ye"):
        for number, item in patties.items():
            print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")
    #choice of the patties
        patty_choice = input("Enter the number of the desired Patty:").strip()
        while patty_choice not in patties:
            print("Invalid choice, please be aware that only digits are accepted.")
            patty_choice = input("Enter the number of the desired Bun:").strip()
    #adding the selected patty to the ingredient list
        customburger_ingredients.append(patties[patty_choice]["name"])
        print("")
        print("------------")
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
        print("")
        print("------------")
        patty_question = input(f"Would you like to add another patty to your burger? yes/no:\n").strip().lower()
    print("")
    print("------------")
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

    #choice if customer want cheese or not
    cheese_question = input(f"Would you like to add a slice of cheese to your Burger? yes/no:\n").strip().lower()
    #print of the list of available cheese
    while cheese_question in ("yes" or "ye" or "y"):
        for number, item in cheeses.items():
            print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal -  Allergens: {item["allergens"]}")
    #choice of the cheese
        cheese_choice = input("Enter the corresponding number of the desired type of Cheese: ").strip()
        while cheese_choice not in cheeses:
            print ("Invalid choice, please be aware that only digits are accepted.")
            cheese_choice = input("Enter the corresponding number of the desired type of Cheese: ").strip()
    #adding the selected cheese to the ingredient list
        customburger_ingredients.append(cheeses[cheese_choice]["name"])
        print("")
        print("------------")
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
        print("------------")
        print("")
        cheese_question = input(f"Would you like to add another slice of cheese to your Burger? yes/no:\n").strip().lower()
    print("")
    print("------------")
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

    #choice if customer want a vegetables or not
    vegetable_question = input(f"Would you like to add vegetables to your Burger? Yes/No:\n").strip().lower()
    #print list of available vegetables
    while vegetable_question in ("yes" or "ye" or "y"):
        for number, item in vegetables.items():
            print(f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal -  Allergens: {item["allergens"]}")
    #choice of the vegetables
        vegetable_choice = input(f"Enter the number of the desired vegetables:\n").strip().lower()
        while vegetable_choice not in vegetables:
            print("Invalid choice, please be aware that only digits are accepted.")
            vegetable_choice = input(f"Enter the number of the desired vegetables:\n").strip().lower()
        #adding the selected vegetables to the ingredient list
        customburger_ingredients.append(vegetables[vegetable_choice]["name"])
        print("")
        print("------------")
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
        print("------------")
        print("")
        vegetable_question = input(f"Would you like to add another vegetables to your Burger? yes/no:\n").strip().lower()
    print("")
    print("------------")
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print("------------")
    print("")

    #choice if customer want a sauce or not
    sauce_question = input(f"Would you like to add a sauce to your burger? Yes/No:\n").strip().lower()
    #print list of available sauces
    while sauce_question in ("yes" or "ye" or "y"):
        for number, item in sauces.items():
            print(f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")
    #choice of the sauce
        sauce_choice = input(f"Enter the number of the desired sauce:\n").strip().lower()
        while sauce_choice not in sauces:
            print("Invalid choice, please be aware that only digits are accepted.")
            sauce_choice = input(f"Enter the number of the desired sauce:\n").strip().lower()


    





#code lines to test the definition
print("Let's create your Dream's Burger!")
place_order = customburger_function()
burger_order = (f'Burger ingredients:{", ".join(place_order)}.')