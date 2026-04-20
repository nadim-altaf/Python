class Programmer:
    a = 1

    def __init__(self):
        print("constructor of Programmer")


class Coder(Programmer):
    b = 2

    def __init__(self):
        super().__init__()
        print("constructor of Coder")


class Mangaer(Coder):
    c = 3
    def __init__(self):
        super().__init__()
        print("constructor of Manger")


# x = Programmer()
# print(x.a)

# z = Coder()
# print(z.a, z.b)

y = Mangaer()
print(y.a, y.b, y.c)
