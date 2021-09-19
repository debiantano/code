from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    name="Kanguro"
    return render_template("index.html", nombre=name)

@app.route('/client')
def client():
    list_name=["test1","test2","test3","list4","list5"]
    return render_template("client.html", list=list_name)


if __name__=="__main__":
    app.run(port=5000, debug=True)
