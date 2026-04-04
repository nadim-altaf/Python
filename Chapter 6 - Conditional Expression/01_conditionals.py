a = int(input("Enter your age : "))

if a >= 18:
    print("you are adult")
    print("good for you")

elif a==0:
    print("0 is also not valid for age")

elif a < 0:
    print("invalid age")

else:
    print("you are below 18")

