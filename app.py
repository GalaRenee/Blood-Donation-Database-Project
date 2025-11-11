from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('blood_bank.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS donors (
        donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        blood_group TEXT,
        phone TEXT,
        city TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS donations (
        donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_id INTEGER,
        date TEXT,
        quantity_ml INTEGER,
        FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS requests (
        request_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        blood_group TEXT,
        quantity_ml INTEGER,
        hospital TEXT,
        date TEXT,
        status TEXT DEFAULT 'Pending'
    )''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('blood_bank.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM donors")
    total_donors = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM requests")
    total_requests = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM donations")
    total_donations = cur.fetchone()[0]
    conn.close()
    return render_template('index.html', donors=total_donors, requests=total_requests, donations=total_donations)

@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['age'],
            request.form['gender'],
            request.form['blood_group'],
            request.form['phone'],
            request.form['city']
        )
        conn = sqlite3.connect('blood_bank.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO donors (name, age, gender, blood_group, phone, city) VALUES (?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_donor.html')

@app.route('/record_donation', methods=['GET', 'POST'])
def record_donation():
    if request.method == 'POST':
        data = (
            request.form['donor_id'],
            request.form['date'],
            request.form['quantity_ml']
        )
        conn = sqlite3.connect('blood_bank.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO donations (donor_id, date, quantity_ml) VALUES (?, ?, ?)', data)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('record_donation.html')

@app.route('/make_request', methods=['GET', 'POST'])
def make_request():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['blood_group'],
            request.form['quantity_ml'],
            request.form['hospital'],
            request.form['date']
        )
        conn = sqlite3.connect('blood_bank.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO requests (name, blood_group, quantity_ml, hospital, date) VALUES (?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('make_request.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        bg = request.form['blood_group']
        conn = sqlite3.connect('blood_bank.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM donors WHERE blood_group = ?', (bg,))
        results = cur.fetchall()
        conn.close()
    return render_template('search.html', results=results)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
