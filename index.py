import sqlite3
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Patients (
#         id INTEGER PRIMARY KEY autoincrement,
#         name TEXT NOT NULL,
#         age INTEGER,
#         gender TEXT,
#         address TEXT,
#         phone_number TEXT,
#         picture blob
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Doctors (
#         id INTEGER PRIMARY KEY autoincrement,
#         name TEXT NOT NULL,
#         specialization TEXT,
#         phone_number TEXT
#         dob date,
#         email text,
#         picture blob
#
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS nurses (
#         id INTEGER PRIMARY KEY autoincrement,
#         name TEXT NOT NULL,
#         phone_number TEXT,
#          dob date,
#         email text,
#         picture blob
#     )
# ''')
#
# # Table: Appointments
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Appointments (
#         id INTEGER PRIMARY KEY autoincrement,
#         patient_id INTEGER,
#         doctor_id INTEGER,
#         appointment_date DATE,
#         appointment_time TIME,
#         FOREIGN KEY (patient_id) REFERENCES Patients(id),
#         FOREIGN KEY (doctor_id) REFERENCES Doctors(id)
#     )
# ''')
#
# # Table: Medications
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Medications (
#         id INTEGER PRIMARY KEY autoincrement,
#         name TEXT NOT NULL,
#         dosage TEXT,
#         patient_id INTEGER ,
#         FOREIGN KEY (patient_id) REFERENCES Patients(id)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS specialization (
#         id INTEGER PRIMARY KEY autoincrement,
#         name TEXT NOT NULL
#     )
# ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pharmacy (
        id INTEGER PRIMARY KEY autoincrement,
        name TEXT NOT NULL,
        Quantity INTEGER,
        remaining INTEGER,
        expendable INTEGER,
        id_doc integer,
        id_patient integer,
        date DATETIME
    )
''')

conn.commit()
conn.close()