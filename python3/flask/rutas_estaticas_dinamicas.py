from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/hola")
def hola():
    return "Hola"

@app.route("/user/<string:user>")
def user(user):
    return "hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID {}, Nombre de Usuario: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "El resultado es: {}".format(n1+n2)

# VALORES POR DEFECTO
@app.route("/default/")
@app.route("/default/<string:dft>")
def  dft(dft="defecto"):
    return "El valor de dft es: {}".format(dft)


if __name__=="__main__":
    app.run(debug=True)
