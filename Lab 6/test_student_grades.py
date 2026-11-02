import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ---------- letter_grade ----------
# Invalid input: both sides of the "marks < 0 or marks > 100" check
def test_invalid_marks_negative():
    with pytest.raises(ValueError):
        letter_grade(-1)

def test_invalid_marks_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)

# Valid extremes (these must NOT raise)
def test_marks_zero_is_valid():
    assert letter_grade(0) == "F"

def test_marks_hundred_is_valid():
    assert letter_grade(100) == "S"

# Each boundary: the lowest mark of a band, and one below it
@pytest.mark.parametrize("marks, expected", [
    (90, "S"), (89, "A"),
    (80, "A"), (79, "B"),
    (70, "B"), (69, "C"),
    (60, "C"), (59, "D"),
    (50, "D"), (49, "E"),
    (40, "E"), (39, "F"),
])
def test_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


# ---------- final_marks ----------
def test_final_marks_invalid_internal():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)

def test_final_marks_invalid_external():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)

def test_final_marks_max_valid_no_project():
    assert final_marks(40, 60, False) == 100

def test_final_marks_no_project():
    assert final_marks(30, 40, False) == 70

def test_final_marks_project_below_cap():
    # has_project True, total stays <= 100 -> "total > 100" is False
    assert final_marks(30, 40, True) == 75

def test_final_marks_project_exactly_100():
    assert final_marks(40, 55, True) == 100

def test_final_marks_project_capped_at_100():
    # has_project True, total would be 105 -> "total > 100" is True
    assert final_marks(40, 60, True) == 100


# ---------- exam_eligibility ----------
def test_blocked_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"

def test_blocked_even_with_medical():
    assert exam_eligibility(90, False, True) == "blocked"

def test_eligible():
    assert exam_eligibility(80, True, False) == "eligible"

def test_eligible_exactly_75():
    assert exam_eligibility(75, True, False) == "eligible"

def test_eligible_with_medical_in_range():
    assert exam_eligibility(70, True, True) == "eligible"

def test_eligible_with_medical_exactly_65():
    assert exam_eligibility(65, True, True) == "eligible"

def test_detained_in_range_without_medical():
    assert exam_eligibility(70, True, False) == "detained"

def test_detained_below_65_even_with_medical():
    assert exam_eligibility(64, True, True) == "detained"

def test_detained_low_attendance_no_medical():
    assert exam_eligibility(50, True, False) == "detained"
