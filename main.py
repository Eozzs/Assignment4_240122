class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            #course.add_student(self)

    def performance_report(self):
        for course in self.enrolled_courses:
            print(f'Student: {self.name}, Course: {course.name}, Grade: {self.grades[course]}')

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
    def list_courses(self):
        return self.courses

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.list_lessons = []
        self.attendance = {}
        teacher.courses.append(self.name)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_status = self.attendance.get(student)
            print(f"Student: {student.name}, Attendance: {attendance_status}")

    def add_lesson(self, topic):
        self.list_lessons.append(topic)

    def get_lessons(self):
        return self.list_lessons

class Lesson(Course):
    def __init__(self, name, topic, hours):
        super().__init__(name)
        self.topic = topic
        self.hours = hours


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']