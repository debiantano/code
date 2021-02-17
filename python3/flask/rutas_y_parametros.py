from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return "GAAAAA"

@app.route('/params')
def params():
    param1=request.args.get('param1','No contiene un parametro')
    param2=request.args.get('param2','No contiene un parametro')
    return "los parametros son: {} y {}".format(param1,param2)



if __name__=="__main__":
    app.run(port=5000, debug=True)
