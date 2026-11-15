# And this is how our first shared Python project begins :)
import filippo_workspace
from datetime import datetime
now = datetime.now()
line = ("-" * 100)
space = (" " * 100)


# This is how the order[] gets the name after complete_payment
def complete_payment():
    now = datetime.now()
    order_name = f"order_{now:%Y%m%d-%H%M}"
    return order_name


print(line)
print(space)
print("*** Welcome to Best Burgers ***")
print(space)
print(line)
print(space)
print(f"Date & Time: {now:%A, %d.%m.%Y %H:%M}")
print(space)
print(line)
print(space)
print(">>> I am ready to take your order, so you can enjoy the Best Burgers you've ever had! <<<")
print(space)
print(line)
print(space)
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

