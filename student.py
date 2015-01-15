# Assignment 1 - Managing Students!
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your group members below, one per line, in format
# <full name>, <utorid>
# Shreyansh Kumar, kumarsh6
# Yun-Yee Megan Yow, yowmegan
# ---------------------------------------------
"""The back-end data model for the program.

TODO: fill in this doctring with information about your
class(es)!
"""


class Student:
    """
    The class represents an individual student and supports adding, removing
    students, course listing and finding common courses between two students.

    Attributes:
    - self.name (str): the name of the student
    - self.courses (list): the list of courses student is enrolled in
    """
    def __init__(self, name):
        """ (Student, str) -> NoneType

        Creates a new Student with name

        Parameters:
        - name: the name of the Student created
        """
        self.name = name
        self.courses = []

    def add_course(self, new_course):
        """ (Student, Course) -> None or StudentAlreadyEnrolledError

        Adds new_course to the list of courses self is taking
        Enrols self to new_course object as well.
        If self is already enrolled in new_course, raise
        StudentAlreadyEnrolledError.

        Parameters:
        - new_course: course code that self wants to enroll in
        """
        if self.is_taking_course(new_course) == -1:

            if new_course.is_full():
                raise CourseFullError
            else:
                self.courses.append(new_course)
                new_course.add_student(self)
        else:
            raise StudentAlreadyEnrolledError

    def drop_course(self, course_obj):
        """ (Student, Course) -> None or StudentNotEnrolledError

        Removes course_obj from the list of courses self is taking
        If self is not taking course_obj, do nothing.
        Assumes course_obj is an already existing course and self is an
        existing student.

        Parameters:
        - course_obj: the Course object that self wants to drop
        """

        course_index = self.is_taking_course(course_obj)

        if course_index != -1:
            course_obj.remove_student(self)
            self.courses.pop(course_index)

    def is_taking_course(self, course_obj):
        """ (Student, Course) -> int

        Helper method: Return the index of a given course_obj in list of
        courses self is taking, if index not found, return -1

        Parameters:
        - course_obj: The Course Object that we want to find in the list
        of courses self is taking
        """
        i = 0
        for course in self.courses:
            if course.code == course_obj.code:
                return i
            i += 1

        return -1

    def list_courses(self):
        """ (Student) -> list

        Return a list of course codes in self is enrolled in alphabetical
        order.
        """
        course_name_list = []
        for course in self.courses:
            course_name_list.append(course.code)

        course_name_list.sort()

        return course_name_list

    def compare(self, student):
        """ (Student, Student) -> list of str

        Return a list of common enrolled course codes between self and
        student in alphabetical order. Assuming self and student are both
        taking at least one common course.

        Parameters:
        - student: the student we want to compare self with for common
        enrolled courses
        """
        common_list = []

        for course1 in self.courses:
            for course2 in student.courses:
                if course1.code == course2.code:
                    common_list.append(course1.code)
                    break

        common_list.sort()

        return common_list


class Course:
    """
    The class represents an individual course and supports student listing,
    adding and removing students.

    Attributes:
    - self.code (str): the course code of the course
    - self.students (list): the list of students enrolled in the course
    """

    def __init__(self, code):
        """ (Course, str) -> NoneType """
        self.code = code
        self.students = []

    def is_full(self):
        """ (Course) -> bool

        helper method: Return True iff self is full.
        """
        return len(self.students) == 30

    def add_student(self, student):
        """ (Course, Student) -> NoneType

        Add student to list of students of self iff student not in the list

        Parameters:
        - student: the student we want to add to a course
        """
        if self.student_index(student) == -1:
            self.students.append(student)

        else:
            # student already in course (do nothing)
            pass

    def student_index(self, student_obj):
        """ (Course, Student) -> int

        helper method: Return the index of student_obj in self.students. If
        not found, return -1.

        Parameters:
        - student_obj: the student we want to find the index of

        """
        i = 0
        for student in self.students:
            if student.name == student_obj.name:
                return i
            i += 1

        return -1

    def remove_student(self, student):
        """ (Course, Student) -> NoneType

        Remove student from self.students

        Parameters:
        - student: the student we want to remove from the course
        """
        # get index of student in self.students list
        student_idx = self.student_index(student)

        if student_idx != -1:
            self.students.pop(student_idx)
        else:
            # student is not taking course so do nothing
            pass

    def student_list(self):
        """ (Course) -> list

        Return a list of student names in self.students in alphabetical order.
        """
        # assume course has students
        student_name_list = []

        for student in self.students:
            student_name_list.append(student.name)

        student_name_list.sort()

        return student_name_list


# Error classes start here


class CourseFullError(Exception):
    pass


class StudentAlreadyEnrolledError(Exception):
    pass


class StudentNotEnrolledError(Exception):
    pass