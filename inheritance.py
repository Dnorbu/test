class Person:
    def _init_(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Teacher(Person):
    def _init_(self, name, age, cid_number, subject, salary, department, designation):
        super()._init_(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")


class Student(Person):
    def _init_(self, name, age, cid_number, student_id, course, year):
        super()._init_(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")


# Creating objects
teacher1 = Teacher("Mrs Tashi Peldon", 40, "11514004815", "CSF", 60000, "IT", "Lecturer")
student1 = Student("Karma", 18, "11514004844", "02230096", "ECE", 1)

# Displaying information and behaviors
print("Teacher Information:")
print(f"Name: {teacher1.name}, Age: {teacher1.age}, CID Number: {teacher1.cid_number}")
teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()

print("\nStudent Information:")
print(f"Name: {student1.name}, Age: {student1.age}, CID Number: {student1.cid_number}")
student1.walk()
student1.talk()
student1.eat()
student1.sleep()
student1.study()
student1.attend_class()
student1.write_exam()