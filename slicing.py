lst = [1,2,3,4,5,6]
print(lst[2:5:2])
tpl = (1,2,3,4,5,5,6,6,67,7)
print(tpl[2:-1:2])

txt='LOL'
n_txt=txt[::-1]

if txt==n_txt:
    print(True)
else:
    print(False)

colours=['orange','black','purple','white']
colours[:3]=['red','green','blue']
print(colours)

li=[2,4,6,8,10]
li1=li[:]
print(li1)

print(tpl.index(5))
print(min(tpl))
print(sorted(tpl))