# USER STORIES 1 - 2 - 3
import 
import csv
from pathlib import Path

LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent

#load ingredients from Csv file
def load_ingredients(filename="csv lists/ingredients.csv"):
    ingredients = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"] = float(row["price"])
            row["calories"]=int(row["calories"])
            ingredients.append(row)
    return ingredients

#connecting the ingredient by the id to the ingredient name
ingredients = load_ingredients()
ingredients_by_id = {i["id"]: i for i in ingredients}

#splitting the ingredients by category
def menu_for(category):
    items = [i for i in ingredients if i["category"] == category]
    return {str(number): item for number, item in enumerate(items, start=1)}

#associating the list of the ingredients to the respective name
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
    bun_choice = input(f"Enter the number of your desired Bun:\n").strip()
    while bun_choice not in buns:
        print("Invalid choice, please be aware that only digits are accepted.")
        bun_choice = input("Enter the number of your desired Bun: ").strip()
    #adding the selected bun to the ingredient list
    customburger_ingredients.append(buns[bun_choice]["name"])
    print("")
    print(LINE)
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print(LINE)
    print("")

    #choice if customer desire a patty or not
    patty_question = input(f"Would you like to add a patty to your burger? yes/no:\n").strip().lower()
    while patty_question not in ("yes","ye","y","no","n"):
        print("Invalice answer, please enter only Yes or No, other terms will not be accepted.")
        patty_question = input(f"Would you like to add a patty to your burger? yes/no:\n").strip().lower()

    # if yes print list of the patties
    while patty_question in ("yes","y","ye"):
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
        print(LINE)
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
        print(LINE)
        print("")
        patty_question = input(f"Would you like to add another patty to your burger? yes/no:\n").strip().lower()
        while patty_question not in ("yes","ye","y","no","n"):
            print("Invalice answer, please enter only Yes or No, other terms will not be accepted.")
            patty_question = input(f"Would you like to add another patty to your burger? yes/no:\n").strip().lower()
        
    print("")
    print(LINE)
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print(LINE)
    print("")

    #choice if customer want cheese or not
    cheese_question = input(f"Would you like to add a slice of cheese to your Burger? yes/no:\n").strip().lower()
    while cheese_question not in ("yes","ye","y","no","n"):
        print("Invalid answer, please enter only Yes or No, other terms will not be accepted.")
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
        print(LINE)
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
        print(LINE)
        print("")
        cheese_question = input(f"Would you like to add another slice of cheese to your Burger? yes/no:\n").strip().lower()
        while cheese_question not in ("yes","ye","y","no","n"):
            print("Invalid answer, please enter only Yes or No, other terms will not be accepted.")
            cheese_question = input(f"Would you like to add another slice of cheese to your Burger? yes/no:\n").strip().lower()
    print("")
    print(LINE)
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print(LINE)
    print("")

    #choice if customer want a vegetables or not
    vegetable_question = input(f"Would you like to add vegetables to your Burger? Yes/No:\n").strip().lower()
    while vegetable_question not in ("yes","ye","y","no","n"):
        print("Invalid answer, please enter only Yes or No, other terms will not be accepted.")
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
        vegetable_question = input(f"Would you like to add another vegetable to your Burger? yes/no:\n").strip().lower()
        while vegetable_question not in ("yes","ye","y","no","n"):
            print("Invalid answer, please enter only Yes or No, other terms will not be accepted.")
            vegetable_question = input(f"Would you like to add another vegetable to your Burger? Yes/No:\n").strip().lower()
    print("")
    print(LINE)
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print(LINE)
    print("")

    #choice if customer want a sauce or not
    sauce_question = input(f"Would you like to add a sauce to your burger? Yes/No:\n").strip().lower()
    while sauce_question not in ("yes","ye","y","no","n"):
        print("Invalid answer, please enter only Yes or No, other terms will not be accepted.")
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
        #adding the selected sauce to the ingredient list
        customburger_ingredients.append(sauces[sauce_choice]["name"])
        print("")
        print(LINE)
        print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
        print(LINE)
        print("")
        sauce_question = input(f"Would you like to add another sauce to your burger? Yes/No:\n").strip().lower()
        while sauce_question not in ("yes","ye","y","no","n"):
            print("Invalid answer, please enter only Yes or No, other terms will not be accepted.")
            sauce_question = input(f"Would you like to add another sauce to your burger? Yes/No:\n").strip().lower()
    print("")
    print(LINE)
    #printing list of ingredients
    print(f'Ingredient list:\n{", ".join(customburger_ingredients)}.')
    print(LINE)
    print("")
#---------------------------
# End of the definition for custom made burger





#----------------------------
# convert the presetburger.csv in a dictionary
def load_preset(filename="csv lists/preset_burgers.csv"):
    presetburger = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"] = float(row["price"])
            row["ingredient_ids"] = row["ingredient_ids"].split(";")
            presetburger.append(row)
    return presetburger

presetburger = load_preset()

def preset_menu_for():
    return {str(number): item for number, item in enumerate(presetburger, start=1)}

#definition to get the allergens information from the ingredients.csv and check if they are double or they don't have it
def presetburger_allergens(ids):
    found = set()
    for i in ids:
        for allergen in ingredients_by_id[i]["allergens"].split(";"):
            if allergen != "none":
                found.add(allergen)
    return sorted(found)

preset_menu = preset_menu_for()
#function to order the preset burger
def presetburger_function():
    #beggining preset order
    print("Which Preset Burger do you want?")
    #showing the list of the available Preset
    for number, burger in preset_menu.items():
        ids = burger["ingredient_ids"]
        names = ", ".join(ingredients_by_id[i]["name"] for i in ids)
        allergens = ", ".join(presetburger_allergens(ids)) or "none"
        print(f"{number}. {burger['name']} - CHF {burger['price']:.2f}")
        print(f" Ingredients: {names}")
        print(f" Allergens: {allergens}")
    
    #customer choose the preset burger
    presetburger_choice = input(f"Enter the number of the desired Burger:\n").strip()
    while presetburger_choice not in preset_menu:
        print("Invalid choice, please be aware that only digits are accepted.")
        presetburger_choice = input(f"Enter the number of the desired Burger:\n").strip()
    #printing the name of the preset burger that the customer choose
    print (f"Wonderful, you choose: {preset_menu[presetburger_choice]['name']}")
#-----------
# convert the sides.csv in a dictionary
def load_sides(filename="csv lists/sides.csv"):
    sides = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"] = float(row["price"])
            row["calories"] = int(row["calories"])
            sides.append(row)
    return sides

sides = load_sides()
#creating the menu for the sides
def sides_menu_for():
    return{str(number): item for number, item in enumerate(sides, start =1)}
sides_menu = sides_menu_for()






#code lines to test the definition
order_info = []
place_order = input ("Enter the number:")
 #Create your own burger
if place_order == "1":
        print("Let's create your Dream's Burger!")
        place_order = customburger_function()
        burger_order = (f'Burger ingredients:{", ".join(place_order)}.')
        order_info.append(burger_order)

    # Choose a preset burger
elif place_order == "2":
        place_order = presetburger_function()
        menu_question = input("Would you like to make a menu?")  
                 
else:
                    print("Only to Test the if")
                    