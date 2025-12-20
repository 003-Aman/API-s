# Flask = web server
# jsonify = converts Python data to JSON
# request = reads data sent by the client
from flask import Flask, jsonify, request

# sqlite3 = Python's built-in database library
import sqlite3


# Create the Flask application (your server)
app = Flask(__name__)


# -----------------------------
# DATABASE CONNECTION FUNCTION
# -----------------------------
def get_db_connection():
    # Connect to the database file
    # If the file doesn't exist, SQLite creates it
    conn = sqlite3.connect("database.db")

    # This allows us to access rows like dictionaries
    # instead of tuples (much easier to work with)
    conn.row_factory = sqlite3.Row

    # Return the connection so Flask can use it
    return conn


# -----------------------------
# GET ALL USERS
# -----------------------------
@app.route("/users", methods=["GET"])
def get_users():
    # Open a connection to the database
    conn = get_db_connection()

    # SQL command:
    # "Give me all rows from the users table"
    users = conn.execute("SELECT * FROM users").fetchall()

    # Always close the database connection
    conn.close()

    # Convert database rows to dictionaries
    # Then return them as JSON
    return jsonify([dict(user) for user in users]), 200


# -----------------------------
# CREATE A NEW USER
# -----------------------------
@app.route("/users", methods=["POST"])
def create_user():

    # Read JSON data from the client
    data = request.get_json()

    # Validate input
    if not data or "name" not in data:
        return jsonify(error="Name is required"), 400

    # Open database connection
    conn = get_db_connection()

    # SQL command to insert a new user
    # ? is a placeholder to prevent SQL injection
    conn.execute(
        "INSERT INTO users (name) VALUES (?)",
        (data["name"],)
    )

    # Save changes to the database
    conn.commit()

    # Close database connection
    conn.close()

    # Respond with success
    return jsonify(message="User created"), 201


# -----------------------------
# START THE SERVER
# -----------------------------
if __name__ == "__main__":
    # Run Flask in debug mode
    app.run(debug=True)
