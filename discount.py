shopping = int(input("Enter your shopping amount: "))

if shopping>=5000:
    print("You are eligible for a discount of 20%")
    discount = shopping * 0.20
elif shopping<5000 and shopping>=1000:
    print("You are eligible for a discount of 10%")
    discount = shopping * 0.10
elif shopping<1000 and shopping>0:
    print("You are eligible for a discount of 5%")
    discount = shopping * 0.05
else:
    print("Enter Valid Amount!")

print("Discount = ",discount,"\n Total Amount After Discount: ",(shopping-discount))