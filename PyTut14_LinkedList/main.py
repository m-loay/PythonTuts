'''
Created on Jul 16, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

from Node import Node
from LinkedList import LinkedList

listing = LinkedList()

listing.insertSorting(5)
listing.insertSorting(4)
listing.insertSorting(6)
listing.insertSorting(9)
listing.insertSorting(2)
listing.insertSorting(1)
listing.insertSorting(0)

print(listing)

countList = listing.getCount()
print("The list Number %d"%countList)


listing.remove(5)
print(listing)

countList = listing.getCount()
print("The list Number %d"%countList)
