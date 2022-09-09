# Inheritance (Kalitim): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Strudent(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firsname = fname
        self.lastname = lname
        print('Person Created')

    def who_am_i(self):
        print(f'I am {self.firsname} {self.lastname}')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')

    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a Student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} Teacher')

c1 = Person('Ali', 'Yilmaz')
c2 = Student('Cinar', 'Turan',1233)
t1 = Teacher('Serkan','Ali','matematik')

t1.who_am_i()

print(c1)
print(c2)

c2.who_am_i()

print(f'first person name: {c1.firsname}, second person name: {c2.firsname}')
