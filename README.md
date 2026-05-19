# 🚗 Sri Lankan Vehicle Maintenance & Predictive Analytics System

An open-source, localized full-stack web application designed for Sri Lankan vehicle owners to seamlessly track expenses, log maintenance activities, visualize cost breakdowns, and receive algorithmic dynamic service reminders.

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-red.svg)](https://flask.palletsprojects.com/)
[![Styling](https://img.shields.io/badge/styling-Tailwind%20CSS-06B6D4.svg)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Core Features

* **🔒 Secure User Authentication:** Full registration, password hashing using `Werkzeug`, and secure session management via `Flask-Login`.
* **🔔 Smart Service Reminders:** Built-in prediction logic that tracks current vehicle mileage against Sri Lankan standard thresholds (e.g., 3,000 km oil change cycles) to display real-time status alerts (`Good`, `Warning`, `Critical`) with dynamic progress bars.
* **🌐 Dual-Language Localization:** Real-time client-side switch between **English** and **Sinhala (සිංහල)** using custom state mapping and cookies.
* **📝 Comprehensive Log Management:** Easily record maintenance actions, current mileage values, custom tasks, costs in LKR, and linked fuel categories.
* **📋 Sri Lankan Registration Validation:** Robust input field parsing powered by advanced Regular Expressions (Regex) matching local license plate conventions (e.g., modern provincial structures like WP CBB-XXXX, vintage styles, and custom groupings).
* **📊 Visual Analytics Dashboard:** Asynchronous dynamic charts utilizing `Chart.js` rendering overall cost trends alongside automated expenditure breakdowns filtered by specific local fuel variants (*92 Octane, 95 Octane, Auto Diesel, Super Diesel*).
* **🛡️ Admin Control Panel:** Secure access monitoring dashboard visualizing full platform user registration datasets.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.11, Flask, Flask-SQLAlchemy (ORM)
* **Database:** SQLite (Default Local Environment), PostgreSQL Ready (Production Compliant)
* **Frontend UI/UX:** HTML5, Tailwind CSS, Vanilla JavaScript, Chart.js Charts Architecture
* **Template Engine:** Jinja2 Templates

---

## 💻 Local Setup & Installation

Follow these steps to configure and boot up the system within your local development workspace:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sl-vehicle-maintenance.git](https://github.com/YOUR_USERNAME/sl-vehicle-maintenance.git)
   cd sl-vehicle-maintenance
