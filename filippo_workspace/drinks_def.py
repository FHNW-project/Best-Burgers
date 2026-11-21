import sys
import csv
from pathlib import Path

##### USER INTERFACE ELEMENTS #####
LINE = "="*50
##### USER INTERFACE ELEMENTS #####

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

#formatting the line of the drinks and append it to drinks
def load_drinks(filename="csv lists/drinks.csv"):
    drinks = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"]= float(row["price"])
            row["calories"]= int(row["calories"])
            drinks.append(row)
    return drinks

drinks = load_drinks()
#creating the drinks menu and giving a sequence number to the drinks
def drinks_menu_for():
    return{str(number): item for number, item in enumerate(drinks, start=1)}
drinks_menu = drinks_menu_for()

#def ordering drinks
def drinks_function(price_factor = 1.0, nutrition_factor = 1.0):
    #beginning drinks order
    print("Which of the following drink do you want?")
    print("")
    #printing the list of the available drinks
    for number,item in drinks_menu.items():
        real_price = item["price"]*price_factor
        real_calories = item["calories"]*nutrition_factor
        print (f"{number}. {item["name"]} - CHF {real_price:,.2f} - {real_calories} Kcal - Allergens: {item["allergens"]}")
    #choice of the desired drinks
    print("")
    drinks_choice= input(f"Enter the number of the desired Drink:\n").strip()
    print(f"\n{LINE}")
    while drinks_choice not in drinks_menu:
        print("")
        print("Invalid choice, be aware that only the digits in the list can be enter.")
        drinks_choice=input(f"Enter the number of the desired Drink:\n").strip()
        print(f"\n{LINE}")

    chosen= drinks_menu[drinks_choice]
    print(f"Perfect, you choose {chosen["name"]} for {chosen["price"]:,.2f} CHF.")
    print(f"{LINE}\n")
    return {
        "type": "drink",
        "name": chosen["name"], 
        "price": chosen["price"], 
        "nutritional_value": {
            "calories": float(chosen["calories"]), 
            "fat": float(chosen["fat"]), 
            "sugar": float(chosen["sugar"]), 
            "protein": float(chosen["protein"]), 
            "fiber": float(chosen["fiber"])
        },  
    }
