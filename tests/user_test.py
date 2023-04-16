from core.models.users import User
def test_get_user():
    user1 = User.get_by_id(1)
    assert user1.id == 1
    assert user1.username == 'student1'

def test_get_not_existing_user():
    user1 = User.get_by_id(100000)
    assert user1 is None

def test_get_user_by_email():
    user1 = User.get_by_email('student1@fylebe.com')
    assert user1.id == 1
    assert user1.username == 'student1'

