## Hello team mate or teacher, this is my Artboard, or my Sandbox.
## Here is where I write and compile my code as a beginner,
## trying out before I write and commit into the official files.

# I expect to be asked if I am a student, and receive a 10% discount before confirming the order and check-out, to profit from my social status.

# I want to apply my student status during the final order review
# So that I can receive a 10% discount on my purchase

from datetime import datetime




print(complete_payment())


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

    def complete_payment():
    now = datetime.now()
    order_name = f"order_{now:%Y%m%d-%H%M}"
    return order_name

order_name()
complete_payment()

