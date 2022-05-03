import glass
import os
class ReadFile:
    def __init__(self,path):
        self.path=path
    def readFile(self):
        ret = open(self.path).readlines()
        lis=list()
        for i in ret:
            lis.append(i)
        return glass.student(lis[0], lis[1], lis[2])

