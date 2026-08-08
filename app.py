from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'test_database.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    conn.commit()
    conn.close()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    
    return jsonify({'id': user_id, 'name': name, 'email': email}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)