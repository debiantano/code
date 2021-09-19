from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', message="hello Flask", contacts=['c1','c2','c3','c4','c5'])

if __name__=="__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
