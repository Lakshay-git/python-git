class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

person1 = person("Messi",35)
print(person1._person__name)
print(person1._person__age)
