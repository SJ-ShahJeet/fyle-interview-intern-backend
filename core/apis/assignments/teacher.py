from flask import Blueprint, make_response, jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.libs.assertions import assert_valid

from .schema import AssignmentSchema, AssignmentSubmitSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)


@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments(p):
    """Returns list of assignments"""
    students_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    students_assignments_dump = AssignmentSchema().dump(students_assignments, many=True)
    return APIResponse.respond(data=students_assignments_dump)


@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignment(p, incoming_payload):
    """Create or Edit an assignment"""
    if len(incoming_payload["grade"])!=1:
        return make_response(jsonify({'error':"ValidationError","status_code":"400","message":"Requested assignment not found"}),400)

    all_assignments = Assignment.get_all()
    is_assignment_found = False
    is_assignment_belongs_to_this_teacher = False
    is_already_graded = False
    for assignment in all_assignments:
        if assignment.id == incoming_payload["id"] and assignment.teacher_id != p.teacher_id:
            is_assignment_belongs_to_this_teacher = True
        if assignment.id == incoming_payload["id"]:
            is_assignment_found = True
        if assignment.id == incoming_payload["id"] and assignment.state == "GRADED":
            is_already_graded = True
    if is_already_graded:
        return make_response(jsonify({'error':"FyleError","status_code":"400","message":"assignment is already graded"}),400)
    if is_assignment_belongs_to_this_teacher:
        return make_response(jsonify({'error':"FyleError","status_code":"400","message":"The assignment not belongs to this teacher"}),400)

    if not is_assignment_found:
        return make_response(jsonify({'error':"FyleError","status_code":"400","message":"Requested assignment not found"}),404)
    

    Assignment.s_grade(
        _id=incoming_payload["id"],
        grade = incoming_payload["grade"],
        principal=p
    )
    db.session.commit()
    res = Assignment.get_by_id(incoming_payload["id"])
    dmp = AssignmentSchema().dump(res)
    return APIResponse.respond(data=dmp)

