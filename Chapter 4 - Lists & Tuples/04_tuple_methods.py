a = (1, 1, 2, 3, 3, 644, False, "python")
print(a)
print(type(a))

no = a.count(3)
print(no)

i = a.index(3)
print(i)

tuple = (1,2,3,4)
repeated = tuple * 2
print(repeated)

print(2 in tuple)
print(4 in tuple)

print(len(a))

sliced = a[0:6] # new tuple will create
print(sliced)