import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.environ.get("APP_NAME")
    REQUIRED_SKILLS = ['Python', 'Flask', 'Pandas', 'SQL']