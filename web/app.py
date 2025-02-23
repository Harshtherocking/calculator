from flask import Flask, render_template, request, jsonify
import psycopg2
import redis
import json
from worker import add_task

app = Flask(__name__)

# Database Connection
conn = psycopg2.connect(
    dbname="mydatabase", user="user", password="password", host="db"
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS calculations (
    id SERIAL PRIMARY KEY,
    expression TEXT,
    result FLOAT
)
""")
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data['expression']
    
    try:
        result = eval(expression)  # Simple Python eval (for demonstration)
        cur.execute("INSERT INTO calculations (expression, result) VALUES (%s, %s)", (expression, result))
        conn.commit()
        return jsonify({"expression": expression, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/history')
def history():
    cur.execute("SELECT expression, result FROM calculations ORDER BY id DESC LIMIT 10")
    records = cur.fetchall()
    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
