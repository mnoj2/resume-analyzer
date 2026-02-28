##  Resume Analyzer  
A professional Flask-based REST API that automates resume screening. It uses Regular Expressions (Regex) for high-speed pattern matching and SQL Server to store analysis results in a flexible JSON format.

##  How to Run the Project
### 1. Prerequisites
Python 3.8+

SQL Server / LocalDB installed (e.g., (localdb)\MSSQLLocalDB).

ODBC Driver 17 for SQL Server installed on Windows.

### 2. Installation
Install the required libraries for Flask, Database connectivity, and Environment management:

Bash
pip install flask flask-sqlalchemy pyodbc python-dotenv
### 3. Database Setup
Open SQL Server Management Studio (SSMS).

Create a new database named ResumeDB.

The application will automatically create the candidates table on the first run using db.create_all().

### 4. Configuration (utils/config.py)
Ensure your connection string points to your LocalDB instance:

Server Name: (localdb)\\MSSQLLocalDB
Driver: ODBC Driver 17 for SQL Server
##  API Endpoints
### 1. Health Check
URL: /health | Method: GET

Verifies API status and database connectivity.

### 2. Upload & Analyze Resume
URL: /upload_resume | Method: POST

Body: form-data | Key: resume (File)

Action: Reads the .txt file, calculates a match score, and saves the results as a JSON string in the SQL Server database.

##  Sample Request (Postman)
Method: POST

URL: http://127.0.0.1:5000/upload_resume

Body: Select form-data.

Key: resume, change type to File.

Value: Upload your .txt file and click Send.

##  Sample Response (200 OK)
The API returns the analysis results and confirms the database save.


{
  "message": "Analyzed and Saved to SQL Server successfully",
  "result": {
    "candidate_name": "MANOJKUMAR G",
    "word_count": 245,
    "match_score": 85.0,
    "matched_skills": ["Python", "Flask", "SQL", "React.js"],
    "entities": {
      "locations": ["Chennai"]
    },
    "warnings": []
  }
}
## 🗄 Database Storage Pattern
The system uses a Hybrid Storage approach. Instead of dozens of columns, we store the core analysis as a single JSON string in an NVARCHAR(MAX) or TEXT column. This allows:

Flexibility: Add new analysis fields without changing the database schema.

Efficiency: Single-row insertion per candidate.

Querying: SQL Server can still query this data using JSON_VALUE().

## 🛠 Tech Stack
Framework: Flask (Python)

Database: SQL Server (LocalDB)

ORM: SQLAlchemy (Flask-SQLAlchemy)

Parsing: Regex (Regular Expressions)
