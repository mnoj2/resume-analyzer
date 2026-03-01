# Resume Analyzer
A Flask-based API that screens resumes using Regex pattern matching and stores the results in SQL Server using JSON for flexibility.

# Getting Started
## 1. Requirements
Install the necessary Python packages:

pip install flask pyodbc python-dotenv
## 2. Database Setup
Create a database named ResumeDB in SQL Server and run the following command to create the table:

SQL
CREATE TABLE candidates (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100),
    raw_analysis NVARCHAR(MAX),
    created_at DATETIME DEFAULT GETDATE()
);
## 3. Environment Config (.env)
Create a .env file in your root directory:


DB_DRIVER=ODBC Driver 17 for SQL Server

DB_SERVER=(localdb)\MSSQLLocalDB

DB_NAME=ResumeDB

APP_NAME=Resume Analyzer

REQUIRED_SKILLS=Python,Flask,SQL,Java

REQUIRED_LOCATIONS=Chennai,Madurai
# API Endpoints
## Health Check
URL: /health

Method: GET

Purpose: Confirms the API is online.

## Upload Resume
URL: /upload_resume

Method: POST

Body: form-data (Key: resume, Type: File)

Process: Parses the .txt file, calculates the match score, and saves the full analysis dictionary as a JSON string into the database.

# Sample Requests & Responses
### Sample Request (Postman/cURL)
Set method to POST.

Enter URL: http://127.0.0.1:5000/upload_resume.

In Body > form-data, add a key named resume, change type to File, and upload a .txt resume.

### Sample Success Response (200 OK)
{
  "message": "resume.txt is analyzed successfully",
  "result": {
    "candidate_name": "MANOJKUMAR G",
    "entities": {
      "locations": ["Chennai"]
    },
    "match_score": 75.0,
    "matched_skills": ["Python", "SQL", "Java"],
    "warnings": [],
    "word_count": 250
  }
}

# Technical Details
Logic: Uses Regular Expressions (Regex) to find exact word matches for skills and locations.

Storage: Uses raw pyodbc connections to insert data. By storing the result as JSON, you can update your analysis logic without needing to change your SQL table structure.

Security: Uses parameterized queries (? placeholders) to prevent SQL injection.