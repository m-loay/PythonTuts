'''
Created on Jul 15, 2016

@author: modys
'''

class Time:
    '''
    classdocs
    '''
    count=0

    def __init__(self,hour=0,minute=0,seconds=0,counter=0):
        '''
        Constructor
        '''
        self.__counter=counter
        print("Constructore of object %d is called"%counter)
        self.setTime(hour,minute,seconds)
        Time.count+=1
    
    def setTime(self,hour,minute,seconds):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSeconds(seconds)
    
    def setHour (self,hour):
        if 0<= hour <24:
            self.__hour=hour
        else:
            raise ValueError("Invalid Entery for hour=%d"%hour)
    
    def setMinute (self,minute):
        if 0<= minute <60:
            self.__minute=minute
        else:
            raise ValueError("Invalid Entery for minute=%d"%minute)
            
    def setSeconds (self,seconds):
        if 0<= seconds <60:
            self.__seconds=seconds
        else:
            raise ValueError("Invalid Entery for hour=%d"%seconds)
            
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSeconds (self):
        return self.__seconds
        
    def prinitUniversal(self):
        """Print Time in Universal Standard"""
        print("Time Universal")
        print("%.2d:%.2d:%.2d"%(self.__hour,self.__minute,self.__seconds))
        
    def printStandard(self):
        """Print Time in Normal Standard"""
        standardTime=""
        if self.__hour == 0 or self.__hour == 12:
            standardTime+="12:"
        else:
            standardTime+="%d:"%(self.__hour%12)
        standardTime+="%.2d:%.2d"%(self.__minute,self.__seconds)
        
        if self.__hour <12 :
            standardTime+=" AM"
        else:
            standardTime+=" PM"
        print("Time Standard")
        print(standardTime)
        
    def __del__(self):
        print("Destructor of object %d is called"%self.__counter)
        Time.count -=1
          
        