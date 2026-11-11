import csv

nutritional_values = {}

with open ("data/ingredients.csv", mode="r", encoding="utf-8") as ingredient_file:
    ingredient_reader = csv.DictReader(ingredient_file)
    for one_ingredient in ingredient_reader:
        ingredient_id = one_ingredient["id"]
        one_ingredient["calories"] = float(one_ingredient["calories"])
        one_ingredient["fat"] = float(one_ingredient["fat"])
        one_ingredient["sugar"] = float(one_ingredient["sugar"])
        one_ingredient["protein"] = float(one_ingredient["protein"])
        one_ingredient["fiber"] = float(one_ingredient["fiber"])
        nutritional_values[ingredient_id] = one_ingredient
# print(nutritional_values["bun_sesame"]["fat"])+(nutritional_values["patty_beef"]["fat"])

def nutritional_calculator(ingredients_id):
    nutrient_total = {
        "calories": 0, 
        "fat": 0, 
        "sugar": 0, 
        "protein": 0, 
        "fiber": 0
        }
    for ingredient_id in ingredients_id:
        ingredient_row = nutritional_values[ingredient_id]
        nutrient_total["calories"] = nutrient_total["calories"] + ingredient_row["calories"]
        nutrient_total["fat"] = nutrient_total["fat"] + ingredient_row["fat"]
        nutrient_total["fiber"] = nutrient_total["fiber"] + ingredient_row["fiber"]
        nutrient_total["protein"] = nutrient_total["protein"] + ingredient_row["protein"]
        nutrient_total["sugar"] = nutrient_total["sugar"] + ingredient_row["sugar"]
    return nutrient_total

# test function print(nutritional_calculator(["bun_sesame", "patty_beef", "cheese_emmental"]))