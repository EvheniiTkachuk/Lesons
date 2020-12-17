class Person:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state


class Student(Person):
    def __init__(self, name, age, state, average_score):
        super().__init__(name, age, state)
        self.average_score = average_score

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, State: {self.state}, Average score: {self.average_score}'


class Teacher(Person):
    def __init__(self, name, age, state, salary):
        super().__init__(name, age, state)
        self.salary = salary

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, State: {self.state}, Salary score: {self.salary}'


student = Student('John', 19, 'm', 85)
teacher = Teacher('Alice', 69, 'w', 18500)

print(student)
print(teacher)