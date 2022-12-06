

# list1 = [3,4,10,9,18,66,13,15]
# #evennum = list(filter(lambda i : i%2==0,list1))

# #greaterthan5 = list(filter(lambda i : i>5,list1))
# #squareNum=list(map(lambda i: i** 2, list1))
# #print(squareNum)

# list1 = [10,20,30,40,50]
# #triples the values of list
# tripleNum = list(map(lambda i : i*3,list1))
# print(tripleNum)


# #list2 = ["a","B","c","D","e","f"]
# #list2 = list(map(lambda i : i))

# def div (a,b):
#     print(a/b)

# def good_div(func):

#     def inner_div(a,b):
#         if a < b:
#             a,b=b,a
#         return func(a,b)
    
#     return inner_div

# div = good_div(4,2)
# div(2,4)


# # The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the
# # list elements mentioned in the sequence passed along.This function is defined in “functools” module.
# # Working :  

# # At first step, first two elements of sequence are picked and the result is obtained.
# # Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# # This process continues till no more elements are left in the container.
# # The final returned result is returned and printed on console.


from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
sum=reduce(lambda i,j: i+j,list1)
print(sum)

