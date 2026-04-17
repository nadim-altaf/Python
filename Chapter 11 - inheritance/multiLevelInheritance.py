class Programmer:
  a = 1

class Coder(Programmer):
  b =2

class Mangaer(Coder):
  c = 3

x= Programmer()
y = Mangaer()

print(y.a)