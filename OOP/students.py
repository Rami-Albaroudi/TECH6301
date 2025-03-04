class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def info_display(self):
        average = sum(self.grades) / len(self.grades)
        
        print(f"The student's name is {self.name}, their age is {self.age}, and their grades are {self.grades}. Their average is {average}.")

def add_student(name, age, grades):

    new_student = Student(name, age, grades)

    print("Student has been added.")

    return new_student
    

sample_student = add_student("Rami", 27, [0, 100, 50])

sample_student.info_display()

