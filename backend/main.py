from flask import Flask, render_template, request
import psycopg2
import json

app = Flask(__name__)

conn = psycopg2.connect(
    host="postgresql",
    database="flask_db",
    user="qweqwe",
    password="test"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user_info (name VARCHAR(255), company VARCHAR(255), jobtitle VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))")

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Im here")
    if request.method == 'POST':
        name = request.json['name']
        company = request.json['company']
        jobtitle = request.json['jobtitle']
        email = request.json['email']
        phone = request.json['phone']
        cur.execute("INSERT INTO user_info (name, company, jobtitle, email, phone) VALUES (%s, %s, %s, %s)", (name, company, jobtitle, email, phone))
        conn.commit()
        return "Ok", 200
    else:
        print("Im here")
        cur.execute("SELECT * from user_info")
        result = cur.fetchall()
        return json.dumps(result)
        #return render_template('form.html')