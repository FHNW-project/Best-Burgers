# And this is how our first shared Python project begins :)
import filippo_workspace
import cosmin_workspace

LINE = "-"*50
order = []

ordering_menu = {
    "1": "Order a Custom made Burger",
    "2": "Order a Preset Burger",
    "3": "Go directly to Sides",
    "4": "Go directly to Drinks"
}

customer_name = input(f"What is your name?\n")
if customer_name != "admin":
    print(f"Welcome to Best burger {customer_name}!")
    #Do you want to place an order?
    answer = input (f"Would you like to place an Order?\n").strip().lower()
    while answer not in ("yes","ye","y","no","n"):
        print("Invalid choice, be aware that you can enter only Yes or No.")
        answer = input(f"Would you like to place an Order?\n").strip().lower()

    if answer in ("yes","ye","y"):
        ordering = True

        while ordering:
            #show the Ordering Menu
            print("")
            for number, text in ordering_menu.items():
                print(f"{number}. {text}")

            menu_choice = input(f"Enter the number:\n").strip()
            while menu_choice not in ordering_menu:
                print("Invalid choice, please enter the number of your choice.")
                menu_choice = input(f"Enter the number:\n").strip()

            if menu_choice in ("1","2"):
                if menu_choice == "1":
                    burger = filippo_workspace.customburger_def.customburger_function()
                else:
                    burger = filippo_workspace.presetburger_def.presetburger_function()

                if filippo_workspace.extradef.ask_yes_no(f"Would you like to make a Menu?\n"):
                    size = filippo_workspace.extradef.choose_size()
                    side = filippo_workspace.sides_def.side_function()
                    drinks = filippo_workspace.drinks_def.drinks_function()
                    order.append(filippo_workspace.extradef.make_menu(burger, side, drinks, size))
                else:
                    order.append(burger)
            elif menu_choice == "3":
                order.append(filippo_workspace.sides_def.side_function())

            elif menu_choice == "4":
                order.append(filippo_workspace.drinks_def.drinks_function())

            ordering = filippo_workspace.extradef.ask_yes_no(f"Would you like to order something else? yes/no\n")

    else:
        print(f"See you the next time {customer_name}.")

    print(LINE)
    print(f"Order for {customer_name}")
    print(LINE)

    print(order)

else:
    customer_name == "admin"
    print("Ciao Admin!")
    cosmin_workspace.admin.admin_login()
    

