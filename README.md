# Employee Data Handler

A simple **Flask** + **MongoDB** web application to manage employee records.  
It supports full CRUD operations (Create, Read, Update, Delete) with a Tailwind CSS-powered interface.

## 🚀 Features
- View all employees in a clean table layout.
- Add new employees with name, department, and email.
- Edit existing employee records.
- Delete employees with confirmation prompts.
- Responsive UI using **Tailwind CSS**.

## 🛠 Tech Stack
- **Backend:** Python 3, Flask, Flask-PyMongo
- **Database:** MongoDB
- **Frontend:** HTML, Tailwind CSS, Jinja2 Templates
- **Other:** PyMongo, bson

## 📂 Project Structure
Employee-Data-Handler/
│
├── app.py # Main Flask application
├── db_config.py # MongoDB connection details
├── templates/ # HTML templates
│ ├── index.html # Employee list page
│ ├── add_employee.html # Add new employee form
│ └── edit_employee.html # Edit employee form
├── static/ # (Optional) CSS/JS files
├── requirements.txt # Python dependencies
└── README.md
