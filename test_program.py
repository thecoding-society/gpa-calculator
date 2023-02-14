import pytest
from program import *

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

    

def test_gpa_class():
    pass

def test_addsubject():
    pass

def test_calc():
    pass

def test_calc_with_negative_credit():
    pass

def test_calc_with_negative_grade_point():
    pass

def test_calc_with_credit_greater_than_8():
    pass

def test_calc_with_grade_point_greater_than_10():
    pass

def test_calc_with_no_subjects():
    pass

def test_calc_with_gpa_greater_than_10():
    pass

def test_calc_with_gpa_less_than_10():
    pass

def test_calc_with_gpa_equal_to_10():
    pass

def test_invalid_credit():
    pass

def test_invalid_grade_point():
    pass

def test_invalid_credit_and_grade_point():
    pass

def test_proper():
    pass