from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Employee

def get_employees(db: Session, skip=0, limit=10):
    return db.query(Employee).offset(skip).limit(limit).all()

def get_employee_count_by_department(db: Session):
    return db.query(Employee.department, func.count(Employee.id)).group_by(Employee.department).all()