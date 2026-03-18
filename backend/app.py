from flask import Flask, render_template, request, redirect, session
import mysql.connector
import time

app = Flask(__name__)
app.secret_key = "secret123"

def get_db_connection():
    for i in range(5):
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="testdb"
            )
            return conn
        except:
            time.sleep(2)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            session['user'] = username
            return redirect('/')
    
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect('/login')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        return redirect('/')

    cursor.execute("SELECT name, email FROM users")
    users = cursor.fetchall()
    conn.close()

    return render_template('index.html', users=users)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)