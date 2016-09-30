'''
Created on Jul 15, 2016

@author: modys
'''

if __name__ == '__main__':
    pass

grades={"mody":90, "maha":100, "lolo":60,"John":87, "Steve":76, "Laura":92, "Edwin":89}

print(grades)

grades["mody"]=95
print("new mody grade=%d"%grades["mody"])

print(grades)

#some methods in Dics
print("The dictionary items are:")
print(grades.items())

print("The dictionary keys are:")
print(grades.keys())

print("The dictionary values are:")
print(grades.values())

for key in grades.keys():
    print("grades[",key,"]=",grades[key])


