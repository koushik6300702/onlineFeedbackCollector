import sqlite3


def create_table():
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    # Add new columns to an existing database if needed.
    cursor.execute("PRAGMA table_info(feedback)")
    columns = [row[1] for row in cursor.fetchall()]

    if "email" not in columns:
        cursor.execute("ALTER TABLE feedback ADD COLUMN email TEXT")

    if "rating" not in columns:
        cursor.execute("ALTER TABLE feedback ADD COLUMN rating INTEGER")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Database updated successfully!")