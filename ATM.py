balance = 500000

withdraw = int(input("Enter the amount you want to withdraw: "))

if withdraw > balance:
    print("Not enough balance")
elif withdraw < 0:
    print("Please enter valid amount")
else:
    balance = balance-withdraw
    print("Debited amount: ", withdraw,"\nBalance: ", balance)