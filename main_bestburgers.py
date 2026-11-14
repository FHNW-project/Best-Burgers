# And this is how our first shared Python project begins :)
import filippo_workspace
from datetime import datetime


# This is how the order[] gets the name after complete_payment
def complete_payment():
    now = datetime.now()
    order_name = f"order_{now:%Y%m%d-%H%M}"
    return order_name

print("_______________________________")
print("                               ")
print("*** Welcome to Best Burgers ***")
print("_______________________________")
print("                                                                     ")
print(">>> I am here to guide you towards the Best Burgers you've ever had! <<<")
print("                                                                     ")
first_name = input("- What is your name? ")
print("                    ")
print (f"Hello {first_name}!")
print("                    ")
answer = input ("Would you like to place an order? (yes/no)")
place_order = ""
if answer.strip().lower() == "yes" or answer.strip().lower() == "y":
    place_order = input ("Would you like to create your own burger or preset one?")
else:
    print ("See you the next time.")

