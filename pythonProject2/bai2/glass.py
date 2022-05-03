import os
class student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    def clas(self):
        self.inp = input("class: ")
        print(self.inp)
    def clasin(self):
        print("Name "+self.name)
        print("Class "+self.inp)