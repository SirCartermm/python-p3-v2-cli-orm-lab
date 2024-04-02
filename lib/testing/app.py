from flask import Flask
from models import db, Employee, Department
from lib import helpers

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////path/to/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
  return "Employee Management System"

@app.route('/employees') 
def list_employees():
  helpers.list_employees()
  return "Employees Listed"

@app.route('/employee/create')
def create_employee():
  helpers.create_employee()
  return "Employee Created"

@app.route('/employee/update')  
def update_employee():
  helpers.update_employee()
  return "Employee Updated"

@app.route('/employee/delete')
def delete_employee():
  helpers.delete_employee()
  return "Employee Deleted"

@app.route('/department/<int:dept_id>/employees')
def list_dept_employees(dept_id):
  helpers.list_dept_employees(dept_id)
  return "Department Employees Listed"

if __name__ == '__main__':
  app.run(debug=True)
