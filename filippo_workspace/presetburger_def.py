import sys
import csv
from pathlib import Path

nextstep = "Then let's go to the next step!"
burgercomplete = "Perfect, you have finished your Dream's Burger. This are the ingredients that you choose:"
LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from cosmin_workspace.nutritional_calc import nutritional_calculator

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
    chosen = preset_menu[presetburger_choice]
    chosencalories = nutritional_calculator(chosen["ingredient_ids"])

    print (f"Wonderful, you choose: {preset_menu[presetburger_choice]['name']}")
    print(f"{chosencalories['calories']:.0f} Kcal - Fat: {chosencalories['fat']:.1f} - Sugar: {chosencalories['sugar']:.1f} - Protein: {chosencalories['protein']:.1f} - Fiber {chosencalories['fiber']:.1f}")
    
    #printing the name of the preset burger that the customer choose
    