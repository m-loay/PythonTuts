'''
Created on Jul 15, 2016

@author: modys
'''

from Employee import Empoloyee

class BasePlus (Empoloyee):
    '''
    classdocs
    '''


    def __init__(self, firstName, lastName, ssn, gs, cr, salary ):
        '''
        Constructor
        '''
        Empoloyee.__init__(self, firstName, lastName, ssn, gs, cr)
        self.__salary=salary
    
    def setSalary(self, salary):
        self.__salary=salary
        
    def getSalary(self):
        return self.__salary
    def getEarnings(self):
        return (self.getSalary()+Empoloyee.getEarnings(self))
    
    def display(self):
        Empoloyee.display(self)
        