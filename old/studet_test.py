# Assignment 1 - Unit Tests for Student
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your group members below, one per line, in format
# Shreyansh Kumar, kumarsh6
# Yun-Yee Megan Yow, yowmegan
# ---------------------------------------------
"""Unit tests for student.py

Submit this file, containing *thorough* unit tests
for your code in student.py.
Note that you should not have any tests involving
standard input or output in here.
"""

import unittest
from student import Student, Course, CourseFullError, StudentAlreadyEnrolledError

########################## Test Student superclass ###############################

class TestStudent(unittest.TestCase):
    """ Test Student Class, its attributes and methods
    
    This superclass will be inherited by TestCase of corresponding methods implemented in the Student class  in student.py
    
    """
    def setUp(self):
        self.bill = Student('bill')
        self.david = Student('david')
        self.csc148 = Course('csc148')
        self.phl100 = Course('phl100')
        self.csc165 = Course('csc165')
        
class TestCaseInit(TestStudent):
    """ 
    Test Cases for Student.__init__()
    Ensure that when a student is created that he is not taking any 
    courses.
    """
    def test_init_simple(self):
        
        self.assertEqual(self.david.courses, []) 

class TestCaseAdd_Course(TestStudent):
    """
    Test cases for Student.add_course(new_course) with new_course being the
    course that a particular Student wants to enroll in.
    """
    def test_add_course_already_enrolled(self):
        """ 
        Raise StudentAlreadyEnrolledError if student is already enrolled in the course
        """
        self.david.add_course(self.csc148)
        self.assertRaises(StudentAlreadyEnrolledError, 
                          self.david.add_course, self.csc148)
        
    def test_add_course_full(self):
        """
        Raise CourseFullError if attempt to add student in an already full class
        """
        # create 30  different hypothetical students named by numbers 1 to 30
        # and then enroll each of them to the same course
        for i in range(0,30):
            hypo_student = Student(str(i))
            hypo_student.add_course(self.csc148)
            
        # now we shall try adding david to the already full course
        self.assertRaises(CourseFullError, 
                          self.david.add_course, self.csc148)
        
    def test_add_course_simple(self):
        
        self.david.add_course(self.csc148)
        
        # check if david is taking csc148
        self.assertEqual(self.david.courses[0], self.csc148)
        
        # check if csc148 has david enrolled
        self.assertEqual(self.csc148.students[0], self.david)
        

class TestCaseDrop_Course(TestStudent):
    """
    Test cases for Student.drop_course(course_obj) with course_obj being the
    course that a particular Student wants to drop. 
    There should be no raised errors whether or not student was taking course
    before trying to drop course
    """
    
    def test_drop_course_nil(self):
        # student not taking course but tries to drop, ensure no errors occur
        
        self.david.drop_course(self.csc148)
        
        self.assertFalse(self.csc148 in self.david.courses)
        self.assertFalse(self.david in self.csc148.students)
    
    def test_drop_course_simple(self):
        
        self.david.add_course(self.csc148)
        self.david.drop_course(self.csc148)
    
        self.assertFalse(self.csc148 in self.david.courses)
        self.assertFalse(self.david in self.csc148.students)
        
class TestCaseIs_Taking_Course(TestStudent):
    """
    Test cases for Student.is_taking_course(course_obj) with course_obj we
    want to find in the list of courses a particular Student is taking.
    """
    def test_is_taking_course_nil(self):
        #check if is_taking_course() returns -1 if student is not enrolled in that course
        self.assertEqual(self.david.is_taking_course(self.csc148), -1)
    
    def test_is_taking_course_simple(self):
        #check if student is in the course
        
        self.david.add_course(self.csc148)
        self.david.add_course(self.phl100)
        
        self.assertEqual(self.david.is_taking_course(self.phl100), 1)

class TestCaseList_Courses(TestStudent):
    """
    Test cases for Student.list_courses()
    """
    
    #Already checking with init? 
    def test_list_course_empty(self):
        
        self.assertEqual(self.david.list_courses(), [])
    
    def test_list_courses_simple(self):
        
        self.david.add_course(self.phl100)
        self.david.add_course(self.csc148)
        self.david.add_course(self.csc165)
        
        self.assertEqual(self.david.courses, ['csc148', 'csc165', 
                                                     'phl100'])
