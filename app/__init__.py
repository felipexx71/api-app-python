from flask import flask
import mysql.connector
import os

def create_app():
    app = Flask(__name__)
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', ''),
    }
    
    try:
        connection = mysql.connector.connect(**db_config)
        connection.close