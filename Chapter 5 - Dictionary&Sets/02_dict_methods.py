marks = {
  "Nadim": 77,
  "Amaan": 88,
  "Aqib": 99, 
  0: "ayaan"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Nadim":65,"Amaan":76}) # marks got updated
print(marks)

print(marks.get("Nadim")) 


print(marks.get("Nadim2"))  # returns NONE

# print(marks["Nadim2"]) # returns error

pop1 = marks.pop("Nadim")

print(marks)

pop2 = marks.popitem()

print(marks)

print(pop2)

