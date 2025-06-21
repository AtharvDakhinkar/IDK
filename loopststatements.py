elec = ["pc","laptop","mobile","smartwatch","idk"]

for i in elec:
    if i == "mobile":
        break

    print(i)

print("\nContinue Statement: ")

for i in elec:
    if i == "mobile":
        continue

    print(i)

lst = [1,2,3,4,5]
for i in lst:
    if i == 3:
        continue
    print(i)
   
print("\nPass:")

lst = [1,2,3,4,5]
for i in lst:
    if i == 3:
        pass
    print(i)
   

for i in range(1,11):
    print(f"5 x {i} = {i*5}")