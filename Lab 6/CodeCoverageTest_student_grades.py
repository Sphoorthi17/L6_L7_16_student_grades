import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ---------- letter_grade: one test per grade band + invalid input ----------
def test_invalid_marks_negative():
    with pytest.raises(ValueError):
        letter_grade(-1)

def test_s_grade():
    assert letter_grade(95) == "S"

def test_a_grade():
    assert letter_grade(85) == "A"

def test_b_grade():
    assert letter_grade(75) == "B"

def test_c_grade():
    assert letter_grade(65) == "C"

def test_d_grade():
    assert letter_grade(55) == "D"

def test_e_grade():
    assert letter_grade(45) == "E"

def test_f_grade():
    assert letter_grade(30) == "F"


# ---------- final_marks ----------
def test_final_marks_invalid_internal():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)

def test_final_marks_no_project():
    assert final_marks(30, 40, False) == 70

def test_final_marks_project_capped_at_100():
    assert final_marks(40, 60, True) == 100


# ---------- exam_eligibility ----------
def test_eligible():
    assert exam_eligibility(80, True, False) == "eligible"

def test_blocked_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"

def test_eligible_with_medical():
    assert exam_eligibility(70, True, True) == "eligible"

def test_detained():
    assert exam_eligibility(50, True, False) == "detained"
