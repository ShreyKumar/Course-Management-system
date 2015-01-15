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
from student import Student, Course, CourseFullError
from student import StudentAlreadyEnrolledError

# TEST STUDENT SUPERCLASS #


class TestStudent(unittest.TestCase):
    """ Test Student Class, its attributes and methods

    This superclass will be inherited by TestCase of corresponding methods
    implemented in the Student class  in student.py

    """
    def setUp(self):
        # Students with lower case names
        self.bill = Student('bill')
        self.david = Student('david')

        # Courses with lower case names
        self.csc148 = Course('csc148')
        self.phl100 = Course('phl100')
        self.csc165 = Course('csc165')

        # Courses with upper case names
        self.CSC148 = Course('CSC148')
        self.CSC165 = Course('CSC165')

        # Students with uppercase names
        self.BILL = Student('BILL')
        self.DAVID = Student('DAVID')

        # Students with Boolean names
        self.true = Student(True)


class TestCaseInit(TestStudent):
    """
    Test Cases for Student.__init__()
    """
    def test_init_simple(self):

        self.assertEqual(self.david.courses, [])

    def test_init_diff_student(self):
        """
        test that capital and lower case named courses are different
        """
        self.assertFalse(self.bill is self.BILL)


class TestCaseAdd_Course(TestStudent):
    """
    Test cases for Student.add_course(new_course) with new_course being the
    course that a particular Student wants to enroll in.
    """
    def test_add_course_alredy_enrol(self):
        """
        Raise StudentAlreadyEnrolledError if student is already enrolled in
        course
        """
        self.david.add_course(self.csc148)
        self.assertRaises(StudentAlreadyEnrolledError,
                          self.david.add_course, self.csc148)

    def test_add__bool_already_enrol(self):
        """
        Raise StudentAlreadyEnrolledError if student with bool name is
        already enrolled in course
        """
        self.true.add_course(self.csc148)
        self.assertRaises(StudentAlreadyEnrolledError,
                          self.true.add_course, self.csc148)

    def test_add_course_overload(self):
        """
        Raise CourseFullError if student tries to enroll but course is full
        """

        # create 30  different hypothetical students named by numbers 1 to 30
        # and then enroll each of them to the same course
        for i in range(0, 30):
            hypo_student = Student(str(i))
            hypo_student.add_course(self.csc148)

        # now we shall try adding david to the already full course
        self.assertRaises(CourseFullError,
                          self.david.add_course, self.csc148)

    def test_add_course_simple(self):
        """
        Check if course is added to student class
        """
        self.david.add_course(self.csc148)

        # check if david is taking csc148
        self.assertEqual(self.david.courses[0], self.csc148)

        # check if csc148 has david enrolled
        self.assertEqual(self.csc148.students[0], self.david)

    def test_add_course_bool(self):
        """
        Check if course is added to student(with bool name) class
        """
        self.true.add_course(self.csc148)

        # check if true is taking csc148
        self.assertEqual(self.true.courses[0], self.csc148)

        # check if csc148 has true enrolled
        self.assertEqual(self.csc148.students[0], self.true)


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
        """
        Test if csc148 is still in self.david.courses after adding and dropping
        """

        self.david.add_course(self.csc148)
        self.david.drop_course(self.csc148)

        self.assertFalse(self.csc148 in self.david.courses)
        self.assertFalse(self.david in self.csc148.students)

    def test_drop_course_caps(self):
        """
        Test if Course is still in student courses attribute after adding and
        dropping
        Note: This is different from the above course since course is CSC148
        and not csc148
        """
        self.david.add_course(self.CSC148)
        self.david.drop_course(self.CSC148)

        self.assertFalse(self.CSC148 in self.david.courses)
        self.assertFalse(self.david in self.CSC148.students)

    def test_drop_course_bool_on_caps(self):
        """
        Test if Course is still in student courses attribute after adding and
        dropping
        Note: This is different from the above course since course is CSC148
        and not csc148. Also student is true instead of david
        """
        self.true.add_course(self.CSC148)
        self.true.drop_course(self.CSC148)

        self.assertFalse(self.CSC148 in self.true.courses)
        self.assertFalse(self.true in self.CSC148.students)

    def test_drop_course_bool(self):
        """
        Test if Course is still in student courses attribute after adding and
        dropping
        Note: This is different from the above course since student is true
        and not david.
        """
        self.true.add_course(self.CSC148)
        self.true.drop_course(self.CSC148)

        self.assertFalse(self.csc148 in self.true.courses)
        self.assertFalse(self.true in self.csc148.students)


