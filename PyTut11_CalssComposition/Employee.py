'''
Created on Jul 15, 2016

@author: modys
'''
from Time1 import Time

class Emp:
    '''
    classdocs
    '''


    def __init__(self,firstName, lastName, checkInTime, CheckOutTime):
        
        '''
        Constructor
        '''
        self.empStartTime = Time(checkInTime)
        self.empEndTime = Time(CheckOutTime)
        
        self.firstName=firstName
        self.lastName=lastName
        print("Constructor called for %s %s"%(self.firstName,self.lastName))
        
    def __del__(self):
        print("Destructore called for %s %s"%(self.firstName,self.lastName))
        
    def display(self):
        print("%s %s"%(self.firstName,self.lastName))
        print("Checked in ")
        self.empStartTime.printStandard()
        print("checked out")
        self.empEndTime.printStandard()
        
        
              
        