class Teacher:
  collage = "CUK"
  name = "Aqib"
  def study(self1):
    print(f"The teacher is {self1.name},teaching maths.")

class Student(Teacher):
  name1 = "nadim"
  def learn(self2):
    print(f"Student {self2.name} is learning from {Teacher.name}")

a = Teacher()
b = Student()

b.study()
b.learn()

'''
You're declaring a new class variable name inside the Student class, which overrides (or hides) the one inherited from Teacher. In Python, when an attribute like name exists in both the parent and child classes, the child class version takes priority when accessed through a child class or its instance.
'''