# Assignment 1 - Managing students!
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your group members below, one per line, in format
# <full name>, <utorid>
# Yun-Yee Megan Yow, yowmegan
# Shreyansh Kumar, kumarsh6
# ---------------------------------------------
"""Interactive console for assignment.

This module contains the code necessary for running the interactive console.
As provided, the console does nothing interesting: it is your job to build
on it to fulfill all the given specifications.

run: Run the main interactive loop.
"""
from student import Student, Course

# Stack Implementation Start Here


class Stack:
    """ A stack containing successful commands

    The class represents a command stack and supports pushing commands at the
    bottom, removing the latest command added and empty checking.

    Attributes:
    - self.commands (list of list of str): the list of successful commands
    """

    def __init__(self):
        """ (Stack) -> NoneType """

        self.commands = []

    def push(self, item):
        self.commands.append(item)

    def pop(self):
        """
        removes last item added
        """
        return self.commands.pop()

    def is_empty(self):
        """
        Return True iff self.commands is empty
        """
        return self.commands == []

# Error Classes Start Here


class StudentExistsError(Exception):
    pass


class StudentDNE_Error(Exception):
    pass


class CourseFullError(Exception):
    pass


class CourseDNE_Error(Exception):
    pass


class StudentAlreadyEnrolledError(Exception):
    pass


class StudnetNotEnrolledError(Exception):
    pass


# Helper Function Start Here


def get_course(code, CourseList):

    """ (str) -> Course or CourseDNE_Error

    Return Course for corresponding code iff code is in CourseList, else raise
    CourseDNE_Error.
    """
    for course in CourseList:
        if code == course.code:
            return course

    raise CourseDNE_Error


def get_student(name, StudentList):

    """ (str, list) -> Student

    Return Student for corresponding name iff name is in StudentList, else
    raise StudentDNE_Error
    """

    for student in StudentList:
        if name == student.name:
            return student

    raise StudentDNE_Error


def student_enrolled(name, course_code, StudentList):

    """ (str, str) -> Course

    Return true iff name is enrolled in course, assuming name and course_code
    is already in StudentList and CourseList respectively.
    """
    # this should not raise any errors assuming name is in StudentList
    student = get_student(name, StudentList)

    for course in student.courses:
        if course.code == course_code:
            return course

    raise StudnetNotEnrolledError


def create_student(name, StudentList):

    """ (str) -> Student

    Create new Student with given name, append to StudentList and return it.
    """
    new_student = Student(name)
    StudentList.append(new_student)
    return new_student


def create_course(code, CourseList):

    """ (str) -> Course

    Create new Course with given code, append to CourseList and return it.
    """
    new_course = Course(code)
    CourseList.append(new_course)
    return new_course


def print_items(list):

    """ (list of str) -> str

    Return the individual items in list in string representation
    """
    print_message = ''

    for item in list:
        print_message = print_message + ', ' + item

    return print_message[2:]


# Action Function Start Here

def create(name, command_list, StudentList, Commands):

    """ (str, list) -> NoneType

    Creates a student profile with name and if successful, push command_list
    onto a stack.
    """
    try:
        # check if student_name has already been created
        get_student(name, StudentList)

    except StudentDNE_Error:
        # if student_name not created, create student
        create_student(name, StudentList)
        Commands.push(command_list)
        return

    Commands.push(command_list)
    print('ERROR: Student {} already exists.'.format(name))


def enrol(name, code, command_list, StudentList, CourseList, Commands):

    """ (str, str, list, list) -> NoneType

    Enrol a student with name to course code and if successful, push
    command_list onto a stack.
    """

    from student import StudentAlreadyEnrolledError, CourseFullError

    # check if course_code not in CourseList, if not create course_obj
    try:
        course_obj = get_course(code, CourseList)
    except CourseDNE_Error:
        course_obj = create_course(code, CourseList)

    # check if student_name in StudentList, if not print error
    try:
        student_obj = get_student(name, StudentList)
    except StudentDNE_Error:
        print('ERROR: Student', name, 'does not exist.')
        return

    try:
        # student_obj adds student to course (add_student method)
        student_obj.add_course(course_obj)

    except StudentAlreadyEnrolledError:
        return

    except CourseFullError:
        print('ERROR: Course ', code, ' is full.')
        return

    # this line is reached iff no errors occur
    Commands.push(command_list)


def drop(name, code, command_list, StudentList, CourseList, Commands):

    """ (str, str, list) -> NoneType

    Drop course code iff student name is enrolled in it. If successful, push
    command_list onto a stack.
    """

    try:
        # check if name in StudentList, StudentDNE_Error raised otherwise
        student_obj = get_student(name, StudentList)

        # check if such a course exists, CourseDNE_Error raised otherwise
        course_obj = get_course(code, CourseList)

        # check if student is enrolled in course, StudnetNotEnrolledError
        # rasied otherwise
        course_obj = student_enrolled(name, code, StudentList)
        student_obj.drop_course(course_obj)

    except StudentDNE_Error:
        print('ERROR: Student', name, 'does not exist.')
        return

    except CourseDNE_Error:
        # do nothing if course DNE
        return

    except StudnetNotEnrolledError:
        # do nothing if student is not enrolled
        return

    # this line is reached iff no errors occur
    Commands.push(command_list)


