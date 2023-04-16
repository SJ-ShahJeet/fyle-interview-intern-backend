from core.libs.assertions import base_assert, assert_valid, assert_auth, assert_true, assert_found
def test_valid_assert():
    try:
        assert_valid(False)
    except Exception as e:
        assert e.status_code == 400
        assert e.message == 'BAD_REQUEST'

def test_auth_assert():
    try:
        assert_auth(False)
    except Exception as e:
        assert e.status_code == 401
        assert e.message == 'UNAUTHORIZED'

def test_found_assert():
    try:
        assert_found(False)
    except Exception as e:
        assert e.status_code == 404
        assert e.message == 'NOT_FOUND'

def test_true_assert():
    try:
        assert_found(False)
    except Exception as e:
        assert e.status_code == 403
        assert e.message == 'FORBIDDEN'
