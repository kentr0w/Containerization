from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="service",
    user="usr",
    password="password"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user_info (name VARCHAR(255), surname VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        phone = request.json['phone']
        cur.execute("INSERT INTO user_info (name, surname, email, phone) VALUES (%s, %s, %s, %s)", (name, surname, email, phone))
        conn.commit()
        return "Ok", 200
    else:
        cur.execute("SELECT * from user_info")
        result = cur.fetchall()
        return result 
        #return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
