from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection
db_url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(db_url)

@app.route('/')
def home():
    return "Hello, Flask + PostgreSQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

