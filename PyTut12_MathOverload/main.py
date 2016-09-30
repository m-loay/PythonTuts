'''
Created on Jul 15, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

from MatheOverLoad import MATHEMATICS

mat1=MATHEMATICS()
mat1.display()

mat2=MATHEMATICS(10,30)
mat2.display()

mat3=MATHEMATICS(-7,14)
mat3.display()

mat4=MATHEMATICS()
mat4=mat2 / mat3
mat4.display()