class TestCaseCompare(TestStudent):
    """
    Test cases for Student.compare(other_student) that returns a list of courses that Student and other_student have in common.
    """
    
    def test_compare_both_empty(self):
        #check if common courses of david and bill is nothing
        self.assertEqual(self.david.compare(self.bill), [])
    
    def test_compare_one_empty_student1(self):
        
        self.david.add_course(self.csc148)
        
        #check if common courses of david and bill are still nothing if bill's courses are entirely empty
        self.assertEqual(self.david.compare(self.bill), [])
        
    def test_compare_one_empty_student2(self):
        
        self.bill.add_course(self.csc148)
        
        self.assertEqual(self.david.compare(self.bill), [])
    
    def test_compare_simple(self):
        
        self.david.add_course(self.phl100)
        self.david.add_course(self.csc165)
        self.bill.add_course(self.csc165)
        self.bill.add_course(self.phl100)
        
        #check if common courses exist between both students
        self.assertEqual(self.david.compare(self.bill), ['csc165', 'phl100'])
        

############################ Test Course superclass ##############################

class TestCourse(unittest.TestCase):
    """ Test Course Class, its attributes and methods
    
    This superclass will be inherited by TestCase of corresponding methods implemented in the Course class in student.py
    
    """
    
    def setUp(self):
        """
        
        """
        self.david = Student('david')
        self.bill = Student('bill')
        self.sara = Student('sara')
        self.csc148 = Course('csc148')  
        
class TestCaseInit(TestCourse):
    """ 
    Test Cases for Course.__init__()
    """
    def test_init_simple(self):
        #check if no students are in csc148
        self.assertEqual(self.csc148.students, [])
        
class is_full(TestCourse):
    """
    Test cases for Course.is_full()
    """
    
    def test_is_full_simple1(self):
        
        self.assertFalse(self.csc148.is_full())
    
    def test_is_full(self):
        
        # enrol 30 different hypothetical students to csc148
        for i in range(0,30):
            hypo_student = Student(str(i))
            hypo_student.add_course(self.csc148) 
            
        self.assertTrue(self.csc148.is_full())
        
class TestCaseAdd_Student(TestCourse):
    """
    Test cases for Course.add_student(student_obj) with student_obj being the
    student we want to enrol in Course.
    """ 
    def test_add_student_simple(self):
        #add student to course list
        self.csc148.add_student(self.david)
        #check if student is in csc148
        self.assertTrue(self.david in self.csc148.students)
    
    def test_add_same_student(self):
        #add student twice to list
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.david)
        
        # check that student only added once into list of students of course
        self.assertEqual(len(self.csc148.students), 1)
        
class TestCaseStudent_Index(TestCourse):
    """
    Test cases for Course.student_index(student_obj) with student_obj we
    want to find in the list of students of a particular Course.
    """
    def test_student_index_nil(self):
        #check if is_equal returns -1 if student is not enrolled
        self.assertEqual(self.csc148.student_index(self.david), -1)
    
    def test_student_index_second(self):
        
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.add_student(self.sara)
        #check if returns appropriate student index
        self.assertEqual(self.csc148.student_index(self.sara), 2)
        
    def test_student_index_third(self):
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.add_student(self.sara)
        self.csc148.add_student(self.test)
        
class TestCaseRemove_Student(TestCourse):
    """
    Test cases for Course.remove_student(student_obj)
    There should not be any raised errors whether or not student_obj is in
    the list of students of the Course
    """
    
    def test_remove_student_nil(self):
        # ensure no errors occur when no such student found in course
        self.csc148.remove_student(self.david)
    
    def test_remove_student_simple(self):
        
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.remove_student(self.david)
        
        self.assertEqual(self.csc148.students[0], self.bill)
        
class TestCaseStudent_List(TestCourse):
    """
    Test cases for Course.student_list()
    """  
    def test_student_list_empty(self):
        
        self.assertEqual(self.csc148.student_list(), [])
    
    def test_student_list_simple(self):
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.add_student(self.sara)
        
        self.assertEqual(self.csc148.student_list(), ['bill', 'david', 'sara'])
        
        
            

if __name__ == '__main__':
    unittest.main(exit=False)