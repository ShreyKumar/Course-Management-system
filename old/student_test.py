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

class TestStudent(unittest.TestCase):
    """ 
    Test Student Class, its attributes and methods
    """
    def setUp(self):
        self.bill = Student('bill')
        self.david = Student('david')
        self.csc165 = Course('csc165')
        self.csc148 = Course('csc148')
        self.phl100 = Course('phl100')
            #self.bill.add_course(self.csc165)
            #self.bill.add_course(self.csc148)
            #self.david.add_course(self.phl100)
            #self.david.add_course(self.csc148)

#Check to see if self.david.courses has something 
class TestCaseInit(TestStudent):
    def test_init_simple(self):
        """ 
        Ensure that when a student is created that he is not taking any 
        courses.
        """
        self.assertEqual(self.david.courses, [])
        

class TestCaseAdd_Course(TestStudent):
    
    def test_add_course_not_enrolled(self):
        """ 
        (Student) -> NoneType
        Raises StudentAlreadyEnrolledError if self is already enrolled in course
        """
        self.david.add_course(self.csc148)
        self.assertRaises(StudentAlreadyEnrolledError, 
                          self.david.add_course, self.csc148)
        
    def test_add_course_overload(self):
        """
        (Student) -> NoneType
        Raise CourseFullError if enroll self in a course above size 30
        """
        
        # create 30 hypothetical different students named by numbers 1 to 30
        # and then enroll each of them to the same course
        for i in range(0,30):
            hypo_student = Student(str(i))
            hypo_student.add_course(self.csc148)
        
        print(self.csc148.students)
            
        # now we shall try adding david to the already full course
        self.assertRaises(CourseFullError, 
                          self.david.add_course, self.csc148)
        
    def test_add_course_simple1(self):
        """
        Checks to see if Student is enrolled in Course and Course is enrolled in Student
        """
        self.david.add_course(self.csc148)
        
        # check if david is taking csc148
        self.assertEquals(self.david.courses[0], self.csc148)
        # check if csc148 has david enrolled
        self.assertEquals(self.csc148.students[0], self.david)

class TestCaseDrop_Course(TestStudent):
    
    def test_list_courses_not_enroled_david(self):
        """
        Raises StudentNotEnrolledError if attempt to drop course in which student is not enrolled in
        """
        self.assertRaises(StudentNotEnrolledError, self.david.drop_course, self.csc165)
        
    def test_student_already_enrolled(self):
        """
        Raises StudentAlreadyEnrolledError if attempt to add course in which student is already enrolled in
        """
        self.assertRaises(StudentAlreadyEnrolledError, self.david.add_course, self.csc165)
        
    def test_drop_course_invalid(self):
        """
        Raises StudentNotEnrolledError if attempt to drop course in which student is 
        """
        self.assertRaises(StudentNotEnrolledError, self.bill.drop_course, self.phl100)
    
    def test_student_no_exist_drop_course(self):
        """
        Raises StudentDNE_Error if attempt to drop course when student is not in course 
        """
        self.assertRaises(StudentDNE_Error, self.philip.drop_course, self.csc165)    
class is_taking_course(TestStudent):
    pass

class TestCaseList_Courses(TestStudent):
    
    def test_list_courses_bill(self):
        """
        Check for appropriate output if bill is enrolled in courses when calling list_courses()
        """
        
        self.assertEqual(self.bill.courses, ['csc148', 'csc165'])
        
    def test_list_courses_david(self):
        """
        Check for appropriate output if david is enrolled in courses when calling list_courses()
        """
        self.assertEqual(self.david.courses, ['csc148', 'phl100'])

    def test_philip_no_exist_list_courses(self):
        """
        Raise StudentDNE_Error if user tries to list-courses when Student not created
        """
        self.assertRaises(StudentDNE_Error, self.philip.list-courses, )
        

class TestCaseCompare(TestStudent):
    
    def test_bill_david_compare(self):
        """
        Check if common courses of bill and david are evident
        """
        self.assertEqual(self.bill.compare(self.david), ['csc148'])
        
    #def test_bill_philip_no_exist_compare:
        #self.assertRaises(StudentExistsError, self.bill.compare, self.philip)

class TestCourse(unittest.TestCase):
    
    def setUp(self):
        self.csc148 = Course('csc148')

    def test_course_no_exist_drop_student(self):
        self.assertRaises(StudentNotEnrolledError, self.phl100.remove_student, self.bill)
        
class TestCaseRemove_Student(TestStudent):
    
    def test_remove_student_david(self):
        """
        Removes student from a course and checks if student is still enrolled in other course
        """
        self.csc165.remove_student(self.bill)
        self.assertEqual(self.bill.list-courses, ['csc148'])
        
class TestCaseIs_Full(TestStudent):
    def test_full_course(self):
        """
        Checks to see whether csc165 is full
        """
        self.assertFalse(self.csc165.is_full)
        
class TestCase_add_course(TestStudent):
    
    def test_student_add_in_course(self):
        """
        Adds a student in course csc148 and checks if student is enrolled in that course
        """
        self.csc148.add_student(self.bill)
        self.assertEqual(self.bill.list-courses, ['csc148', 'csc165'])
    def test_student_drop_course(self):
        """
        Check if student is removed from the course
        """
        self.phl100.remove_student(self.david)
        self.assertEqual(self.phl100.students, [])

class TestCourse(unittest.TestCase):
    
    def setUp(self):
        self.csc148 = Course('csc148')

    def test_course_no_exist_drop_student(self):
        """
        Raise StudentNotEnrolledError if attempt to drop remove student which is not in. 
        """
        self.assertRaises(StudentNotEnrolledError, self.phl100.remove_student, self.bill)
        

    


if __name__ == '__main__':
    unittest.main(exit=False)
