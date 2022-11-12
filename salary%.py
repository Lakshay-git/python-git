# company will give bonus base on following criteria 

# time spent in copany           bonus 
#     greater than 10 years       10%

# more than 6 and less
#    than 10                       8%

#   less than 6                    5%

# ask the salary and time spent from the user 
# print the net bonus amount accordingly 

salary = int(input("enter your current salary"))
year = int(input("enter your year spend"))

if year >= 10 :
    print("your net salary with 10 percent bonus- ", salary+salary*10/100)

elif year > 6 <= 10:
    print("your net salary wit 8 percent bonus-", salary+ salary*8/100)

elif year < 6:
    print("your net salary with 5 percent bonus-", salary+salary*5/100)