product = ["mouse","keyboard","mobile","headset","earbuds","water","idk"]
search = input("Search: ")

for i in product:
    if search==i:
        print(f"Product Found: {i}")
        break
    else:
        print("Product Not Found")