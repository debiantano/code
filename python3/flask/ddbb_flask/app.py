from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'noroot'
app.config['MYSQL_PASSWORD'] = 'noroot'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		details = request.form
		firstName = details['fname']
		lastName = details['lname']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO MyUsers(firstname, lastname) VALUES (%s, %s)", (firstName, lastName))
		mysql.connection.commit()
		cur.close()
		return 'success'
	return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
