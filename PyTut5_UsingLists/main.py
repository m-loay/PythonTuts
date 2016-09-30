'''
Created on Jul 14, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

def modifyList(alist):
    for i in range(len(alist)):
        alist[i]*=2

def modifyElement(element):
    element*=2



alist=[]

for i in range(10):
    alist+=[i]
    
for i in range(len(alist)):
    print("%7d %10d %s"%(i,alist[i],"*"*alist[i]))

for i in range(-1,-len(alist)-1,-1):
    print("%7d %10d %s"%(i,alist[i],"*"*alist[i]))


print("Before any Modification")
print(alist)

print("Modify List")
modifyList(alist)
print(alist)

print("Modify Element")
modifyElement(alist[3])
print(alist)