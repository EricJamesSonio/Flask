from main import app  # This imports your Flask app from main.py
from extension import db
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("📦 Tables in the database:")
    for table in tables:
        print(f" - {table}")
