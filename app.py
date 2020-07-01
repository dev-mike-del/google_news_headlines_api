import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from config import mysql

@app.route('/headlines')
def headlines():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM headlines")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/headlines/<int:headline_id>')
def student(headline_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM headlines WHERE id=%s", headline_id)
        row = cursor.fetchone()
        res = jsonify(row)
        res.status_code = 200
        
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'There is no record: ' + request.url,
            }
    res = jsonify(message)
    res.status_code = 404

    return res
                            
if __name__ == "__main__":
    app.run()
