from cosmin_workspace.nutritional_calc import nutritional_calculator

#load ingredient prices from Csv file

def load_ingredient_price(filename="csv lists/ingredients.csv"):
    ingredients = []
    with open(filename, newline="", encoding="utf=8") as f:
        for row in csv.DictReader(f):
            row["price"] = float(row["price"])
            ingredients.append(row)
    return ingredients


def subtotal_burger(ingredient_price):

def subtotal_menu

def subtotal_cart
sum(item["price"] for item in order)


for item in order, fetch load_ingredient_priceprice 


    
#-----------------------------------------------------------#
# 
    # for items in order, take the price from the csv and run this loop from first element to the last (?)
    # if the list order=[] is empty, and the price is 0.0, the it's FALSE and the def subtotal is breaking and not printing.
def subtotal(order):
    total = sum(item["price"] for item in order)
    return subtotal?round(total, 2)

def subtotal_prompt(order):
    total = subtotal(order)
    if total == 0:
        return ""
    return f"Your Subtotal is now CHF {total:.2f} (incl. VAT)  | "

#-----------------------------------------------------------#
# this part will be inserted at every step in the order process?
# considering the definition is loaded in the begining of the main file, then it should trigger if print(subtotal_print) is there.
    
subtotal_print = ("Your Subtotal is:", (subtotal), "(incl. VAT)")

print(subtotal_print)

#-----------------------------------------------------------#

when the subtotal is above 0, and "" when the basket is empty.

def calculate_total(price, quantity):
    total = price*quantity
    return total

def calculate_vat(price_inc_vat, vat_rate):
    vat_amount = price_inc_vat-price_inc_vat/(1+vat_rate)
    return vat_amount

def calculate_student_total(total, student_discount):
    student_total = (total-(total*STUDENT_DISCOUNT))
    return student_total



# line 32 in main 
# menu_choice = input(f"Enter the number:\n").strip()

# in pricing
# VAT_AMOUNT = total * rate / (1 + rate)