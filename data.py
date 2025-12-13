import sqlite3
import bcrypt
import tkinter as tk

def init_feedback_db():
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        reviewer_name TEXT,
        reviewer_ID TEXT,
        score INTEGER,
        comment TEXT
    )
    """)
    conn.commit()
    conn.close()

def init_sentiment_db():
    conn = sqlite3.connect("sentiment.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        session_name TEXT,
        session_ID TEXT,
        overall_sentiment REAL
    )
    """)
    conn.commit()
    conn.close()

def init_users_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        passwords TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_new_user(email,password):
    conn = sqlite3.connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users (email,password) VALUES (?,?)
    """,(email,password))

def email_exists(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def create_account(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_pw.decode('utf-8')))
    conn.commit()
    conn.close()

def validate_login(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash = result[0]
        if bcrypt.checkpw(password.encode('utf-8'),stored_hash.encode('utf-8')):
            return True
        return False
       # return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
    #return False

def insert_feedback(reviewer_name, reviewer_ID, session_name, session_ID, score, comment):
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO feedback (reviewer_name, reviewer_ID, session_name, session_ID, score, comment)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (reviewer_name, reviewer_ID, session_name, session_ID, score, comment))
    conn.commit()
    conn.close()

def insert_sentiment(session_name, session_ID, overall_sentiment):
    conn = sqlite3.connect("sentiment.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO feedback (session_name, session_ID, overall_sentiment)
    VALUES (?, ?, ?)
    """, (session_name, session_ID, overall_sentiment))
    conn.commit()
    conn.close()

def get_comments_for_session(session_ID):
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute("SELECT comment FROM feedback WHERE session_ID = ?", (session_ID,))
    comments = [row[0] for row in cursor.fetchall()]
    conn.close()
    return comments


def run_gui(session):
    window = tk.Tk()
    window.title(f"Feedback Form - {session['name']}")
    window.geometry("600x400")

    tk.Label(window, text=f"Feedback for {session['name']}",
             font=("Arial", 18, "bold")).pack(pady=20)

    # Add your feedback form fields here...
    tk.Entry(window, width=40).pack(pady=10)
    tk.Text(window, width=40, height=5).pack(pady=10)

    tk.Button(window, text="Submit", command=lambda: print("Feedback submitted")).pack(pady=20)

    window.mainloop()
 


