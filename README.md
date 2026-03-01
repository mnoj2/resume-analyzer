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

# Technical Details
Logic: Uses Regular Expressions (Regex) to find exact word matches for skills and locations.

Storage: Uses raw pyodbc connections to insert data. By storing the result as JSON, you can update your analysis logic without needing to change your SQL table structure.

Security: Uses parameterized queries (? placeholders) to prevent SQL injection.