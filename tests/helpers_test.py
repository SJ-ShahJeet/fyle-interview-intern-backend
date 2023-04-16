from core.libs.helpers import get_utc_now
from datetime import datetime


def test_get_assignments_student_1():
    " get utc time should return a datetime object"
    assert isinstance(get_utc_now(), datetime)