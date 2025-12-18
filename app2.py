# POST requests and JSON
'''THE CLIENT WILL SEND DATA
THE SERVER WILL PROCESS AND STORE IT'''


from flask import Flask, jsonify, request
#request  is a thing inside the flask package that gives access to the incoming request, lets you read json, headers,etc


app = Flask(__name__)

users = []#this is a server side storage. which only exists while the server runs

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify(error="Name is required"), 400

    user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(user)

    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)
