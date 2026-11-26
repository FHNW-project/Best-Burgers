import csv
from datetime import datetime
from pathlib import Path
import pricing

# US-9: SAVE ORDER TO INVOICE .CSV @Andrei Oros

# HERE ARE ALL THE VARIABLES PREPARED FOR THE SAVE_ORDER LOOP.

# HERE IS WHERE THE INVOICES WILL BE SAVED AS .CSV
ORDERS_FOLDER = Path(__file__).resolve().parent / "data" / "orders"

# EXTRA DETAILS FROM THE SHOP, FOR REALISM ONLY
STORE = "Best Burgers"
REGISTER = "1"
CASHIER = "Self-service"
PAYMENT = "default"

# .CSV file column separator
DELIMITER = ";"

# HERE WE ASSIGN or change THE VAT FOR PRODUCT CATEGORIES (from .CSV) 
VAT_RATES = {
    "burger": pricing.VAT_REDUCED,
    "menu": pricing.VAT_REDUCED,
    "side": pricing.VAT_REDUCED,    
    "drink": pricing.VAT_REDUCED,
}

# HERE IS THE SETUP FOR THE .CSV FILE (removed the item_id after item_no)
CSV_COLUMNS = [
    # order details (number and date are the most important)
    "order_number", "store", "register", "cashier", "date", "time", "customer",
    # item details (one item per row, item_no is the row number)
    "item_no", "item_name", "category", "size", "quantity", "unit_price", "vat_rate", "item_total", "ingredients",
    # financial details / order totals (the same on every row, only count from first row)
    "discount_rate", "subtotal", "discount", "total", "vat_amount", "payment_method", "rating",
]


# THIS CREATES AND RETURNS THE ORDER NUMBER FROM CURRENT DATE+TIME (Ex: order_20261122-160512)
def create_order_number(now):
    return f"order_{now:%Y%m%d-%H%M%S}" #order_year+month_day-hour+minute+second


# THIS RETURNS THE ITEM TYPE/CATEGORY 
def item_category(item):
    return item["type"].lower()


# THIS RETURNS THE NAME FOR EVERY ITEM IN ORDER
def item_name(item):
    if item_category(item) == "menu":
        return f"Menu: {item['burger']['name']} + {item['side']['name']} + {item['drink']['name']}"
    return item["name"]


# THIS RETURNS THE INGREDIENS OF CUSTOM_BURGER, OR JUST A BURGER
def item_ingredients(item):
    if item_category(item) == "menu":
        return item_ingredients(item["burger"])
    return ", ".join(item.get("ingredients", []))


# THIS CALCULATES THE ORDER TOTAL COST + VAT
def calculate_totals(order, discount_rate):
    subtotal = sum(item["price"] for item in order)
    discount = subtotal * discount_rate
    total = subtotal - discount

    # AND THIS CALCULATES AND RETURNS THE VAT_AMOUNT TO THE .CSV (based on the VAT_RATE) 
    vat_amount = 0
    for item in order:
        vat_rate = VAT_RATES[item_category(item)]
        paid_price = item["price"] * (1 - discount_rate)
        vat_amount += paid_price * vat_rate / (1 + vat_rate)
    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "total": round(total, 2),
        "vat_amount": round(vat_amount, 2),
    }


# THIS SETS UP THE FILE: calls the variables from above
# SAVES THEM IN THE ROWS OF THE .CSV, LOCATED IN ORDERS_FOLDER
# RETURNS THE ORDER NR AND PATH
def save_order(customer_name, order, discount_rate=0.0, folder=ORDERS_FOLDER):
    now = datetime.now()
    order_number = create_order_number(now)
    totals = calculate_totals(order, discount_rate)

    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"{order_number}.csv"

# NOW THE LOOP BEGINS:
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, delimiter=DELIMITER)
        writer.writeheader()
        for number, item in enumerate(order, start=1):
            quantity = item.get("quantity", 1)
            writer.writerow({
                "order_number": order_number,
                "store": STORE,
                "register": REGISTER,
                "cashier": CASHIER,
                "date": f"{now:%Y-%m-%d}",
                "time": f"{now:%H:%M:%S}",
                "customer": customer_name,
                "item_no": number,
                "item_name": item_name(item),
                "category": item_category(item),
                "size": item.get("size", ""),
                "quantity": quantity,
                "unit_price": f"{item['price']:.2f}",
                "vat_rate": VAT_RATES[item_category(item)],
                "item_total": f"{item['price'] * quantity:.2f}",
                "ingredients": item_ingredients(item),
                "discount_rate": discount_rate,
                "subtotal": f"{totals['subtotal']:.2f}",
                "discount": f"{totals['discount']:.2f}",
                "total": f"{totals['total']:.2f}",
                "vat_amount": f"{totals['vat_amount']:.2f}",
                "payment_method": PAYMENT,
                "rating": "",
            })

    return order_number, file_path