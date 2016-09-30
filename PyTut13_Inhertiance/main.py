'''
Created on Jul 15, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

from Employee import Empoloyee
from BasePlus import BasePlus

e1=Empoloyee("mohamed","Loay","123-443",200,0.1)
e2=Empoloyee("mohamed1","Loay1","123-443",300,0.1)
e3=Empoloyee("mohamed2","Loay2","123-443",400,0.1)

b1=BasePlus("Mody","Ali","123-6378",1000,0.1,100)
b2=BasePlus("Mody1","Ali1","123-36378",2000,0.1,100)
b3=BasePlus("Mody2","Ali2","123-336378",2000,0.1,100)

employees=[e1, e2, e3, b1, b2, b3]

for emp in employees:
    emp.display()
    print()