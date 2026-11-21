import sys
import csv
from pathlib import Path

LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

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

def side_function(price_factor = 1.0, nutrition_factor = 1.0):
    #beginning side order
    print("Which of the following Sides do you want?")
    print("")
    #printing the list of the available Sides
    for number, item in sides_menu.items():
        real_price = item["price"]*price_factor
        real_calories = item["calories"]*nutrition_factor
        print (f"{number}. {item["name"]} - CHF {real_price:,.2f} - {real_calories} Kcal - Allergens: {item["allergens"]}")

    #choise of the desired Side
    print("")
    side_choice = input(f"Enter the number of the desired Side:\n").strip().lower()
    while side_choice not in sides_menu:
        print("")
        print("Invalid choice, be aware that only digits can be entered.")
        side_choice = input(f"Enter the number of the desired Side:\n").strip().lower()
    chosen = sides_menu[side_choice]
    print(f"\n{LINE}")
    print(f"Perfect, you choose {chosen["name"]} for {chosen["price"]:,.2f} CHF.")
    print(f"{LINE}\n")
    return{
        "type": "Side",
        "name": chosen["name"], 
        "price": float(chosen["price"]), 
        "nutritional_value": {
            "calories": float(chosen["calories"]), 
            "fat": float(chosen["fat"]), 
            "sugar": float(chosen["sugar"]), 
            "protein": float(chosen["protein"]), 
            "fiber": float(chosen["fiber"]),
        },
    }
