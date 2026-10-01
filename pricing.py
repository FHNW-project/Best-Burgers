VAT_NORMAL = 0.081
VAT_REDUCED = 0.026
VAT_NONE = 0.0
STUDENT_DISCOUNT = 0.15


def calculate_total(price, quantity):
    total = price*quantity
    return total

def calculate_vat(price_inc_vat, vat_rate):
    vat_amount = price_inc_vat-price_inc_vat/(1+vat_rate)
    return vat_amount

def calculate_student_total(total, discount)
    student_total = (total-(total*STUDENT_DISCOUNT))
    return student_total

