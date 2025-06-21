x = {1, 2, 3, 4}
y = {5, 6, 7}
z = {8, 11, 5}

a = set(x) & set(y) & set(z)
if not a:  
    print("No common elements")
else:
    print("Common elements are: ", a)

