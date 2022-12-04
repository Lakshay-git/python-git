#store multiple values in single variable
#unorderd
#mySet = {"car","bike","boat"}
#print(mySet)

#unchangeable
#duplicates are not allowed

myset = {"car","bike","boat","train"}
myset1 = {1,2,3,4}
myset2 = {4,5,6}
#myset3 = myset1.union(myset2)
#myset3 = myset1.intersection(myset2)

#myset3 = myset1.union(myset2)
myset3 = myset1.symmetric_difference(myset2)
print(myset3)