import csv

def load_ingredients(filename="ingredients.csv"):
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

