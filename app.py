from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import db_config  # Our configuration file with connection details

app = Flask(__name__)

# Configure MongoDB connection
app.config["MONGO_URI"] = db_config.MONGO_URI
mongo = PyMongo(app)

# Access the specified database and collection
db = mongo.cx[db_config.DB_NAME]
collection = db[db_config.COLLECTION_NAME]

@app.route('/')
def index():
    """Display all employees."""
    employees = list(collection.find())
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    """Add a new employee."""
    if request.method == 'POST':
        name = request.form['name'].strip()
        department = request.form['department'].strip()
        email = request.form['email'].strip()

        if name and department and email:
            collection.insert_one({
                "name": name,
                "department": department,
                "email": email
            })
        return redirect(url_for('index'))
    return render_template('add_employee.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_employee(id):
    """Edit an existing employee."""
    employee = collection.find_one({"_id": ObjectId(id)})
    if not employee:
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name'].strip()
        department = request.form['department'].strip()
        email = request.form['email'].strip()

        collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": name,
                "department": department,
                "email": email
            }}
        )
        return redirect(url_for('index'))

    return render_template('edit_employee.html', employee=employee)

@app.route('/delete/<id>', methods=['POST'])
def delete_employee(id):
    """Delete an employee by ID."""
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
