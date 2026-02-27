from flask import Flask, jsonify, request
from utils import config

app = Flask(__name__)
app.config.from_object(config.Config)

@app.route("/upload_resume", methods=["POST"])
def upload_resume():

    # Key check from Body
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file'}), 400

    # Filename check from files
    file = request.files['resume']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    #Only .txt file allowed
    if not file.filename.lower().endswith('.txt'):
        return jsonify({'error': 'Only .txt files allowed'}), 400

    content = file.read().decode('utf-8')

    return jsonify({'message': f'{file.filename} is read successfully', 'txt_content': content}), 200


@app.route("/health")
def health_check():
    app_name = app.config.get("APP_NAME")
    return f"{app_name} API is Running", 200

if __name__ == "__main__":
    app.run(debug=True)