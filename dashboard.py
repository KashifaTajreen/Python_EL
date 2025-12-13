import tkinter as tk
from gui import run_gui 
from analysis_view import run_analysis_view # Import the new analysis view

# Define the function to transition from Dashboard to Feedback Form
def open_feedback_form(root, session):
    root.withdraw()  # Close dashboard window
    run_gui(root,session) # Open the feedback form
    root.deiconify()
   
def run_dashboard(user_email):
    root = tk.Tk()
    root.title("Session Dashboard")
    root.geometry("800x600")
    
    # --- NEW COLOR PALETTE (CONSISTENT VARIABLE NAMES) ---
    BG_COLOR = "#F5F5F5"      # Main Background (Light Grey)
    BTN_COLOR = "#FFD700"     # Primary Accent (Warm Gold)
    TEXT_COLOR = "#191970"    # Dark Text/Headings (Navy Blue)
    CARD_BG = "#FFFFFF"       # Input Field/Card Background (Pure White)
    SECONDARY_COLOR = "#E0E0E0" # Secondary Button/Highlight (Slightly darker grey)

    root.configure(bg=BG_COLOR)

    sessions = [
        {"name": "AI Ethics 🤖", "date": "2025-11-20", "id": "S001"},
        {"name": "Urban Innovation 🏙️", "date": "2025-11-22", "id": "S002"},
        {"name": "Python Workshop 🐍", "date": "2025-11-24", "id": "S003"},
    ]

    tk.Label(root, text=f"Hello, {user_email}!", font=("Arial", 16), 
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(20, 5))

    tk.Label(root, text="Select a Session to Review 🌟", font=("Arial", 22, "bold"), 
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    tk.Label(root, text="— Tap a session card to begin —", font=("Arial", 10), 
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(0, 20))


    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=10)

    for i, session in enumerate(sessions):
        # Card uses CARD_BG (White)
        card = tk.Frame(frame, bg=CARD_BG, bd=1, relief="solid") 
        card.grid(row=i // 2, column=i % 2, padx=30, pady=20, ipadx=15, ipady=15)

        # Labels use CARD_BG (White) and TEXT_COLOR (Navy)
        tk.Label(card, text=session['name'], font=("Arial", 14, "bold"), 
                 bg=CARD_BG, fg=TEXT_COLOR).pack(pady=(5, 2))
        
        tk.Label(card, text=session['date'], font=("Arial", 10), 
                 bg=CARD_BG, fg="#555555").pack(pady=5) # Use a neutral grey for subtext

        # BUTTON 1: GIVE FEEDBACK (Primary Gold button)
        tk.Button(card, text="Give Feedback 📝", bg=BTN_COLOR, fg=TEXT_COLOR, 
                  activebackground=BTN_COLOR, activeforeground=TEXT_COLOR,
                  font=("Arial", 11, "bold"),
                  command=lambda s=session: open_feedback_form(root, s)).pack(pady=(10, 5))

        # BUTTON 2: VIEW ANALYSIS (Secondary Grey button)
        tk.Button(card, text="View Analysis 📈", bg=SECONDARY_COLOR, fg=TEXT_COLOR, 
                  activebackground=BTN_COLOR, activeforeground=TEXT_COLOR,
                  font=("Arial", 11, "bold"),
                  command=lambda s=session: run_analysis_view(root, s)).pack(pady=(5, 10))

    root.mainloop()
    return True
