'''
Created on Jul 14, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

counter1=1
counter2=1
fact=1
counter=1
summ=1
x=3
while counter1 < 11:
    
    for counter2 in range(1,counter1+1):
        fact*=counter2
    print(fact)
    summ+=(x**counter1)/fact
    fact=1
    counter1+=1     
print("e= %.2f"%summ)