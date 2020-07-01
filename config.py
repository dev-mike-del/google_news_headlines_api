from app import app
from flaskext.mysql import MySQL

from secret_variables import db_user, db_password, db_host, db_name
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host
mysql.init_app(app)
