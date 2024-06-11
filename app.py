from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crime_monitoring.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        description = request.form['description']
        vehicle_registration = request.form['vehicle_registration']
        location = request.form['location']
        gender = request.form['gender']
        crime_type = request.form['crime_type']
        most_wanted = request.form['most_wanted']
        
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        status = 'Reported'
        
        conn = get_db_connection()
        conn.execute('''
        INSERT INTO incidents (date, time, description, vehicle_registration, location, status, gender, crime_type, most_wanted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, time, description, vehicle_registration, location, status, gender, crime_type, most_wanted))
        conn.commit()
        conn.close()
        
        success_message = "Incident reported successfully!"
        return render_template('report.html', success_message=success_message)
    
    return render_template('report.html')

@app.route('/view')
def view():
    conn = get_db_connection()
    incidents = conn.execute('SELECT * FROM incidents').fetchall()
    conn.close()
    return render_template('view.html', incidents=incidents)

@app.route('/track', methods=['GET', 'POST'])
def track():
    if request.method == 'POST':
        vehicle_registration = request.form['vehicle_registration']
        conn = get_db_connection()
        incidents = conn.execute('SELECT * FROM incidents WHERE vehicle_registration = ?', (vehicle_registration,)).fetchall()
        conn.close()
        return render_template('track.html', incidents=incidents, vehicle_registration=vehicle_registration)
    
    return render_template('track.html', incidents=None)

if __name__ == '__main__':
    app.run(debug=True)
