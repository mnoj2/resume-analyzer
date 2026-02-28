import os
from urllib.parse import quote_plus


class Config:
    driver = "ODBC Driver 17 for SQL Server"
    server = "(localdb)\\MSSQLLocalDB"
    database = "ResumeDB"

    params = quote_plus(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_NAME = "Resume Analyzer"
    REQUIRED_SKILLS = ['Python', 'Flask', 'Pandas', 'SQL', 'Java']
    REQUIRED_LOCATIONS = ['Madurai', 'Chennai', 'Virudhunagar']