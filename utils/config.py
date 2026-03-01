import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_CONN_STR = (
        f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"Trusted_Connection=yes;"
    )
    APP_NAME = os.getenv("APP_NAME")
    REQUIRED_SKILLS = os.getenv("REQUIRED_SKILLS").split(",")
    REQUIRED_LOCATIONS = os.getenv("REQUIRED_LOCATIONS").split(",")