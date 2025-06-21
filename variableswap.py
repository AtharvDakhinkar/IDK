a = 10
b = 20
print("a = ",a)
print("b = ",b)

a , b = b , a
print("a = ",a)
print("b = ",b)

c = 30
d = 40
print("c = ",c)
print("d = ",d)

temp = c
c = d
d = temp
print("c = ",c)
print("d = ",d)

l = [[1,2],[3,4]]
print(l[1][0])