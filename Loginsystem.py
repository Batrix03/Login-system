
accounts = open("Usernamelist.txt", "r+")

print("Hello human!")

username = input("insert your username and password ")
if username in accounts:
    print("Access completed")
else:
    error = input("Username not found, if you are new, type \"sign up\" if you want to try login again, type \"login\" ")
    if error == "sign up":
        sign_up = input("Enter a new username and a new password ")
        while sign_up in accounts:
            sign_up = input("Username taken, try again! ")
        else:
            accounts.write(sign_up)

    elif error == "login":

        username = input("insert your username and password ")
    else:
         print("Invalid Input")

