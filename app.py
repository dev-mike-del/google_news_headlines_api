from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from secret_variables import db_user, db_password, db_host, db_name

app = Flask(__name__)
CORS(app)

uri = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)

headlines1 = db.Table('headlines', 
    db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/headlines')
def headlines():
    try:
        results = db.session.query(headlines1).all()
        json_results = jsonify(results)
        json_results.status_code = 200
        return json_results
    except Exception as e:
        print(e)
    finally:
        db.session.close()

@app.route('/headline/<int:headline_id>')
def headline(headline_id):
    print("You have entered the 'headline' function")
    try:
        results =  db.session.execute(
            headlines1.select().where(headlines1.columns.id == headline_id))
        json_results = jsonify({'result': [dict(row) for row in results]})
        json_results.status_code = 200
        return json_results
    except Exception as e:
        print(e)
        raise e
    finally:
        db.session.close()

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
