from flask import Flask, jsonify, request
from utils import config
from services import analyzer
from utils import file_handler
from models.candidate import db, Candidate
import json

app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)

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

        try:
            json_data = json.dumps(analysis_results)
            new_record = Candidate(
                name=analysis_results.get('candidate_name'),
                raw_analysis=json_data
            )
            db.session.add(new_record)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"DB Error: {str(e)}"}), 500

        return jsonify({
            'message': f"{file.filename} is analyzed successfully",
            'result': analysis_results
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health_check():
    app_name = app.config.get("APP_NAME")
    return jsonify({
        'message': f"{app_name} API is Running"
    }), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
    app.run(debug=True)