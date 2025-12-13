import tkinter as tk
from tkinter import messagebox

def run_gui(session):
    root = tk.Tk()
    root.title(f"Feedback - {session['name']}")
    root.geometry("800x650")

    # --- FLOWER THEME ---
    bg_color = "#FFFFFF"   # White
    btn_color = "#FF69B4"  # Hot Pink
    text_color = "#000000" # Black

    root.configure(bg=bg_color)

    # Decorate corners with flowers using Labels
    tk.Label(root, text="🌺", font=("Arial", 30), bg=bg_color, fg="#FF1493").place(x=10, y=10)
    tk.Label(root, text="🌺", font=("Arial", 30), bg=bg_color, fg="#FF1493").place(x=740, y=10)
    tk.Label(root, text="🌷", font=("Arial", 30), bg=bg_color, fg="#FF1493").place(x=10, y=580)
    tk.Label(root, text="🌷", font=("Arial", 30), bg=bg_color, fg="#FF1493").place(x=740, y=580)

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(pady=40)

    # Title
    tk.Label(frame, text=f"Feedback for\n{session['name']}", font=("Arial", 22, "bold"), 
             bg=bg_color, fg="#C71585").grid(row=0, column=0, columnspan=2, pady=20)

    # Labels and Entries
    labels = ["Reviewer Name", "Reviewer ID", "Score (1-10)", "Comment"]
    entries = {}

    for i, label_text in enumerate(labels):
        tk.Label(frame, text=label_text + ":", font=("Arial", 12, "bold"), 
                 bg=bg_color, fg=text_color).grid(row=i+1, column=0, padx=10, pady=10, sticky="e")
        
        entry = tk.Entry(frame, width=30, font=("Arial", 11), bg="#FFF0F5") # Light pink input
        entry.grid(row=i+1, column=1, padx=10, pady=10)
        entries[label_text] = entry

    def submit_feedback():
        reviewer_name = entries["Reviewer Name"].get()
        reviewer_ID = entries["Reviewer ID"].get()
        score = entries["Score (1-10)"].get()
        comment = entries["Comment"].get()

        if not reviewer_name or not reviewer_ID or not score or not comment:
            messagebox.showerror('Error', '🌸 Please fill in all fields! 🌸')
            return

        try:
            score_int = int(score)
        except ValueError:
            messagebox.showerror('Error', 'Score must be a number')
            return

        # Import inside function to avoid circular import
        from data import insert_feedback, insert_sentiment
        from analysis import analyze_sentiment

        # --- FIX: Passing all 6 arguments now ---
        insert_feedback(reviewer_name, reviewer_ID, session['name'], session['id'], score_int, comment)
        
        # Analyze Sentiment
        sentiment_score = analyze_sentiment(comment)
        insert_sentiment(session['name'], session['id'], sentiment_score)

        messagebox.showinfo('Success', 'Feedback submitted! 🌷')
        root.destroy() # Close window

    # Pink Submit Button
    tk.Button(frame, text="Submit Feedback 🌸", bg=btn_color, fg="white", 
              font=("Arial", 14, "bold"), command=submit_feedback).grid(row=6, column=0, columnspan=2, pady=30)

    root.mainloop()
