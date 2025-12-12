import streamlit as st
from data import init_feedback_db, init_sentiment_db
from login import run_login
from dashboard import run_dashboard
from gui import run_gui

# Initialize databases
init_feedback_db()
init_sentiment_db()

def main():
    # Step 1: Run login page
    user = run_login()   # should return user info or True if login success

    if user:  # only continue if login/account creation succeeded
        # Step 2: Run dashboard
        session = run_dashboard(user)  # dashboard returns selected session or True

        if session:
            # Step 3: Run GUI (feedback form)
            run_gui(session)

if __name__ == "__main__":
    main()

