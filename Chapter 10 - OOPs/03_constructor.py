class Employee:
    name = "Aqib"
    lang = "urdu"
    salary = 12000

    def __init__(self, name, lang, salary):
        self.name = name
        self.lang = lang
        self.salary = salary


e1 = Employee("amaan", "python", 4300000)
print(e1.name, e1.lang,e1.salary)
