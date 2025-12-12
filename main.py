import streamlit as st
import bcrypt
import json
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Feedback Analyser", layout="centered")

# --- USER DATA MANAGEMENT (Replacing your sqlite3/json logic) ---
DB_FILE = 'users.json'

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, 'w') as f:
        json.dump(users, f)

# --- SESSION STATE INITIALIZATION ---
# This keeps track of the user across reruns
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""

# --- LOGIN FUNCTION ---
def login_page():
    st.title("🔐 Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        users = load_users()
        
        if username in users:
            # Check password (assuming you stored it as a hash)
            # If you stored plain text, just use: if users[username] == password:
            stored_hash = users[username].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success("Login successful!")
                st.rerun() # Reload to show the dashboard
            else:
                st.error("Incorrect password")
        else:
            st.error("User not found")

# --- SIGN UP FUNCTION ---
def signup_page():
    st.title("📝 Create New Account")
    
    new_user = st.text_input("Choose a Username")
    new_pass = st.text_input("Choose a Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        users = load_users()
        
        if new_user in users:
            st.warning("Username already exists!")
        elif new_pass != confirm_pass:
            st.warning("Passwords do not match!")
        else:
            # Hash the password before saving
            hashed_pw = bcrypt.hashpw(new_pass.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            users[new_user] = hashed_pw
            save_users(users)
            st.success("Account created! Please go to Login.")

# --- MAIN DASHBOARD (Your Analysis Tool) ---
def main_dashboard():
    st.sidebar.title(f"Welcome, {st.session_state['username']}")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
        
    st.title("📊 Feedback Analyser Dashboard")
    st.write("This is where your sentiment analysis graphs will go.")
    
    # Example input for analysis
    user_text = st.text_area("Enter customer feedback:")
    if st.button("Analyze"):
        from textblob import TextBlob
        blob = TextBlob(user_text)
        sentiment = blob.sentiment.polarity
        st.info(f"Sentiment Score: {sentiment}")
        if sentiment > 0:
            st.success("Positive Feedback! 😊")
        elif sentiment < 0:
            st.error("Negative Feedback 😠")
        else:
            st.warning("Neutral Feedback 😐")

# --- APP FLOW CONTROL ---
if st.session_state['logged_in']:
    main_dashboard()
else:
    # Sidebar to switch between Login and Sign Up
    choice = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])
    
    if choice == "Login":
        login_page()
    else:
        signup_page()
