friends = ["Ayaan", "Amaan", 5, 45.4, False, "Aqib"]

# APPEND method

print(friends)
friends.append("Nadim") # join at the end a string like "Nadim"
print(friends)
print("\n")

# SORT Method

l1 = [2, 4, 1, 7, 3, 5, 6]
l1.sort()
print(l1)
print("\n")
 
# REVERSE Method

l2 = [1,2,3,4,5,6,7,8,9]
l2.reverse()
print(l2)
print("\n")

# INSERT Method

l1 = [2, 4, 1, 7, 3, 5, 6]
l1.insert(3, 8) # insert 8 such that its index in the list is 3
print(l1)
print("\n")

# POP Method

l1 = [2, 4, 1, 7, 3, 5, 6]
l1.pop(3) # --> 7 will delete which is at index 3
print(l1)
print("\n")
print(l1.pop(3)) # --> it return value of index 3 which is 7


print("\n")
l1 = [2, 4, 1, 7, 3, 5, 6]
l1.remove(4) # removes value not which is at index 4
print(l1)