# CÓDIGO CORREGIDO - app_secure.py
from flask import Flask, request

import sqlite3

app = Flask(__name__)

@app.route('/login')
def login():
    user = request.args.get('user')

    # Consulta parametrizada (previene SQL Injection)

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (user,))
    return str(cursor.fetchall())

if __name__ == '__main__':
    # debug=False en producción (previene exposición de datos internos)

    app.run(host='0.0.0.0', port=5000, debug=False)
