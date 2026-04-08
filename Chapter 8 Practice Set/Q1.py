# Write a program using functions to find greatest of three numbers.
def greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


a = 3
b = 1
c = 5

print(greater(a, b, c))
