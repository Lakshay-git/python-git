# def name(x):
#     print(x)
# name(10)
# name(4)

# def add(num1, num2):
#    sum = num1 + num2
#    print(sum)
# add(5,10)
# add(100,17)
# add(150,150)

# def sub(num1,num2):
#     sub = num1 - num2 
#     print(sub)
# sub(5,2)

# def add(num1,num2):
#     sum = num1 + num2
#     return sum 

# result = add(1,4)
# print(result)

# def name(myname):
#     print("my name is : " + myname)

# name("xyz")

# def name(firstname = "vishal"):
#     print("my name is : " + firstname)

# name("vishal")
# name("pragya")
# name()
# name("kashish")

#create a function to print your name and age 
# def name(myname, age):
#     print("your name: "  + myname + "my age is " + age)

# name("lakshay", "21")

#write a program to create a function using following conditions 

#it should accept employee name and salary and display both 
#if the salary is missing then assign the default value as 10000 to salary 

#ben(12000) #mike(15000) #bob()

# def factorial(num):
#     if num==0:
#         return 1 
#     return num * factorial(num-1)
# ans=factorial(5)
# print(ans)

#def sum_recursion(num):
#    if num==0:
#        return.num
#    return.num+sum_recursion(num-1)
#ans = sum_recursion(5)
#print(ans)

a=int(input())
p=0
q=1
print(p,q)
for i in range(0,a+1):
    r=p+q
    print(r,end=" ")
    p=q
    q=r