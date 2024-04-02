from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)

@db.session.commit
def commit():
  pass

@db.session.rollback  
def rollback():
  pass

