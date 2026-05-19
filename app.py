from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Vehicle, MaintenanceLog
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"]
        )
        user.set_password(request.form["password"])

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()

        if user and user.check_password(request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard"))

        flash("Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()
    logs = MaintenanceLog.query.all()

    total_cost = sum(log.cost_lkr for log in logs)

    return render_template(
        "dashboard.html",
        vehicles=vehicles,
        logs=logs,
        total_cost=total_cost
    )

@app.route("/add-vehicle", methods=["POST"])
@login_required
def add_vehicle():
    vehicle = Vehicle(
        vehicle_no=request.form["vehicle_no"],
        brand=request.form["brand"],
        model=request.form["model"],
        fuel_type=request.form["fuel_type"],
        user_id=current_user.id
    )

    db.session.add(vehicle)
    db.session.commit()

    return redirect(url_for("dashboard"))

@app.route("/add-log", methods=["POST"])
@login_required
def add_log():
    log = MaintenanceLog(
        vehicle_id=request.form["vehicle_id"],
        service_date=datetime.strptime(
            request.form["service_date"],
            "%Y-%m-%d"
        ),
        current_mileage=request.form["current_mileage"],
        task_description=request.form["task_description"],
        fuel_type=request.form["fuel_type"],
        cost_lkr=request.form["cost_lkr"]
    )

    db.session.add(log)
    db.session.commit()

    return redirect(url_for("dashboard"))

@app.route("/api/logs")
def api_logs():
    logs = MaintenanceLog.query.all()

    return {
        "logs": [
            {
                "id": log.id,
                "cost_lkr": log.cost_lkr,
                "fuel_type": log.fuel_type
            }
            for log in logs
        ]
    }

@app.route("/admin")
@login_required
def admin():
    if not current_user.is_admin:
        return "Unauthorized"

    users = User.query.all()

    return render_template("admin.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)