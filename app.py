from flask import Flask, render_template, request, redirect, abort,jsonify
import json

app = Flask(__name__)

# Load student data
with open('students.json', 'r') as file:
    students_data = json.load(file)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html exists in the templates folder

@app.route('/get-admit-card-link', methods=['POST'])
def get_admit_card_link():
    # Get data from the request
    data = request.json
    mobile_number = data.get('mobileNumber')
    roll_number = data.get('rollNumber')

    # Validate credentials
    if mobile_number in students_data and roll_number in students_data[mobile_number]:
        admit_card_link = students_data[mobile_number][roll_number]
        return jsonify({"admitCardLink": admit_card_link})
    else:
        return jsonify({"error": "Invalid credentials or Admit Card not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)