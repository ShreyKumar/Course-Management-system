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
# 
#
# ---------------------------------------------
"""Interactive console for assignment.

This module contains the code necessary for running the interactive console.
As provided, the console does nothing interesting: it is your job to build
on it to fulfill all the given specifications.

run: Run the main interactive loop.
"""
from student import Student, Course

########################## Stack Implementation ############################
class Stack:
    
    def __init__(self):
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
        
############################# Constants #################################        

StudentList = []
CourseList = []
Commands = Stack()

CREATE = 'create'
ENROL = 'enrol'
DROP = 'drop'
EXIT = 'exit'
LIST_COURSES = 'list-courses'
COMMON_COURSES = 'common-courses'
CLASS_LIST = 'class-list'
UNDO = 'undo'

######################## Error Classes ############################

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

######################## Helper Functions ############################

def get_course(code):
    """ (str) -> Course or CourseDNE_Error
    
    Return Course for corresponding code iff code is in CourseList, else 
    raise CourseDNE_Error    
    """
    for course in CourseList:
        if code == course.code:
            return course
   
    raise CourseDNE_Error  

def get_student(name):
    """ (str) -> Student or StudentDNE_Error
    
    Return Student for corresponding name iff name is in StudentList, else 
    raise StudentDNE_Error
    """

    for student in StudentList:
        if name == student.name:
            return student

    raise StudentDNE_Error

def student_enrolled(name, course_code):
    """ (str, str) -> Course
    
    Return true iff name is enrolled in course, assuming name and course_code 
    is already in StudentList and CourseList respectively.
    """
    # this should not raise any errors assuming name is in StudentList
    student = get_student(name)
    
    for course in student.courses:
        if course.code == course_code:
            return course
        
    raise StudnetNotEnrolledError  

def create_student(name):
    """ (str) -> Student
    
    Create new Student with given name, append to StudentList and return it.
    """
    new_student = Student(name)
    StudentList.append(new_student)
    return new_student    
   
def create_course(code):
    """ (str) - > Course
    
    Create new Course with given code, append to CourseList and return it.
    """
    new_course = Course(code)
    CourseList.append(new_course)
    return new_course

def print_items(list):
    
    print_message = ''
    
    for item in list:
        print_message = print_message + ', ' + item
    
    return print_message[2:]     

############################ Action Functions ##############################

def create(name, command_list):
    """ (str, list) -> NoneType
    
    Creates a student profile with name and if successful, push command_list
    onto a stack.
    """ 
    try:
        # check if student_name has already been created 
        get_student(name) 
              
    except StudentDNE_Error:
        # if student_name not created, create student
        create_student(name)
        Commands.push(command_list)
        return
    
    print('ERROR: Student {} already exists.'.format(name))

def enrol(name, code, command_list):
    """ (str, str, list) -> NoneType
    
    Enrol a student with name to course code and if successful, push
    command_list onto a stack.
    """
    
    from student import StudentAlreadyEnrolledError, CourseFullError
    
    # check if course_code not in CourseList, if not create course_obj
    try:
        course_obj = get_course(code)
    except CourseDNE_Error:   
        course_obj = create_course(code) 
          
    # check if student_name in StudentList, if not print error
    try:
        student_obj = get_student(name)                
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
    
def drop(name, code, command_list):
    """ (str, str, list) -> NoneType
    
    Drop course code iff student name is enrolled in it. If successful, push
    command_list onto a stack.
    """
    
    try:
        # check if name in StudentList, StudentDNE_Error raised otherwise
        student_obj = get_student(name)
        
        # check if such a course exists, CourseDNE_Error raised otherwise
        course_obj = get_course(code)
        
        # check if student is enrolled in course, StudnetNotEnrolledError
        # rasied otherwise
        course_obj = student_enrolled(name, code)
        
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
    
def list_courses(name):
    """ (str) -> Nonetype
    
    Lists the courses that a student with name is taking.
    """
    
    try:
        student_obj = get_student(name)
        
    except StudentDNE_Error:
        print ('ERROR: Student', name, 'does not exist.')
        return
    
    if student_obj.courses == []:
        print( name, 'is not taking any courses.')
        return
        
    print(print_items(student_obj.list_courses()))

def common_courses(name1, name2):
    """ (str, str) -> NoneType
    
    Lists the courses that name1 and name2 are both enrolled in.
    """
    
    # check if student1_name exists in StudentList
    try:
        student1_obj = get_student(name1)
    except StudentDNE_Error:
        print('ERROR: Student', name1, 'does not exist.')
        return
        
    # check if student2_name exists in StudentList
    try:
        student2_obj = get_student(name2)
        
    except StudentDNE_Error:
        print('ERROR: Student', name2, 'does not exist.')
        return
    

    print(print_items(student1_obj.compare(student2_obj)))
    
def class_list(code): 
    """ (str) -> NoneType
    
    Lists students who are successfully enrolled in course code.
    """
    try:
        course_obj = get_course(code)
            
    except CourseDNE_Error:
        return
    
    if course_obj.students == []:
        print('No one is taking {}'.format(code))
        return      
    
    print(print_items(course_obj.student_list()))
 

def undo():
    """ (NoneType) -> NoneType
    
    Perform undo action according to the last successful command in Commands.
    """

    if Commands.is_empty():
        print("No commands to undo.")
        return
        
    command_list = Commands.pop()
        
    action = command_list[0]    
    
    if action != ENROL or action != CREATE or action != DROP:
        return

    student_name = command_list[1]
    course_code = command_list[2] 
    
    student_obj = get_student(student_name)  
    course_obj = get_course(course_code)

    if action == CREATE:
        pass #do nothing here
    
    elif action == ENROLL:       
        student_obj.drop_course(course_obj)   
   
    elif action == DROP:
        # student_obj adds student to course (add_student method)
        student_obj.add_course(course_obj)  

def undo_nth(n):
    """ (int) -> NoneType
    
    Call undo() n times
    """
    
    counter = 0
    while counter <  n:
        undo()
        counter += 1
    


########################################################################

# Interactive loop 

def run():
    """ (NoneType) -> NoneType

    Run the main interactive loop.
    """

    while True:
        command = input('')

        if command == 'exit':
            break        
        
        process_command(command)
        
def process_command(command):
    """ (str) -> NoneType
    
    Processes the command and calls the appropriate functions.
    """
    
    command_list = command.split()
    
    action = command_list[0]
    
    if action == CREATE:
        
        # assignment statement
        student_name = command_list[2]
        
        create(student_name, command_list)
        
    elif action == ENROL:
        
        # assignment statements
        student_name = command_list[1]
        course_code = command_list[2]
        
        # check if student_name exists, if not print error
        enrol(student_name, course_code, command_list)
        
    elif action == DROP:
        
        # assignment statements
        student_name = command_list[1]
        course_code = command_list[2]
        
        drop(student_name, course_code, command_list)
        
    elif action == LIST_COURSES:
        
        # assignment statement
        student_name = command_list[1]
        
        list_courses(student_name)
        
    elif action == COMMON_COURSES:
        
        # assignment statements
        student1_name = command_list[1]
        student2_name = command_list[2]
        
        common_courses(student1_name, student2_name)
        
    elif action == CLASS_LIST:
        
        # assignment statement
        course_code = command_list[1]
        
        class_list(course_code)
        
    elif action == UNDO:
        num_undo = 1
            
        # assign num_undo to a different num if input is undo <n>
        if len(command_list) == 2:
            num_undo = command_list[1]
            
        undo_nth(num_undo)
        
    else:
        print('Unrecognized command!')

if __name__ == '__main__':
    run()
    
