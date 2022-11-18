from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL CONNECTION
app.config['MYSQL_USER'] = 'noroot'
app.config['MYSQL_PASSWORD'] = 'noroot'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'flaskcrud'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# SETTINGS
app.secret_key = "my_secret_key"

@app.route("/")
def index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM contacts")
	data = cur.fetchall()
	print(data)
	return render_template("index.html", contacts = data)

@app.route("/add_contact", methods=["POST"])
def add_contact():
	if request.method == "POST":
		fullname = request.form["fullname"]
		phone = request.form["phone"]
		email = request.form["email"]
		print(email, phone, fullname)
	
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
	
		mysql.connection.commit()
		flash("Contact Added Successfully")
	return redirect(url_for('index'))

@app.route("/delete/<string:id>")
def delete_contact(id):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM contacts WHERE id = {0}".format(id))
	mysql.connection.commit()
	flash("Contact Removed Successfully")
	return redirect(url_for("index"))

@app.route("/edit/<id>")
def get_contact(id):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM contacts WHERE id = %s", (id))
	data = cur.fetchall()
	return render_template("edit-contact.html", contact = data[0])

@app.route("/update/<id>", methods=["POST"])
def update_contact(id):
	if request.method == "POST":
		fullname = request.form["fullname"]
		phone = request.form["phone"]
		email = request.form["email"]

	cur = mysql.connection.cursor()
	cur.execute("""
		UPDATE contacts
		SET fullname = %s,
		email = %s,
		phone = %s
	WHERE id = %s
	""", (fullname, email, phone, id))
	mysql.connection.commit()

	flash("Contact Updated Successfully")
	return redirect(url_for("index"))



if __name__ == "__main__":
	app.run(port=3000, debug=True)
