import tkinter as tk
from tkinter import messagebox

# The run_gui function MUST accept the 'session' dictionary
def run_gui(parent_root,session):
    root = tk.Toplevel(parent_root)
    root.title(f"Feedback Form for {session['name']}")
    root.geometry("800x600")

    # --- BABY PINK & COZY THEME ---
    bg_color = "#FFF0F5"   # Lavender Blush (Very light baby pink)
    btn_color = "#FFC0CB"  # Pink (Lighter baby pink for buttons)
    text_color = "#4B0082" # Indigo/Dark Purple (Cozy contrast)
    highlight_color = "#E0BBE4" # Lilac/Muted Pink for borders

    root.configure(bg=bg_color)

    # Frame for content
    frame = tk.Frame(root, bg=bg_color, bd=2, relief="groove")
    frame.pack(padx=40, pady=40, fill='both', expand=True)

    # Title with Cozy separator
    tk.Label(frame, text=f"✨ Session Feedback ✨", font=("Arial", 20, "bold"), 
             bg=bg_color, fg=text_color).grid(row=0, column=0, columnspan=2, pady=(10, 5))
    tk.Label(frame, text="— Submit your valuable thoughts —", font=("Arial", 10), 
             bg=bg_color, fg=text_color).grid(row=1, column=0, columnspan=2, pady=(0, 20))

    # Entries setup
    labels = ["Reviewer Name", "Reviewer ID", "Score (1-10)", "Comment"]
    entries = {}

    for i, label_text in enumerate(labels):
        tk.Label(frame, text=label_text + ":", font=("Arial", 12, "bold"), 
                 bg=bg_color, fg=text_color).grid(row=i+2, column=0, padx=10, pady=10, sticky="e")
        
        # Use a slightly darker background for input fields
        entry = tk.Entry(frame, width=30, font=("Arial", 11), bg="#FFFFFF", bd=1, relief="solid")
        entry.grid(row=i+2, column=1, padx=10, pady=10, sticky="w")
        entries[label_text] = entry

    # For comment field, use a Text widget for better input area
    tk.Label(frame, text="Comment:", font=("Arial", 12, "bold"), 
             bg=bg_color, fg=text_color).grid(row=5, column=0, padx=10, pady=10, sticky="e")
    comment_text_widget = tk.Text(frame, width=30, height=5, font=("Arial", 11), bg="#FFFFFF", bd=1, relief="solid")
    comment_text_widget.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    
    def submit_feedback():
        # Get data from entry widgets
        reviewer_name = entries["Reviewer Name"].get()
        reviewer_ID = entries["Reviewer ID"].get()
        score = entries["Score (1-10)"].get()
        comment = comment_text_widget.get("1.0", tk.END).strip() # Get text from Text widget
        
        if not reviewer_name or not reviewer_ID or not score or not comment:
            messagebox.showerror('Error', 'Please fill in all fields.')
            return

        try:
            score_int = int(score)
            if not (1 <= score_int <= 10):
                raise ValueError
        except ValueError:
            messagebox.showerror('Error', 'Score must be a whole number between 1 and 10.')
            return

        # Import inside function to avoid circular import issues
        from data import insert_feedback, insert_sentiment
        from analysis import analyze_sentiment
        
        # --- CRITICAL FIX ---
        # Passing all 4 arguments, including session details, to the database function
        insert_feedback(reviewer_name, reviewer_ID, score_int, comment)
        
        # Analyze Sentiment
        sentiment_score = analyze_sentiment(comment)
        insert_sentiment(session['name'], session['id'], sentiment_score)

        messagebox.showinfo('Success', 'Feedback submitted successfully! Thank you. 💖')
        root.destroy() 

    # Submit Button with the baby pink color
    tk.Button(frame, text="Submit Feedback", bg=btn_color, fg=text_color, 
              activebackground=highlight_color, activeforeground=text_color,
              font=("Arial", 14, "bold"), command=submit_feedback).grid(row=6, column=0, columnspan=2, pady=30, ipadx=10)

   #root.mainloop()
   root.transient(parent_root)
   root.grab_set()
   parent_root.wait_window(root)

    

# Note: The imported run_gui in main1.py calls this function
