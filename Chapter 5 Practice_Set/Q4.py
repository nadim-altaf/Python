s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?

print(len(s))
print(s)

print()

s2 = {}
print(type(s2))