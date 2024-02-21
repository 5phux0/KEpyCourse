class Person(object):
    def __init__(self, firstname='John', lastname='Smith'):
        self.firstname = firstname
        self.lastname = lastname

    def printFullName(self):
        print('{} {}'.format(self.firstname, self.lastname))


class Student(Person):
    def __init__(self, firstname='John', lastname='Smith', subject='Science'):
        super().__init__(firstname, lastname)
        self.subject = subject

    def printNameAndField(self):
        print('{} {}, {}'.format(self.firstname, self.lastname, self.subject))


class Teacher(Person):
    def __init__(self, firstname='John', lastname='Smith', course='Science 101'):
        super().__init__(firstname, lastname)
        self.course = course

    def printNameAndCourse(self):
        print('{} {}, {}'.format(self.firstname, self.lastname, self.course))
