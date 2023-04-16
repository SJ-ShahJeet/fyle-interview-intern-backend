from core.server import handle_error
from core.libs.exceptions import FyleError
def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/',
        headers=h_student_1
    )

    assert response.status_code == 200

    status = response.json['status']
    assert status == 'ready'

def test_error():
    assert handle_error is not None
