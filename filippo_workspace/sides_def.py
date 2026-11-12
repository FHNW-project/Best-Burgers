import sys
import csv
from pathlib import Path

nextstep = "Then let's go to the next step!"
burgercomplete = "Perfect, you have finished your Dream's Burger. This are the ingredients that you choose:"
LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from cosmin_workspace.nutritional_calc import nutritional_calculator

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

def side_function():
    
    #beginning side order
    print("Which of the following Sides do you want?")
    #printing the list of the available Sides
    for number, item in sides_menu.items():
        print (f"{number}. {item["name"]} - CHF {item["price"]:.2f} - {item["calories"]} Kcal - Allergens: {item["allergens"]}")

    #choise of the desired Side
    side_choice = input(f"Enter the number of the desired Side:\n").strip().lower()
    while side_choice not in sides_menu:
        print("Invalid choice, be aware that only digits can be entered.")
        side_choice = input(f"Enter the number of the desired Side:\n").strip().lower()
    print(LINE)
    print(f"Perfect, you choose {sides_menu[side_choice]["name"]}.")
