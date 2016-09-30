'''
Created on Jul 16, 2016

@author: modys
'''

class Node:
    '''
    classdocs
    '''


    def __init__(self, value):
        '''
        Constructor
        '''
        self.data=value
        self.nextNode=None
        
    def setData(self,data):
        self.data=data 
    
    def getData(self):
        return self.data 
    def setNextNode(self,newNode):
        self.nextNode=newNode 
        
    def getNextNode(self):
        return self.nextNode
    
        