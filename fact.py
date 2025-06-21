num = int(input("Enter an integer: "))
fact = 1

for i in range(1,num+1):
    fact = fact * i
    if(i==num):
        print(i,end=" ")
    else:
        print(i,end=" x ")

print("= ", fact)

print(f"Factorial of {num} is {fact}")