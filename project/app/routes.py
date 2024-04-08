import os
from app import app
from flask import request, render_template, jsonify
from werkzeug.utils import secure_filename
import subprocess

RESUME_PROCESSING_SCRIPT = os.path.join(os.path.dirname(__file__), 'resume_processing.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'userResume' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['userResume']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Ensure the userUploads folder exists
        user_uploads_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'userUploads')
        os.makedirs(user_uploads_folder, exist_ok=True)

        # Save the uploaded file with its original filename
        filename = secure_filename(file.filename)
        file_path = os.path.join(user_uploads_folder, filename)
        file.save(file_path)

        process_uploaded_resume(file_path)
        # Return a JSON response indicating success
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})

    # Handle other HTTP methods if needed
    return jsonify({'error': 'Invalid request method'})

def process_uploaded_resume(file_path):
    # Call the resume_processing.py script with the uploaded resume path
    try:
        subprocess.run(['python3', RESUME_PROCESSING_SCRIPT, file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing resume_processing.py: {e}")

@app.route('/results', methods=['GET', 'POST'])
def display_results():
    if request.method == 'POST':
        # Get the JSON data from the POST request
        data = request.get_json()

        # Process the JSON data as needed
        skills_data = data.get('skills', {})
        # You can further process and extract specific information here

        # Render the results page with the processed data
        return render_template('results.html', skills_data=skills_data)

    elif request.method == 'GET':
        # Handle the GET request to display the results page
        # You can perform any necessary actions here before rendering the page
        return render_template('results.html')

    # Handle other HTTP methods if needed
    return jsonify({'error': 'Invalid request method'})