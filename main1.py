from data import init_feedback_db, init_sentiment_db, init_users_db
from login import run_login
from dashboard import run_dashboard

# --- Initialize all databases when the program starts ---
init_feedback_db()
init_sentiment_db()
init_users_db()

def main_app_loop():
    # 1. Start with Login screen
    user_email = run_login()
    
    # 2. Check if login was successful
    if user_email:
        # 3. Open Dashboard with the user's email
        run_dashboard(user_email)

if __name__ == "__main__":
    main_app_loop()
