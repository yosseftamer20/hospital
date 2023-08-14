from flask import Flask, render_template, request, redirect, session
import sqlite3, datetime

app = Flask(__name__)
app.secret_key = '123'


def handle_db(sql):
    conn = sqlite3.connect(r'"C:\Users\yosse\PycharmProjects\pythonProject1\hospital\hospital.db"')
    cursor = conn.cursor()
    cursor.execute(sql)
    if sql.lower().startswith('select'):
        col_names = [i[0] for i in cursor.description]
        result = cursor.fetchall()
        return col_names, result
    else:
        conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def start():

    return