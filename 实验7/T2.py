class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self, age):
        self.age = age

    def setSex(self, sex):
        self.sex = sex

    def getSex(self):
        return self.sex

    def show(self):
        return 'name:{0},age:{1},sex:{2}'.format(self.name, self.age, self.sex)


if __name__ == "__main__":
    adela = Person('adela', 16, 'F')
    print(adela.show())
