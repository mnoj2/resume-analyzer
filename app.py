from flask import Flask, jsonify, request
from utils.config import Config
from services import analyzer
from utils import file_handler
import pyodbc, json

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    return pyodbc.connect(app.config['DB_CONN_STR'])

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    try:
        file = request.files.get("resume")
        content, error, status = file_handler.validate_and_read_file(file)
        if error:
            return jsonify({"error": error}), status

        req_skills = app.config.get("REQUIRED_SKILLS")
        req_locations = app.config.get("REQUIRED_LOCATIONS")
        analysis_results = analyzer.analyze_resume(content, req_skills, req_locations)

        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO candidates (name, raw_analysis) VALUES (?, ?)"
            cursor.execute(query, (analysis_results.get('candidate_name'), json.dumps(analysis_results)))
            conn.commit()
        except Exception as db_err:
            return jsonify({"error": f"Database Failure: {str(db_err)}"}), 500
        finally:
            if conn:
                conn.close()

        return jsonify({
            'message': f"{file.filename} is analyzed successfully",
            'result': analysis_results
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health_check():
    return jsonify({'message': f"{app.config.get('APP_NAME')} API is Running"}), 200

if __name__ == "__main__":
    app.run(debug=True)