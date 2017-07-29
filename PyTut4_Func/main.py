'''
Created on Jul 14, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

def maxValue(x,y,z):
    maxx=x
    
    if y>maxx:
        maxx=y
    if z>maxx:
        maxx=z
 
    return maxx

a=int(input("Enter First integer:"))

b=int(input("Enter Second integer:"))

c=int(input("Enter third integer:"))

print("MAx Value= ",maxValue(a, b, c))

a1=float(input("Enter First Float:"))

b1=float(input("Enter Second Float:"))

c1=float(input("Enter third Float:"))

print("MAx Value= ",maxValue(a1, b1, c1))

a2=(input("Enter First string:"))

b2=(input("Enter Second string:"))

c2=(input("Enter third string:"))

print("MAx Value= ",maxValue(a2, b2, c2))