#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from itertools import chain


class Student(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []
        self.attendances = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def add_attendance(self, attendance):
        "True if student was present, else False"
        self.attendances.append(attendance)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def count_number_of_attendances(self):
        return sum(self.attendances)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    __unicode__ = __str__

    __repr__ = __str__


class Class(object):
    def __init__(self, name, list_of_students=None):
        "List of students is a set of students"
        self.name = name
        self.list_of_students = list_of_students or set()

    def add_student(self, student):
        self.list_of_students.add(student)

    def count_avg_grade(self):
        if not self.list_of_students:
            return 0
        return (sum(chain(stud.grades for stud in self.list_of_students))/
                sum(len(stud.grades) for stud in self.list_of_students))

    def order_students_by_grade(self):
        return sorted(self.list_of_students, key=lambda x: x.get_average_grade,
                reverse=True)

    def __str__(self):
        return "Class {}".format(self.name)

    __unicode__ = __str__

    __repr__ = __str__


class School(object):
    def __init__(self, list_of_classes=None):
        self.list_of_classes = list_of_classes or set()

    def order_classes_using_grade(self):
        return sorted(self.list_of_classes, key=lambda x: x.count_avg_grade,
                reverse=True)


if __name__ == '__main__':
    # example
    student1 = Student('student', 'one')
    student2 = Student('student', 'two')
    student3 = Student('student', 'three')
    student4 = Student('student', 'four')

    class1 = Class('1A', {student1, student2})
    class2 = Class('1B', {student3, student4})

    school = School({class1, class2})

    student1.add_attendance(True)
    student1.add_attendance(True)
    student1.add_attendance(False)
    student1.add_grade(3)
    student1.add_grade(2)
    student1.add_grade(4)

    student2.add_attendance(True)
    student2.add_attendance(True)
    student2.add_attendance(True)
    student2.add_grade(5)
    student2.add_grade(5)
    student2.add_grade(4)

    student3.add_attendance(True)
    student3.add_attendance(True)
    student3.add_attendance(True)
    student3.add_grade(5)
    student3.add_grade(5)
    student3.add_grade(5)

    student4.add_attendance(True)
    student4.add_attendance(True)
    student4.add_attendance(True)
    student4.add_grade(5)
    student4.add_grade(5)
    student4.add_grade(5)

    print school.order_classes_using_grade()
    print class1.order_students_by_grade()
    print class2.order_students_by_grade()

