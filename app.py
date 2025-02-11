from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv('MONGO_URI'))
db = client.formbuilder
forms_collection = db.forms

# Home route (Admin form builder)
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route (User form)
@app.route('/form/<form_id>')
def form(form_id):
    return render_template('form.html', form_id=form_id)

# API: Save a new form
@app.route('/api/forms', methods=['POST'])
def save_form():
    form_data = request.json
    result = forms_collection.insert_one(form_data)
    return jsonify({"status": "success", "form_id": str(result.inserted_id)})

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for forms (replace with DB for persistence)
forms = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_form', methods=['POST'])
def save_form():
    data = request.json
    form_id = data.get("form_id")
    forms[form_id] = data
    return jsonify({"message": "Form saved successfully", "form_id": form_id})

@app.route('/get_forms', methods=['GET'])
def get_forms():
    return jsonify(forms)

if __name__ == '__main__':
    app.run(debug=True)
