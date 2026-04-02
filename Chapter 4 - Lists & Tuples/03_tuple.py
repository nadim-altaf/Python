a = (1,2,2,3,644,False,"python")
b = (1,) # if you want to declear one element in a tuple then put comma after element,python recognize  it is tuple not a integer

# a[0] = 8 # gives error , we can't change tuple

print(a)
print(b)

print(type(a))
print(type(b))

n = a.count(2)
print(n)
i = a.index(64)
print(i)