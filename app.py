from flask import Flask, request
import sqlite3

app = Flask(__name__)


def get_user(user_id):
    conn = sqlite3.connect("users.db")

    query = "SELECT * FROM users WHERE id = " + user_id

    result = conn.execute(query).fetchall()

    conn.close()

    return result


@app.route("/users")
def users():
    user_id = request.args.get("id")

    return {
        "users": get_user(user_id)
    }


if __name__ == "__main__":
    app.run(debug=True)