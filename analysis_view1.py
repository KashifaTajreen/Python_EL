'''import tkinter as tk
from data import get_session_summary, get_comments_for_session
from tkinter import ttk # Used for scrollbar

def run_analysis_view(parent_root, session):
    
    # --- BABY PINK & COZY THEME ---
    bg_color = "#FFF0F5"
    text_color = "#4B0082"
    
    window = tk.Toplevel(parent_root)
    window.title(f"Analysis for: {session['name']}")
    window.geometry("750x650")
    window.configure(bg=bg_color)

    summary = get_session_summary(session['id'])
    comments_data = get_comments_for_session(session['id'])
    
    # --- Top Summary Section ---
    summary_frame = tk.Frame(window, bg=bg_color, padx=20, pady=10)
    summary_frame.pack(fill='x')
    
    tk.Label(summary_frame, text=f"📊 Results for {session['name']} 📊", 
             font=("Arial", 20, "bold"), bg=bg_color, fg=text_color).pack(pady=10)

    # Calculate readable scores
    avg_score_val = f"{summary['avg_score']:.1f}" if summary['avg_score'] else "N/A"
    avg_sentiment_val = f"{summary['avg_sentiment']:.2f}" if summary['avg_sentiment'] else "N/A"
    
    tk.Label(summary_frame, text=f"Avg Score: {avg_score_val} / 10", 
             font=("Arial", 16), bg=bg_color, fg=text_color).pack(pady=5)
    
    tk.Label(summary_frame, text=f"Total Reviews: {len(comments_data)}", 
             font=("Arial", 14), bg=bg_color, fg=text_color).pack(pady=5)

    # --- Comments Section (Scrollable) ---
    tk.Label(window, text="— Individual Comments —", font=("Arial", 14, "underline"), 
             bg=bg_color, fg=text_color).pack(pady=(20, 10))

    # Setup for Scrollable Frame
    canvas = tk.Canvas(window, bg=bg_color)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=bg_color)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=20)
    scrollbar.pack(side="right", fill="y")
    
    if not comments_data:
        tk.Label(scrollable_frame, text="No feedback submitted yet.", 
                 font=("Arial", 12), bg=bg_color, fg=text_color).pack(pady=50)
    else:
        for score, comment in comments_data:
            # Comment Card
            card = tk.Frame(scrollable_frame, bg="#FFFFFF", bd=1, relief="solid") # White background for card
            card.pack(fill='x', padx=10, pady=5)
            
            # Score Label (left)
            tk.Label(card, text=f"Score: {score}/10", font=("Arial", 11, "bold"), 
                     bg="#FFFFFF", fg=text_color).pack(anchor='w', padx=10, pady=(5, 2))
            
            # Comment Text (below score)
            tk.Label(card, text=comment, font=("Arial", 10), wraplength=700, justify=tk.LEFT,
                     bg="#FFFFFF", fg="#333333").pack(anchor='w', padx=10, pady=(0, 5))

    # Button to close the analysis window
    tk.Button(window, text="Close Analysis", command=window.destroy, 
              font=("Arial", 12), bg="#FFC0CB", fg=text_color).pack(pady=15)
    
    window.transient(parent_root) # Make it modal
    window.grab_set()
    parent_root.wait_window(window)'''
