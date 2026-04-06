n = int(input("Enter a Number : "))

# if n % 2 == 0:
#     print(f" {n} is not a prime")

# elif n % 2 != 0:
#     print(f"{n} is prime")

for i in range(2, n):
    if (n % i) == 0:
        print("Number is not Prime")
        break

else:
    print("number is Prime")
