class Student:
    a = 1
    @classmethod # decorator
    def show(cls):
        print(f"The class attribute is of (a) is {cls.a}")


obj = Student()

obj.a = 66 # not take this 
# obj.a = 66 # not take this 
obj.show()


'''
@classmethod is a decorator used to define a method that belongs to the class, not the instance.

It takes cls (the class itself) as the first argument instead of self.

This allows the method to access and modify class variables and call other class methods.
'''