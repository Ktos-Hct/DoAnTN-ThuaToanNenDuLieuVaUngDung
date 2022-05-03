import os
import bai1.examble2 as ex
list=[1,2,"BALA"]
list.append("KAKA")
def sum(a,b):
    return a+b
if __name__ == "__main__":
    print(sum(4,5))
    ret=sum(3,4)
    for i in list:
        print(str(list.index(i))+": " + str(i))
    if (ret==4) or ret==7:
        print("dung con me no roi")
    else:
        print("sai con me no roi")
    a=ex.ReadFile("file.txt")
    b=a.readFile()
    b.clas()
    b.clasin()
