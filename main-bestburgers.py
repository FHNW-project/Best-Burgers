# And this is how our first shared Python project begins :)

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
