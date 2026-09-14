class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f'Hi, I am {self.first_name} {self.last_name}')


class Student(Person):

    def __init__(self, first_name, last_name, course):
        super().__init__(first_name, last_name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I study {self.course}.")

    def study(self):
        print(f'{self.first_name} is studying {self.course}.')


class WorkingStudent(Student):

    def __init__(self, first_name, last_name, course, company):
        super().__init__(first_name, last_name, course)
        self.company = company

    def introduce(self):
        super().introduce()
        print(f"I work at {self.company}.")

if __name__ == "__main__":

    p = Person('Jose', 'Rizal')
    s = Student('Melchora', 'Aquino', 'BS Computer Science')
    w = WorkingStudent('Andres', 'Bonifacio', 'BS Information Technology', 'PUP Tech Inc.')

    p.introduce()       
    s.introduce()       
    w.introduce()       
    w.study()
