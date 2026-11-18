import time
from getpass import getpass

def admin_login():
    failed_attempts = 0
    while failed_attempts < 3:
        password = getpass("Please enter the password: ", echo_char="*")
        if password == "Password123!":
            print ("Welcome to the admin panel")
            return True
        else:
            print("password incorrect. Please try again")
            failed_attempts = failed_attempts + 1

    if failed_attempts == 3:
        print ("Maximum attempts reached")
        time.sleep(2.5)
    return False