login = "admin"
passkey = "admin"
attempt = 10

while(True):
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    if username.strip()==login:
        if password==passkey:
            print("Successfully Logged-In!")
            break
        else:
            print("Incorrect Password!")
    else: 
        print("Invalid Username! Please try Again")
    
    attempt -= 1
    print("Attempts Remaining: ",attempt)

    if attempt<=0:
        print("Maximum Attempts Exceeded! Please try again later.")
        break