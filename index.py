import sqlite3

# Connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('hospital.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the tables

# Table: Patients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Patients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        address TEXT,
        phone_number TEXT
    )
''')

# Table: Doctors
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doctors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        specialization TEXT,
        phone_number TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS nurses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT
    )
''')

# Table: Appointments
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Appointments (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date DATE,
        appointment_time TIME,
        FOREIGN KEY (patient_id) REFERENCES Patients(id),
        FOREIGN KEY (doctor_id) REFERENCES Doctors(id)
    )
''')

# Table: Medications
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Medications (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dosage TEXT,
        patient_id INTEGER,
        FOREIGN KEY (patient_id) REFERENCES Patients(id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()