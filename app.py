from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("feedback.db")
    conn.row_factory = None
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/feedback", methods=["POST"])
def feedback():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    rating = request.form.get("rating", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not rating or not message:
        return "Please fill in all fields.", 400

    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            return "Rating must be between 1 and 5.", 400
    except ValueError:
        return "Please select a valid rating.", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback (name, message, email, rating)
        VALUES (?, ?, ?, ?)
        """,
        (name, message, email, rating)
    )

    conn.commit()
    conn.close()

    return render_template(
        "success.html",
        name=name,
        message=message
    )


@app.route("/admin")
def admin():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, message, email, rating FROM feedback ORDER BY id DESC"
    )
    feedbacks = cursor.fetchall()

    conn.close()

    return render_template("admin.html", feedbacks=feedbacks)


@app.route("/delete/<int:feedback_id>", methods=["POST"])
def delete_feedback(feedback_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM feedback WHERE id = ?",
        (feedback_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)