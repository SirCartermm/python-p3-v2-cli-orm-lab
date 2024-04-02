from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
  __tablename__ = 'departments'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))

  employees = db.relationship('Employee', backref='department')

class Employee(db.Model):
  __tablename__ = 'employees'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

  department = db.relationship("Department")

def __repr__(self):
  return f"<Employee {self.name}>"

