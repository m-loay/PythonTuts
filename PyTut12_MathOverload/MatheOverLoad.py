'''
Created on Jul 15, 2016

@author: modys
'''

def GCD(x,y):
    while y:
        z=x
        x=y
        y = z % x
    return x


class MATHEMATICS:
    '''
    classdocs
    '''


    def __init__(self, top=1, bottom=1):
        '''
        Constructor
        '''
        if bottom==0:
            raise (ZeroDivisionError,"Cannot have zero in den"%bottom)
        
        self.num=abs(top)
        self.den=abs(bottom)
        
        if top * bottom > 0:
            self.sign=1
        else:
            self.sign=-1
            
        
        self.simplify()
        
 
    def simplify(self):
        common = GCD(self.num, self.den)
        self.num /= common
        self.den /= common
        
    def __neg__(self):
        return MATHEMATICS(-self.sign * self.num, self.den)
    
    def __add__(self, other):
        return MATHEMATICS (self.sign * self.num * other.den +
                            other.sign * other.num * other.den ,
                            self.den * other.den)
    
    def __sub__(self, other):
        return self + (-other)
 
    
    def __mul__(self, other):
        return MATHEMATICS(self.num * other.num ,
         self.sign * self.den * other.sign * other.den)
        
    def __div__(self, other):
        return MATHEMATICS(self.num * other.den,
         self.sign * self.den * other.sign * other.num)
        
    def __truediv__(self, other):
        return self.__div__(other)
        
    def display(self):
        print("%d/%d"%(self.sign * self.num, self.den))
        
      
    
 
        
        