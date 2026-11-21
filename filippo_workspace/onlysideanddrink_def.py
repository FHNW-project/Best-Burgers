import sys
import csv
from pathlib import Path
import filippo_workspace
import extradef
LINE = "="*50

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))


def onlyside_function():
    size = extradef.choose_size()
    side = filippo_workspace.sides_def.side_function(size["price_factor"], size["nutrition_factor"])
    return filippo_workspace.extradef.side_size(side, size)

def side_size(side, size):
    price = side["price"]*size["price_factor"]
    nutrition = extradef.add_nutrition(
        extradef.scale_nutrition(side["nutritional_value"], size["nutrition_factor"])
    )
    return{
        "type": "side",
        "name": f"{side["name"]} ({size['size']})",
        "size": size["size"],
        "price": round(price, 2),
        "nutritional_value": {name: round(value, 1) for name, value in nutrition.items()},

    }
