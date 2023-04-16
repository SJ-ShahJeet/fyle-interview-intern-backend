from core.models.assignments import Assignment
def test_get_assigment():
    assignmnet = Assignment.get_by_id(1)
    assert assignmnet is not None
    assert assignmnet.id == 1

def test_get_not_existing_assignment():
    assignmnet = Assignment.get_by_id(100000)
    assert assignmnet is  None


def test_get_all_assignments():
    assignmnets = Assignment.get_all()
    assert len(assignmnets) > 3
