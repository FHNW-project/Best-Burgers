import sys
import csv
from pathlib import Path
import filippo_workspace

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
LINE = "="*50

#load the sizes from the csv file and changing the format from text to float number
def load_sizes(filename="csv lists/sizes.csv"):
    sizes=[]
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["nutrition_factor"] = float(row["nutrition_factor"])
            row["price_factor"]= float(row["price_factor"])
            sizes.append(row)
    return sizes
#creation of the dictionary for sizes
sizes= load_sizes()
size_menu = {str(number): item for number, item in enumerate(sizes, start=1)}

#def to choose the size
def choose_size():
    print("")
    print(f"Which size do you want?\n")
    #printing the list of the available sizes
    for number, size in size_menu.items():
        print(f"{number}. {size["size"]}")
    #asking the customer to enter the number of the choose size
    size_choice = input(f"\nEnter the number of the desired size:\n").strip()
    while size_choice not in size_menu:
        print("Invalid choice, please enter one of the number listed in the menu.")
        size_choice = input(f"Enter the number of the desired size\n").strip()
    print(f"{LINE}\n")
    return size_menu[size_choice]

def scale_nutrition(nutrition, factor):
    return {name: value * factor for name, value in nutrition.items()}

def add_nutrition(*nutritions):
    total = {}
    for nutrition in nutritions:
        for name, value in nutrition.items():
            total[name] = total.get(name, 0) + value
    return total


def ask_yes_no(question):
    answer= input(question).strip().lower()
    while answer not in ("yes", "ye", "y", "no", "n"):
        print("")
        print("Invalid choice, please answer yes or no.")
        answer= input(question).strip().lower()
    return answer in ("yes", "ye", "y")

def make_menu(burger,side,drink,size):
    price = burger["price"]+(side["price"]+drink["price"])*size["price_factor"]

    nutrition = add_nutrition(
        burger["nutritional_value"],
        scale_nutrition(side["nutritional_value"], size["nutrition_factor"]),
        scale_nutrition(drink["nutritional_value"], size["nutrition_factor"]),
    )
    
    return{
        "type": "menu",
        "size": size["size"],
        "burger": burger,
        "side": side,
        "drink": drink,
        "price": round(price, 2),
        "nutritional_value": {name: round(value, 1) for name, value in nutrition.items()}
    }

def menu_function(burger):
     size = choose_size()
     side = filippo_workspace.sides_def.side_function(size["price_factor"], size["nutrition_factor"])
     drink = filippo_workspace.drinks_def.drinks_function(size["price_factor"], size["nutrition_factor"])
     return make_menu(burger, side, drink, size)