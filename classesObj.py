
# # class laptop:
# #     def __init__(self):
# #         print("Hello world")
# #     def config(self):
# #         print("Asus","i7","1TB")

# # laptop1 = laptop()
# # laptop2 = laptop()



# # #laptop.config(laptop1)
# # laptop1.config()
# # laptop2.config()

# #id gives memory location


# #config calls the function , the memory in which this are created are called is heap

# #pass ia a keyword 




# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno = rollno



#     def info(self):
#         pass
#         print("name is : ",self.name,"roll number is:",self.rollno)

# student1 = student("lakshay","63")
# student2 = student("shivam","34")

# print(id(student1))
# print(id(student2))

# student1.info()
# student2.info()

# class person:
#     def __init__(self):
#         self.name = "ishan"
#         self.number = 32

#     def compare(self, other):
#         if(self.number == other.number):
#             return True
#         else:
#             return False


# p1 = person()
# p2 = person()
# p2.number = 18
# if p1.compare(p2):
#     print("same")
# else:
#     print("different")


# print(p1.number)
# print(p2.number)


#class car:
    #wheel=4
    #static variable-values are constant(for car ,tyre etc)
    #instance variables-value varies from obj to obj
   # def __init__(self):
  #      self.company="bmw"
 #       self.mileage=10

#car1=car()
#car2=car()

#print(car1.company,car1.wheel)
#print(car2.company,car2.wheel)
#print(c1.mileage)
#print(c2.mileage)



class student:
    collegeName = "LPU"

    def __init__(self, python,web,math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
        #self.average = (python + web + math)/3

    def avgCalculator(self):
        return(self.subject1 + self.subject2 + self.subject3)/3

    #def get_subject1(self):
        #return self.subject1 #this method called accessesor

    #def set_marks(self,value):
     #   return self.subject1   #this method called mutator
#below is a class method 
    @classmethod
    def collegeDetail(cls):
        return cls.collegeName

student1=student(4,7,8)
student2=student(2,3,9)

print(student1.avgCalculator())
print(student2.avgCalculator())
print(student.collegeDetail())
