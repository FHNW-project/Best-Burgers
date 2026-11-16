import time

def admin_login():
    failed_attempts = 0
    while failed_attempts < 3:
        print("please enter the password:")
        password = input()
        if password == "Password123!":
            print ("Welcome to the admin panel")
            break
        else:
            print("password incorrect. Please try again")
            failed_attempts = failed_attempts + 1

    if failed_attempts == 3:
        print ("Maximum attempts reached")
        time.sleep(5)
        
admin_login()