class TestCaseIs_Taking_Course(TestStudent):
    """
    Test cases for Student.is_taking_course(course_obj) with course_obj we
    want to find in the list of courses a particular Student is taking.
    """
    def test_is_taking_course_nil(self):

        self.assertEqual(self.david.is_taking_course(self.csc148), -1)

    def test_is_taking_course_simple(self):
        """
        Check to see if index of student is returned in the method
        """

        self.david.add_course(self.phl100)

        self.assertEqual(self.david.is_taking_course(self.phl100), 0)

    def test_is_taking_course_multiple(self):
        """
        Check to see if index of student is returned in the method
        """

        self.david.add_course(self.csc148)
        self.david.add_course(self.phl100)

        self.assertEqual(self.david.is_taking_course(self.phl100), 1)


class TestCaseList_Courses(TestStudent):
    """
    Test cases for Student.list_courses()
    """

    def test_list_course_empty(self):
        """
        Check if Student is initially enrolled in nothing
        """
        self.assertEqual(self.david.courses, [])

    def test_list_courses_simple(self):
        self.david.add_course(self.phl100)

        self.assertEqual(self.david.list_courses(), ['phl100'])

    def test_list_courses_sorted(self):

        self.david.add_course(self.phl100)
        self.david.add_course(self.csc148)
        self.david.add_course(self.csc165)

        self.assertEqual(self.david.list_courses(), ['csc148', 'csc165',
                                                     'phl100'])

    def test_list_courses_bools(self):
        self.true.add_course(self.csc165)
        self.true.add_course(self.csc148)

        self.assertEqual(self.true.list_courses(), ['csc148', 'csc165'])


class TestCaseCompare(TestStudent):
    """
    Test cases for Student.compare(other_student) that returns a list
    of courses that Student and other_student have in common.
    """

    def test_compare_both_empty(self):
        """
        Checks to see if common courses of both students is nothing since
        nobody is enrolled in the course
        """
        self.assertEqual(self.david.compare(self.bill), [])

    def test_compare_one_empty1(self):
        """
        Checks to see if compare returns no course if one of the students are
        not enrolled in any courses
        """

        self.david.add_course(self.csc148)

        self.assertEqual(self.david.compare(self.bill), [])

    def test_compare_one_emtpy2(self):
        self.david.add_course(self.csc148)
        self.assertEqual(self.bill.compare(self.david), [])

    def test_compare_simple(self):
        """
        Checks if both courses return a common list of courses
        """

        self.david.add_course(self.phl100)
        self.david.add_course(self.csc165)
        self.bill.add_course(self.csc165)
        self.bill.add_course(self.phl100)

        # returns a common list of courses of david and bill
        self.assertEqual(self.david.compare(self.bill), ['csc165', 'phl100'])

    def test_compare_no_similar(self):

        self.david.add_course(self.phl100)
        self.david.add_course(self.csc165)
        self.bill.add_course(self.csc148)

        self.assertEqual(self.david.compare(self.bill), [])

    def test_compare_diff_num(self):
        self.david.add_course(self.csc148)
        self.david.add_course(self.csc165)
        self.bill.add_course(self.csc148)

        self.assertEqual(self.david.compare(self.bill), ['csc148'])
        self.assertEqual(self.bill.compare(self.david), ['csc148'])


# TEST COURSE SUPERCLASS #

class TestCourse(unittest.TestCase):
    """ Test Course Class, its attributes and methods

    This superclass will be inherited by TestCase of corresponding methods
    implemented in the Course class in student.py

    """

    def setUp(self):

        self.david = Student('david')
        self.bill = Student('bill')
        self.sara = Student('sara')
        self.csc148 = Course('csc148')

        # FROM TEST STUDENT SUPERCLASS #

        # Courses with upper case names
        self.CSC148 = Course('CSC148')
        self.CSC165 = Course('CSC165')

        # Students with uppercase names
        self.BILL = Student('BILL')
        self.DAVID = Student('DAVID')

        # Students with Boolean names
        self.true = Student(True)
        self.false = Student(False)

        # Students with number names
        self.c_4_k_u_m_a_r_s = Student('c4kumars')


