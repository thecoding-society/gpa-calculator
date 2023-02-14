import pytest
from program import *

# Subject class test cases

def test_subject_class():
    # Test if the subject class is defined
    obj = subject(4, 10)
    assert obj.credit == 4
    assert obj.grade_point == 10

    obj = subject(3, 9)
    assert obj.credit == 3
    assert obj.grade_point == 9

    # raise an error if the credit is not an integer
    with pytest.raises(TypeError):
        obj = subject(3.5, 9)
    with pytest.raises(TypeError):
        obj = subject('three', 9)
    with pytest.raises(TypeError):
        obj = subject(True, 9)

    # raise an error if the grade_point is not an integer
    with pytest.raises(TypeError):
        obj = subject(3, 9.5)
    with pytest.raises(TypeError):
        obj = subject(3, 'nine')
    with pytest.raises(TypeError):
        obj = subject(3, True)

    # raise an error if the credit and grade point is not negative
    with pytest.raises(ValueError):
        obj = subject(-3, 9)
    with pytest.raises(ValueError):
        obj = subject(3, -9)
    with pytest.raises(ValueError):
        obj = subject(-3, -9)
    
# GPA class test cases

# addsubject function test cases

def test_addsubject():
    # create an object of the gpa class
    obj = gpa()

    # Test if the addsubject function is defined
    obj.addsubject(4, 10)
    assert obj.no_of_subjects == 1
    assert obj.sub[0].credit == 4
    assert obj.sub[0].grade_point == 10

    obj.addsubject(3, 9)
    assert obj.no_of_subjects == 2
    assert obj.sub[1].credit == 3
    assert obj.sub[1].grade_point == 9


def test_invalid_credit():
    with pytest.raises(TypeError):
        obj = subject(3.5, 9)
    with pytest.raises(TypeError):
        obj = subject('three', 9)
    with pytest.raises(TypeError):
        obj = subject(True, 9)


def test_invalid_grade_point():
    with pytest.raises(TypeError):
        obj = subject(3, 9.5)
    with pytest.raises(TypeError):
        obj = subject(3, 'nine')
    with pytest.raises(TypeError):
        obj = subject(3, True)


def test_invalid_credit_and_grade_point():
    obj = gpa()
    # raise an error if the credit and grade point is not negative
    with pytest.raises(ValueError):
        obj.addsubject(-3, 9)
    with pytest.raises(ValueError):
        obj.addsubject(3, -9)
    with pytest.raises(ValueError):
        obj.addsubject(-3, -9)


def test_credit_greater_than_8():
    obj = gpa()

    # raise an error if the credit is greater than 8
    with pytest.raises(ValueError):
        obj.addsubject(9, 9)
    with pytest.raises(ValueError):
        obj.addsubject(13, 9)


def test_grade_point_greater_than_10():
    obj = gpa()

    # raise an error if the grade point is greater than 10
    with pytest.raises(ValueError):
        obj.addsubject(3, 11)
    with pytest.raises(ValueError):
        obj.addsubject(3, 15)

# calc function test cases

def test_calc_1():
    obj = gpa()

    # Test if the calc function is defined
    obj.addsubject(4, 10)
    obj.addsubject(3, 9)
    obj.addsubject(3, 8)
    obj.addsubject(2, 7)
    obj.addsubject(2, 7)
    obj.addsubject(1, 9)
    obj.addsubject(3, 8)
    obj.addsubject(2, 3)
    obj.calc()

    assert obj.gpa == 7.9


def test_calc_2():
    obj = gpa()

    # Test if the calc function is defined
    obj.addsubject(4, 10)
    obj.addsubject(3, 10)
    obj.addsubject(3, 10)
    obj.addsubject(2, 10)
    obj.addsubject(2, 10)
    obj.addsubject(1, 10)
    obj.addsubject(3, 10)
    obj.addsubject(2, 10)
    obj.addsubject(2, 10)
    obj.calc()

    assert obj.gpa == 10


def test_calc_3():
    obj = gpa()

    # Test if the calc function is defined
    obj.addsubject(4, 7)
    obj.addsubject(3, 7)
    obj.addsubject(3, 7)
    obj.addsubject(2, 7)
    obj.addsubject(2, 7)
    obj.addsubject(1, 7)
    obj.addsubject(3, 7)
    obj.addsubject(2, 7)
    obj.addsubject(2, 7)
    obj.calc()

    assert obj.gpa == 7


def test_calc_4():
    obj = gpa()

    # Test if the calc function is defined
    obj.addsubject(2, 8)
    obj.addsubject(3, 8)
    obj.addsubject(3, 7)
    obj.addsubject(4, 8)
    obj.addsubject(2, 10)
    obj.addsubject(4, 9)
    obj.addsubject(4, 9)
    obj.addsubject(3, 8)
    obj.calc()

    assert obj.gpa == 8.36


def test_calc_with_no_subjects():
    obj = gpa()

    # Test if the calc function is defined
    with pytest.raises(ValueError):
        obj.calc()

    assert obj.gpa == 0.0

# display function test cases

def test_display():
    pass

# gpa class overall test cases
def test_gpa_class():
    pass