from models import Employee, Department
from db import db

def list_employees():
  employees = Employee.query.all()
  return employees

def create_employee(name, department):
  employee = Employee(name=name, department=department)
  db.session.add(employee)
  db.commit()

def update_employee(employee):
  employee.name = "New Name" 
  db.session.commit()

def delete_employee(employee):
  db.session.delete(employee)
  db.session.commit()

def list_dept_employees(dept_id):
  department = Department.query.get(dept_id)
  return department.employees

@db.session.commit  
def commit():
  pass

@db.session.rollback
def rollback():
  pass
