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
# for testing: print(nutritional_values["bun_sesame"]["fat"])