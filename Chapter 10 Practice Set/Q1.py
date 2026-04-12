class Programmer:
  company = "Microsoft"

  def __init__(self,name,salary,codeID):
    self.name = name
    self.salary = salary
    self.codeID = codeID

p = Programmer("Nadim" ,1200000,105)
print(p.name,":",p.salary,":",p.codeID)