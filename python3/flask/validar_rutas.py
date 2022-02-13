from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return "hola123"
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name='valor por default', num="nada"):
    return "El parametro es: {} y {}".format(name,num)



if __name__=="__main__":
    app.run(port=5000, debug=True)
