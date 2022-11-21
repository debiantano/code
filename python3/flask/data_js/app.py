from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    user = {'firstname': "Mr.", 'lastname': "My Father's Son"}
    return render_template("index.html", user=user)

if __name__ == "__main__":
	app.run(port=3000, debug=True)
