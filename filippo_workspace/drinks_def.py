import sys
import csv
from pathlib import Path

nextstep = "Then let's go to the next step!"
burgercomplete = "Perfect, you have finished your Dream's Burger. This are the ingredients that you choose:"
LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from cosmin_workspace.nutritional_calc import nutritional_calculator
#formatting the line of the drinks and append it to drinks
def load_drinks(filename="csv lists/drinks.csv"):
    drinks = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"]= float(row["price"])
            row["calories"]= int(row["calories"])
            drinks.append
    return drinks

drinks = load_drinks()
#creating the drinks menu and giving a sequence number to the drinks
def drinks_menu_for():
    return{str(number): item for number, item in enumerate(drinks, start=1)}
drinks_menu = drinks_menu_for()

#def ordering drinks
def drinks_function():
    #beginning drinks order
    print("Which of the following drink do you want?")
    #printing the list of the available drinks
    for number,item in drinks_menu.items():
        print(f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")

    #choise of the desired drinks
    drinks_choice= input(f"Enter the number of the desired Drink:\n")
    while drinks_choice not in drinks_menu:
        print("Invalid choice, be aware that only the digits in the list can be enter.")
        drinks_choice=input(f"Enter the number of the desired Drink:\n")

    chosen= drinks_menu[drinks_choice]
    print(LINE)
    print(f"Perfect, you choose {chosen["name"]}.")
    return {"type": "side", "name": chosen["name"]}