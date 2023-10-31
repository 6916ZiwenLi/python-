from T2 import Person


class Teacher(Person):
    def __init__(self, name, age, sex, course, salary):
        Person.__init__(self, name, age, sex)
        self.course = course
        self.salary = salary

    def setCourse(self, course):
        self.course = course

    def getCourse(self):
        return self.course

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def show(self):
        return (Person.show(self) + (',course:{0},salary:{1}'.format(self.course, self.salary)))


if __name__ == "__main__":
    teacher0 = Teacher('teachername', 30, 'f', 'sourse', 'salary')
    print(teacher0.show())
