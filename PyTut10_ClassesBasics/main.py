'''
Created on Jul 15, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

from Time1 import Time

print("Count value=")
print(Time.count)

time1=Time(counter=1)
time2=Time(2,counter=2)
time3=Time(21,34,counter=3)
time4=Time(12,25,42,4)

print("After creating objects Count value=")
print(time1.count)


print("Time 1")
time1.printStandard()
time1.prinitUniversal()

print("Time 2")
time2.printStandard()
time2.prinitUniversal()

print("Time 3")
time3.printStandard()
time3.prinitUniversal()

print("Time 4")
time4.printStandard()
time4.prinitUniversal()

del time1
del time2
del time3
del time4

print("After deleting objects Count value=")
print(Time.count)


