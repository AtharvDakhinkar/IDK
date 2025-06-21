password = input("Enter your password: ")

if (len(password)>=10):
    print("Strong Password!")
elif (len(password)<=10 and len(password)>=7):
    print("Moderate Password!")
elif (len(password)<=6 and len(password)>=4):
    print("Weak Password!")
else:
    print("Password must be atleast 4 Characters long!")