def list_courses(name, command_list, StudentList, Commands):

    """ (str) -> Nonetype

    Lists the courses that a student with name is taking.
    """

    try:
        student_obj = get_student(name, StudentList)

    except StudentDNE_Error:
        print('ERROR: Student', name, 'does not exist.')
        return

    if student_obj.courses == []:
        print(name, 'is not taking any courses.')
        return

    print(name, 'is taking', print_items(student_obj.list_courses()))
    Commands.push(command_list)


def common_courses(name1, name2, command_list, StudentList, Commands):

    """ (str, str) -> NoneType

    Lists the courses that name1 and name2 are both enrolled in.
    """

    # check if student1_name exists in StudentList
    try:
        student1_obj = None
        student1_obj = get_student(name1, StudentList)

    except StudentDNE_Error:
        print('ERROR: Student', name1, 'does not exist.')

    # check if student2_name exists in StudentList
    try:
        student2_obj = get_student(name2, StudentList)

    except StudentDNE_Error:
        print('ERROR: Student', name2, 'does not exist.')
        return

    if student1_obj is not None:
        print(print_items(student1_obj.compare(student2_obj)))
        Commands.push(command_list)


def class_list(code, command_list, CourseList, Commands):

    """ (str) -> NoneType

    Lists students who are successfully enrolled in course code.
    """
    try:
        course_obj = get_course(code, CourseList)

    except CourseDNE_Error:
        return

    if course_obj.students == []:
        print('No one is taking {}.'.format(code))
        Commands.push()
        return

    print(print_items(course_obj.student_list()))
    Commands.push(command_list)


def undo(StudentList, CourseList, Commands):

    """ (NoneType) -> NoneType

    Perform undo action according to the last successful command in Commands.
    """

    if Commands.is_empty():
        print("ERROR: No commands to undo.")
        return

    command_list = Commands.pop()

    action = command_list[0]

    if not(action == 'create' or action == 'enrol' or action == 'drop'):
        return

    elif action == 'create':
        # do nothing here
        return

    student_name = command_list[1]
    course_code = command_list[2]

    student_obj = get_student(student_name, StudentList)
    course_obj = get_course(course_code, CourseList)

    if action == 'enrol':
        student_obj.drop_course(course_obj)

    elif action == 'drop':
        # student_obj adds student to course (add_student method)
        student_obj.add_course(course_obj)


def undo_nth(n, StudentList, CourseList, Commands):

    """ (int) -> NoneType

    Call undo() n times
    """

    counter = 0
    while counter < n:
        undo(StudentList, CourseList, Commands)
        counter += 1


# Interactive Loop Start Here


def run():

    """ (NoneType) -> NoneType

    Run the main interactive loop.
    """
    CourseList = []
    StudentList = []
    Commands = Stack()

    while True:
        command = input('')

        if command == 'exit':
            break

        elif command == '':
            print('Unrecognized command!')

        else:
            process_command(command, StudentList, CourseList, Commands)


def process_command(command, StudentList, CourseList, Commands):

    """ (str) -> NoneType

    Processes the command and calls the appropriate functions.
    """

    command_list = command.split()

    action = command_list[0]

    if action == 'create':

        # assignment statement
        student_name = command_list[2]

        create(student_name, command_list, StudentList, Commands)

    elif action == 'enrol':

        # assignment statements
        student_name = command_list[1]
        course_code = command_list[2]

        # check if student_name exists, if not print error
        enrol(student_name, course_code, command_list, StudentList,
              CourseList, Commands)

    elif action == 'drop':

        # assignment statements
        student_name = command_list[1]
        course_code = command_list[2]

        drop(student_name, course_code, command_list, StudentList,
             CourseList, Commands)

    elif action == 'list-courses':

        # assignment statement
        student_name = command_list[1]

        list_courses(student_name, command_list, StudentList, Commands)

    elif action == 'common-courses':

        # assignment statements
        student1_name = command_list[1]
        student2_name = command_list[2]

        common_courses(student1_name, student2_name, command_list,
                       StudentList, Commands)

    elif action == 'class-list':

        # assignment statement
        course_code = command_list[1]

        class_list(course_code, command_list, CourseList, Commands)

    elif action == 'undo':
        # default num_undo
        num_undo = 1

        # assign num_undo to a different num if input is undo <n>
        if len(command_list) == 2:
            num_undo = int(command_list[1])

        undo_nth(num_undo, StudentList, CourseList, Commands)

    else:
        print('Unrecognized command!')


if __name__ == '__main__':
    run()
