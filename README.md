Online Feedback Collector

Project Description

Online Feedback Collector is a web application that allows users to submit feedback through a web form. The administrator can view, search, and delete feedback records using the admin dashboard.

Objectives

- Collect feedback online.
- Store feedback in an SQLite database.
- Display submitted feedback in an admin dashboard.
- Allow administrators to search and delete feedback records.

Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript (if used)

Features

1. Feedback submission form.
2. Name, email, rating, and message fields.
3. Success page after submission.
4. SQLite database storage.
5. Admin dashboard.
6. Search feedback by name or email.
7. Delete feedback records.

Project Structure

- "app.py" — Flask application and routes.
- "database.py" — Database table setup.
- "feedback.db" — SQLite database file, if included.
- "templates/" — HTML templates.
- "static/" — CSS and JavaScript files.

How to Run

1. Install Python.

2. Open a terminal in the project folder.

3. Install Flask:
   
   "pip install flask"

4. Initialize or update the database if required by the project.

5. Start the application:
   
   "python app.py"

6. Open "http://127.0.0.1:5000/" in your browser.

7. Open "http://127.0.0.1:5000/admin" to view the admin dashboard.

Testing

The feedback submission, database display, search, and delete features were tested.

Conclusion

The project provides a simple way to collect and manage feedback using a Python Flask web application and an SQLite database.