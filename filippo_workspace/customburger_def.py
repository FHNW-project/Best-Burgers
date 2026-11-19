import sys
import csv
from pathlib import Path
from . import extradef
from cosmin_workspace.nutritional_calc import nutritional_calculator

question = extradef.ask_yes_no
nextstep = "Then let's go to the next step!"
burgercomplete = "Perfect, you have finished your Dream's Burger. This are the ingredients that you choose:"
LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

#load ingredients from Csv file
def load_ingredients(filename="csv lists/ingredients.csv"):
    ingredients = []
    try:
        with open(filename, newline="", encoding="utf=8") as f:
            for row in csv.DictReader(f):
                row["price"] = float(row["price"])
                row["calories"]=int(row["calories"])
                ingredients.append(row)
        return ingredients
    except:
        print("Upss, file is disappeared.")

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

def customburger_recap(ingredients, ids):
    nutritional_value = nutritional_calculator(ids)
    price = sum(ingredients_by_id[i]["price"] for i in ids)
    print("")
    print(LINE)
    print(f"Ingredient List:\n{", ".join(ingredients)}.")
    print(f"Total calories: {nutritional_value["calories"]:,.0f} Kcal - Fat {nutritional_value["fat"]:,.1f} - Sugar: {nutritional_value["sugar"]:,.1f} - Protein: {nutritional_value["protein"]:,.1f} - Fiber: {nutritional_value["fiber"]:,.1f}")
    print(f"Total: {price:,.2f} CHF")
    print(LINE)
    print("")
    return price, nutritional_value

def customburger_function():
    customburger_ingredients=[]
    ingredients_ids=[]

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
    ingredients_ids.append(buns[bun_choice]["id"])
    burger_recap = customburger_recap(customburger_ingredients, ingredients_ids)

    #choice if customer desire a patty or not
    patty_question = question(f"Would you like to add a patty to your burger? yes/no:\n")
    # if yes print list of the patties
    while patty_question:
        for number, item in patties.items():
            print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")
    #choice of the patties
        patty_choice = input("Enter the number of the desired Patty:").strip()
        while patty_choice not in patties:
            print("Invalid choice, please be aware that only digits are accepted.")
            patty_choice = input("Enter the number of the desired patty:").strip()
    #adding the selected patty to the ingredient list
        customburger_ingredients.append(patties[patty_choice]["name"])
        ingredients_ids.append(patties[patty_choice]["id"])
        burger_recap = customburger_recap(customburger_ingredients, ingredients_ids)

        patty_question = question(f"Would you like to add another patty to your burger? yes/no:\n")
    print("")
    print(LINE)
    print(nextstep)
    print("")

    #choice if customer want cheese or not
    cheese_question = question(f"Would you like to add a slice of cheese to your Burger? yes/no:\n")
    #print of the list of available cheese
    while cheese_question:
        for number, item in cheeses.items():
            print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal -  Allergens: {item["allergens"]}")
    #choice of the cheese
        cheese_choice = input("Enter the corresponding number of the desired type of Cheese: ").strip()
        while cheese_choice not in cheeses:
            print ("Invalid choice, please be aware that only digits are accepted.")
            cheese_choice = input("Enter the corresponding number of the desired type of Cheese: ").strip()
    #adding the selected cheese to the ingredient list
        customburger_ingredients.append(cheeses[cheese_choice]["name"])
        ingredients_ids.append(cheeses[cheese_choice]["id"])
        burger_recap = customburger_recap(customburger_ingredients, ingredients_ids)
        cheese_question = question(f"Would you like to add another slice of cheese to your Burger? yes/no:\n")
    print("")
    print(LINE)
    print(nextstep)
    print("")

    #choice if customer want a vegetables or not
    vegetable_question = question(f"Would you like to add vegetables to your Burger? Yes/No:\n")
    #print list of available vegetables
    while vegetable_question:
        for number, item in vegetables.items():
            print(f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal -  Allergens: {item["allergens"]}")
    #choice of the vegetables
        vegetable_choice = input(f"Enter the number of the desired vegetables:\n").strip().lower()
        while vegetable_choice not in vegetables:
            print("Invalid choice, please be aware that only digits are accepted.")
            vegetable_choice = input(f"Enter the number of the desired vegetables:\n").strip().lower()
        #adding the selected vegetables to the ingredient list
        customburger_ingredients.append(vegetables[vegetable_choice]["name"])
        ingredients_ids.append(vegetables[vegetable_choice]["id"])
        burger_recap = customburger_recap(customburger_ingredients, ingredients_ids)
        vegetable_question = question(f"Would you like to add another vegetable to your Burger? yes/no:\n")
    print("")
    print(LINE)
    print(nextstep)
    print("")

    #choice if customer want a sauce or not
    sauce_question = question(f"Would you like to add a sauce to your burger? Yes/No:\n")
    #print list of available sauces
    while sauce_question:
        for number, item in sauces.items():
            print(f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")
    #choice of the sauce
        sauce_choice = input(f"Enter the number of the desired sauce:\n").strip().lower()
        while sauce_choice not in sauces:
            print("Invalid choice, please be aware that only digits are accepted.")
            sauce_choice = input(f"Enter the number of the desired sauce:\n").strip().lower()
        #adding the selected sauce to the ingredient list
        customburger_ingredients.append(sauces[sauce_choice]["name"])
        ingredients_ids.append(sauces[sauce_choice]["id"])
        burger_recap = customburger_recap(customburger_ingredients, ingredients_ids)
        sauce_question = question(f"Would you like to add another sauce to your burger? Yes/No:\n")
    
    custom_calories = nutritional_calculator(ingredients_ids)
    burger_price = sum(ingredients_by_id[i]["price"] for i in ingredients_ids)

    burger_recap = customburger_recap(customburger_ingredients, ingredients_ids)

    return{
         "type": "burger",
         "name": "Custom burger",
         "price": burger_price,
         "ingredients": customburger_ingredients,
         "nutritional_value": custom_calories
    }
#---------------------------
# End of the definition for custom made burger

                    