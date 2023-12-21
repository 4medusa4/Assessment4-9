from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define the path to the image folder
image_folder_path = r'C:\Users\Menuka\Desktop\9\9'

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Check if the 'file' key is in the request
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file part'})

        file = request.files['file']

        # Check if the file has a name
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'})

        # Save the file to the specified folder
        file.save(os.path.join(image_folder_path, file.filename))

        return jsonify({'status': 'success', 'message': 'File uploaded successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3300)
