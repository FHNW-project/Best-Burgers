VAT_NORMAL = 0.081
VAT_REDUCED = 0.026
VAT_NONE = 0.0
STUDENT_DISCOUNT = 0.15

##### USER INTERFACE ELEMENTS #####
LINE = "-"*50

#-----------------------------------------------------------#

def subtotal(order):
    total = sum(item["price"] for item in order)
    return round(total, 2)


def subtotal_prompt(order):
    total = subtotal(order)
    if total == 0:
        return ""
    return f"Your Subtotal is now: CHF {total:.2f} (incl. VAT)  "
