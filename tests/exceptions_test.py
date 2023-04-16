from core.libs.exceptions import FyleError
def test_exception_default_status_code():
    exception = FyleError(message="test",status_code=500)
    assert exception.status_code == 500
    assert exception.message == "test"

def test_exception_dic():
    exception = FyleError(message="test",status_code=500)

    dict  = exception.to_dict()
    assert dict['message'] == "test"
