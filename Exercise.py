print ("Welcome to FAA Burger shop, the shop where you can create the Burger of your dream.")
first_name = input("What is your name?")
last_name = input ("What is your last name?")
print ("Hello", first_name, last_name)
print ("Would you like to place an order?")
answer = input ("Please confirm (yes/no):")
own_burger = ""
if answer.strip().lower() == "yes" or answer.strip().lower() == "y":
    own_burger = input ("Would you like to create your own burger (yes/no)?")
else:
    print ("See you the next time.")
bread_type = ""
preset_burger = ""
if own_burger.strip().lower() == "yes" or own_burger.strip().lower() == "y":
    bread_type = input ("Which type of Bread would you like?")
else:
    preset_burger = input("Which of the following Preset Burger would you like?")