import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice :")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]

print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if computer == you:
    print("its draw game")

else:
    # if computer == -1 and you == 1:  # computer - you = -1 - 1 = -2
    #     print("you win")
    # elif computer == -1 and you == 0:  # computer - you = -1 - 0 = -1
    #     print("you lose")
    # elif computer == 1 and you == -1:  # computer - you = 1 - -1 = 2
    #     print("you lose")
    # elif computer == 1 and you == 0:  # computer - you = 1 - 0 = 1
    #     print("you win")
    # elif computer == 0 and you == -1:  # computer - you = 0 - -1 = 1
    #     print("you win")
    # elif computer == 0 and you == 1:  # computer - you = 0 - 1 = -1
    #     print("you lose")
    # else:
    #     print("somethind wrong!")


 if (computer - you) == -1 or (computer - you) == 2:
    print("You Lose")
 else:
    print("You win")
