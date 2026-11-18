import time
from getpass import getpass

def admin_login():
    failed_attempts = 0
    while failed_attempts < 3:
        password = getpass("Please enter the password: ", echo_char="*")
        if password == "Password123!":
            print ("Welcome to the admin panel\n")
            admin_menu()
            return True
        else:
            print("password incorrect. Please try again")
            failed_attempts = failed_attempts + 1

    if failed_attempts == 3:
        print ("Maximum attempts reached")
        time.sleep(2.5)
    return False

def admin_menu():
    print ("1: Sales overview") # Weekly revenue and total orders
    print ("2: Burger popularity") # Custom vs preset burgers
    print ("3: Order comparison") # Number of orders this week vs last week
    print ("4: Revenue comparison") # Revenue this week vs last week, including percentage change
    print ("5: Customer satisfaction") # Average weekly rating and comparison with the previous week
    print ("6: Inventory") # Remaining quantities of ingredients
    print ("7: Best-selling burgers") # Top 3 most popular preset burgers
    print ("8: Return to main menu") # Exit admin panel
    selected = input("which menu you want to access? \n")
    if selected == "1":
        print ("menu 1")
    elif selected == "2":
        print ("menu 2")
    elif selected == "3":
        print ("menu 3")
    elif selected == "4":
        print ("menu 4")
    elif selected == "5":
        print ("menu 5")
    elif selected == "6":
        print ("menu 6")
    elif selected == "7":
        print ("menu 7")
    elif selected == "8":
        return
    else:
        print ("invalid choice")