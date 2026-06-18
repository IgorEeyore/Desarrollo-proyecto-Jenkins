# CÓDIGO VULNERABLE
from flask import Flask, request

import sqlite3

app = Flask(__name__)

@app.route('/login')
def login():
    user = request.args.get('user')

    # VULNERABILIDAD SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user}'"
    cursor.execute(query)
    return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)