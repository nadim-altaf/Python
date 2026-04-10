# p = open("poem.txt")
# data = p.read()
# print(data)


with open("poem.txt") as p:
  print(p.read())