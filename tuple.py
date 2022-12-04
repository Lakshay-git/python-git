# myTuple = ("car","bike","boat")
# myList = list(myTuple)
# myList.append("ship")
# myTuple = tuple(myList)
# print(myTuple)

#tuple1 = (1,2,3,4,5)
#reverse the above tuple 
#print(tuple1[::-1])

tuple1 = (10,20)
tuple2 = (30,40)
#swap above tuples
#output - tuple1 = (30,40)
#          tuple2 = (10,20)
temp = tuple1
tuple1 = tuple2
tuple2 = temp
print(tuple1)
print(tuple2)