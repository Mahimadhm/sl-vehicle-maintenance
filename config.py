import os
import subprocess
import sys

# Render එකේදී විතරක් psycopg2-binary එක dynamic install කරවනවා
if os.environ.get("DATABASE_URL"):
    try:
        import psycopg2
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psycopg2-binary"])

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")
    
    db_url = os.environ.get("DATABASE_URL", "sqlite:///vehicle_logs.db")
    if db_url and db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False