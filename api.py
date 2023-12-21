from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

image_folder_path = r'C:\Users\Menuka\Desktop\9\9'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return jsonify({'status': 'success', 'message': 'Welcome to the home page'})
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        try:
            # Check if the 'file' key is in the request
            if 'file' not in request.files:
                return jsonify({'status': 'error', 'message': 'No file part'})

            file = request.files['file']

            # Check if the file has a name
            if file.filename == '':
                return jsonify({'status': 'error', 'message': 'No selected file'})

            # Check if the file type is allowed
            if not allowed_file(file.filename):
                return jsonify({'status': 'error', 'message': 'Invalid file type'})

            # Generate a unique filename and save the file
            filename = secure_filename(file.filename)
            file.save(os.path.join(image_folder_path, filename))

            # Provide a success message after successfully uploading the file
            return jsonify({'status': 'success', 'message': 'File uploaded successfully'})
            
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    # For GET requests to the '/upload' endpoint
    return jsonify({'status': 'success', 'message': 'This is the upload page. Use a POST request to upload a file.'})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3300)
