class TestCaseInit(TestCourse):
    """
    Test Cases for Course.__init__()
    """
    def test_init_simple(self):

        self.assertEqual(self.csc148.students, [])

    def test_init_diff_course(self):
        """
        test that capital and lower case named courses are different
        """
        self.assertFalse(self.csc148 is self.CSC148)


class is_full(TestCourse):
    """
    Test cases for Course.is_full()
    """

    def test_is_full_simple(self):
        """
        Checks to see if is_full() returns false if course is not full
        """

        self.assertFalse(self.csc148.is_full())

    def test_is_full_caps(self):
        """
        Checks to see if is_full() returns false if course with capitals is
        not full
        """

        self.assertFalse(self.CSC148.is_full())

    def test_is_full(self):
        """
        Checks to see if returns true if course is already full
        """
        # enrol 30 different hypothetical students to csc148
        for i in range(0, 30):
            hypo_student = Student(str(i))
            hypo_student.add_course(self.csc148)

        self.assertTrue(self.csc148.is_full())

    def test_is_full_bools(self):
        """
        Checks to see if returns true if course is already full
        """
        # enrol 30 different hypothetical students to csc148
        for i in range(0, 30):
            hypo_student = Student(str(i))
            hypo_student.add_course(self.CSC148)

        self.assertTrue(self.CSC148.is_full())


class TestCaseAdd_Student(TestCourse):
    """
    Test cases for Course.add_student(student_obj) with student_obj being the
    student we want to enrol in Course.
    """
    def test_add_student_simple(self):
        """
        Check to see if student exists in Student list when added
        """
        # add student david
        self.csc148.add_student(self.david)

        self.assertTrue(self.david in self.csc148.students)

    def test_add_student_bool_on_caps(self):
        """
        Check to see if student with bool name exists in Student list when
        added to course with capitals
        """
        # add student david
        self.CSC148.add_student(self.true)

        self.assertTrue(self.true in self.CSC148.students)

    def test_add_same_student(self):
        """
        Check to see if student is added only once when attempt to add two
        """
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.david)

        # check that student only added once into list of students of course
        self.assertEqual(len(self.csc148.students), 1)

    def test_add_diff_student(self):
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.DAVID)

        self.assertEqual(self.csc148.students, [self.david, self.DAVID])


class TestCaseStudent_Index(TestCourse):
    """
    Test cases for Course.student_index(student_obj) with student_obj we
    want to find in the list of students of a particular Course.
    """
    def test_student_index_nil(self):
        """
        Check to see if return -1 if student does not exist
        """
        self.assertEqual(self.csc148.student_index(self.david), -1)

    def test_student_index_simple(self):
        """
        Check to see if the third element index is returned as 2
        """
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.add_student(self.sara)

        self.assertEqual(self.csc148.student_index(self.sara), 2)


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
        self.csc148.remove_student(self.david)

        self.assertEqual(self.csc148.students, [])

    def test_remove_student_multiple(self):
        """
        Check to see if Student.courses shifts in index if first student
        is deleted
        """
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.remove_student(self.david)

        self.assertEqual(self.csc148.students[0], self.bill)


class TestCaseStudent_List(TestCourse):
    """
    Test cases for Course.student_list()
    """
    def test_student_list_empty(self):
        """
        Check if returned an empty list if student_list() called on an
        empty string
        """
        self.assertEqual(self.csc148.student_list(), [])

    def test_student_list_simple_sorted(self):
        """
        Check if returned list with students when added to the student
        """
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.bill)
        self.csc148.add_student(self.sara)

        self.assertEqual(self.csc148.student_list(), ['bill', 'david', 'sara'])

    def test_student_list_names(self):
        self.csc148.add_student(self.david)
        self.csc148.add_student(self.DAVID)

        self.assertEqual(self.csc148.student_list(), ['DAVID', 'david'])

    def test_student_list_simple(self):
        """
        Check if returned true when student is added to same course in caps
        lock
        """
        self.CSC148.add_student(self.sara)

        self.assertEqual(self.CSC148.student_list(),  ['sara'])

    def test_student_list_caps_with_bool(self):
        self.CSC148.add_student(self.true)

        self.assertEqual(self.CSC148.student_list(), [True])

if __name__ == '__main__':
    unittest.main(exit=False)