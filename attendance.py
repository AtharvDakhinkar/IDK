attendance = ["Atharv","Nishad","John Wick","IDK","Car","Someone","Something","Bleh"]
search = input("Enter Student name to search: ")
found = False

for i in attendance:
    if search==i:
        found = True
        break

if found == True:
    print(f"{search} is Present")
else: 
    print(f"{search} is Absent")