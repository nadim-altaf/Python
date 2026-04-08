# def rem(l,word):
#   for item in l:
#     l.remove(word)
#     return l

# l = ["apple", "mango","grapes"]
# print(rem(l,"apple"))


def table(n):
    for i in range(1, n + 1):
        a = 3 * i
        print(f"3 * {a}")


n = int(input("enter number : "))
table(n)
