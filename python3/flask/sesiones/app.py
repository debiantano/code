from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        rol = request.form["rol"]
        session["user"] = email
        session["rol"] = rol
        return redirect(url_for('products'))
    
    else:
        return "bad request"
    
    return render_template("login.html")

@app.route("/products")
def products():
    if "user" in session and session["rol"] == "admin":
        return render_template("products.html")
    else:
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(debug=True)
