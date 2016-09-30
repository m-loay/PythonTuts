'''
Created on Jul 15, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

atuple=("hello","world",1)
alist=["pythin","programming",3]
astring="abc"

print("unpack tuple")
first,sec,third=atuple
print(first,sec,third)

print("unpack list")
first,sec,third=alist
print(first,sec,third)

print("unpack astring")
first,sec,third=astring
print(first,sec,third)

x=3
y=5
print("before swapping x=%d y=%d"%(x,y))

x,y=y,x

print("After swapping x=%d y=%d"%(x,y))
