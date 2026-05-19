from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    vehicles = db.relationship("Vehicle", backref="owner", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_no = db.Column(db.String(20), unique=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    fuel_type = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class MaintenanceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))
    service_date = db.Column(db.Date)
    current_mileage = db.Column(db.Integer)
    task_description = db.Column(db.Text)
    fuel_type = db.Column(db.String(50))
    cost_lkr = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)