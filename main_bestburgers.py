# And this is how our first shared Python project begins :)
import filippo_workspace
import cosmin_workspace
import pricing
import order_save

##### USER INTERFACE ELEMENTS #####
LINE = "="*50
SPACE = " "*50
##### USER INTERFACE ELEMENTS #####
ordering_menu = {
    "1": "Order a Custom made Burger",
    "2": "Order a Preset Burger",
    "3": "Go directly to Sides",
    "4": "Go directly to Drinks"
}

while True:
    order = []   # every new customer starts with an empty order
    customer_name = input(f"What is your name?\n")
    print("")
    if customer_name != "admin":
        print(f"Welcome to Best burger {customer_name}!")
        print("")
        #Do you want to place an order?
        answer = filippo_workspace.extradef.ask_yes_no(f"Would you like to place an Order? (Y/N)\n")
        print(f"{LINE}\n{SPACE}") 

        if answer:
            ordering = True

            while ordering:
                #show the Ordering Menu
                for number, text in ordering_menu.items():
                    print(f"{number}. {text}")
                    print("")
# SELECTION PROMPT #                    
                print(pricing.subtotal_prompt(order))
                menu_choice = input(f"Enter your selection:\n").strip()  
                print(f"{LINE}\n") 

                while menu_choice not in ordering_menu:
                    print("Invalid choice, please enter the number of your choice.")
                    menu_choice = input(f"Enter the number:\n").strip()
                    print(f"{SPACE}\n{LINE}") 

                if menu_choice in ("1","2"):
                    if menu_choice == "1":
                        burger = filippo_workspace.customburger_def.customburger_function()
                    else:
                        burger = filippo_workspace.presetburger_def.presetburger_function()

                    if filippo_workspace.extradef.ask_yes_no(f"{LINE}\n \nWould you like to make a Menu?\n"):
                        order.append(filippo_workspace.extradef.menu_function(burger))
                    else:
                        order.append(burger)
                elif menu_choice == "3":
                    order.append(filippo_workspace.onlysideanddrink_def.onlyside_function())

                elif menu_choice == "4":
                    order.append(filippo_workspace.onlysideanddrink_def.onlydrink_function())

                ordering = filippo_workspace.extradef.ask_yes_no(f"Would you like to order something else? (Y/N)\n")
                print(f"\n {LINE}")

                # HERE WE MUST CONTINUE THE PROGRAM > WHEN NO > THIS IS YOUR ORDER TOTAL > PAY? DISCOUNT? CANCEL?
                # AND AFTER PAYMENT > LEAVE A REVIEW FROM 1 TO 5 !!!
        else:
            print(f"See you the next time {customer_name}.")

# HERE THE SAVE_INVOICE BEGINS #
        if order:
            order_number, file_path = order_save.save_order(customer_name, order)
            print(LINE)
            print(SPACE)        
            print(f"Your order number is: {order_number}")    
            print(SPACE)   
            print(f"Thank you, {customer_name}, see you the next time!")    
            print(SPACE)   
            print(LINE)

    else:
        customer_name == "admin"
        print("Ciao Admin!")
        cosmin_workspace.admin.admin_login()