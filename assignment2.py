age = int(input("Enter your age: "))

if age>=18:
    print("You are eligible for voting.")
elif age<=17 and age>=0:
    print("You are NOT eligible for voting.")
elif age<0:
    print("Please Enter Valid Age!")
else: 
    print("Error")