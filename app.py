from flask import Flask, jsonify
#flask is a python package= alibrary someone wrote that helps you build web severs easily
#Flask is a thing inside that package that lets you create an app/server
#jsonify is the translator that converts Python data into JSON


app = Flask(__name__)

@app.route("/users", methods=["GET"])# this is called a decorator. It attaches the fuction below to a URL
def get_users():
    return jsonify([]), 200

if __name__ == "__main__":
    app.run(debug=True)
