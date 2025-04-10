from flask import Blueprint, request, jsonify
from .models import Department
from .db import db

bp = Blueprint('api', __name__)

@bp.route('/departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify([d.to_dict() for d in departments]), 200

@bp.route('/departments/<int:id>', methods=['GET'])
def get_department(id):
    department = Department.query.get_or_404(id)
    return jsonify(department.to_dict()), 200

@bp.route('/departments', methods=['POST'])
def add_department():
    data = request.json
    new_dep = Department(
        name=data['name'],
        location=data['location'],
        contact_email=data.get('contact_email')
    )
    db.session.add(new_dep)
    db.session.commit()
    return jsonify(new_dep.to_dict()), 201

@bp.route('/departments/<int:id>', methods=['PUT'])
def update_department(id):
    data = request.json
    department = Department.query.get_or_404(id)
    department.name = data.get('name', department.name)
    department.location = data.get('location', department.location)
    department.contact_email = data.get('contact_email', department.contact_email)
    db.session.commit()
    return jsonify(department.to_dict()), 200

@bp.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return '', 204
