def celToFerh(f):

    return 5 * (f - 32) / 9


f = int(input("Enter number : "))

Celsius = celToFerh(f)

print(f"F to C is {round(Celsius , 2)}°C")
