'''
Created on Jul 15, 2016

@author: modys
'''

class Empoloyee:
    '''
    classdocs
    '''


    def __init__(self, firstName, lastName, ssn, gs, cr ):
        '''
        Constructor
        '''
        self.__firstName=firstName
        self.__lastName=lastName
        self.__ssn=ssn
        self.__gs=gs
        self.__cr=cr

    
    def setFirstName(self,firstName):
        self.__firstName=firstName
    
    def getFirstName(self):
        return self.__firstName
    
    def setLastName(self,lastName):
        self.__lastName=lastName
        
    def getLastName(self):
        return self.__lastName
        
    def setSsn(self,ssn):
        self.__ssn=ssn
    
    def getSsn(self):
        return self.__ssn 
        
    def setGs(self,gs):
        if gs < 0:
            self.__gs=0
        else:
            self.__gs=gs
    
    def getGs(self):
        return self.__gs 
     
    def setCr(self,cr):
        if(cr < 0):
            self.__cr=0
        else:
            self.__cr=cr
        
    def getCr(self):
        return self.__cr
    
    def getEarnings(self):
        return (self.getCr() * self.getGs())
    
    def display(self):
        print(self.getFirstName(), self.getLastName())
        print(self.getSsn())
        print("Earnings=%d"%(self.getEarnings()))
    
                
    
        
        