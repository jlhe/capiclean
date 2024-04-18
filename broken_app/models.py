from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


# Modelo usuario
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    def __init__(self, username, password, role_id):
        self.username = username
        self.password = password
        self.role_id = role_id

    def __repr__(self):
        return f'<Username {self.username}>'

# Modelo Quote Requests
class quote_requests(db.Model):
    quote_id = db.Column(db.Integer, primary_key=True)
    checkboxes = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    def __init__(self, checkboxes, email):
        self.checkboxes = checkboxes
        self.email = email

    def __repr__(self):
        return f'<Quote ID {self.quote_id}>'

# Modelo Services
class services(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(2100), nullable=False)
    service_description = db.Column(db.Text(), nullable=False)
    service_price = db.Column(db.Float(precision=2), nullable=False)
    service_qty = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __init__(self, service_name, service_description, service_price, service_qty):
        self.service_name = service_name
        self.service_description = service_description
        self.service_price = service_price
        self.service_qty = service_qty

    def __repr__(self):
        return f'<Service Name {self.service_name}>'