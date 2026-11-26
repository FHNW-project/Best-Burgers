VAT_NORMAL = 0.081
VAT_REDUCED = 0.026
VAT_NONE = 0.0
STUDENT_DISCOUNT = 0.15
STUDENT_ID = "12345"

##### USER INTERFACE ELEMENTS #####
LINE = "-"*50

#-----------------------------------------------------------#

# US-5: SUBTOTAL at every step @Andrei Oros

def subtotal(order):
    total = sum(item["price"] for item in order)
    return round(total, 2)


def subtotal_prompt(order):
    total = subtotal(order)
    if total == 0:
        return ""
    return f"Your Subtotal is now: CHF {total:.2f} (incl. VAT)  "


def subtotal_burger(ingredient_ids, ingredients_by_id):
    total = round(sum(ingredients_by_id[i]["price"] for i in ingredient_ids), 2)
    if total == 0:
        return ""
    return f"Your Burger Subtotal is now: CHF {total:.2f} (incl. VAT)  "
