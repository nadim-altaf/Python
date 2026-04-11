class Employee:
  name = "Aqib"
  lang = "urdu"
  salary = 12000

  def getInfo(self):
    print(f"The language is {self.lang}. The Salary is {self.salary}")

  def __init__(self): # dunder method which is automatically called.
    print("i am creating a object")
  
  @staticmethod  # no need of object , (self)
  def greet():
    print("Asalamulaikum")
e1 = Employee()
e1.getInfo()
e1.greet()
