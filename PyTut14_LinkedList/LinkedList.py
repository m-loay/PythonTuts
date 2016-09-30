'''
Created on Jul 16, 2016

@author: modys
'''

from Node import Node

class LinkedList:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.first=None
    
    def isEmpty(self):
        return self.first is None
    
    def __str__(self):
        if self.isEmpty():
            return"The list is Empty"
        
        currentNode=self.first
        strings="The list is "
        
        while currentNode is not None:
            strings+=str(currentNode.getData())
            strings+="--> "
            currentNode=currentNode.getNextNode()
            
        strings+="None"
        
        return strings
            
    def insertSorting(self,value):
        current=self.first
        prev=None
        
        while (current is not None) and (current.getData() < value):
            prev = current
            current = current.getNextNode()
            
        newNode=Node(value)
        newNode.setNextNode(current)
        
        if prev == None :
            self.first = newNode
        else :
            prev.setNextNode(newNode)
        
    def remove(self,delValue):
        if self.isEmpty():
            raise(ValueError,"List is empty")

        currentx = self.first
        if delValue == self.first.getData():
            self.first = self.first.getNextNode()
            currentx.setNextNode(None)
        else:
            prev = None
            while (currentx is not None) and (currentx.getData() != delValue):
                prev = currentx
                currentx = currentx.getNextNode()
                
            if(currentx is not None):
                prev.setNextNode(currentx.getNextNode())
                currentx.setNextNode(None)
                
    def getCount(self):
        
        if self.isEmpty():
            raise(ValueError,"List is empty")
            
        current = self.first
        countList=0
        
        while current is not None :
            countList+=1
            current = current.getNextNode()
        return countList
                
            
            
        
            

                
    
    
        
        
    
        