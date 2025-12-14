import tkinter as tk
from tkinter import ttk
from data import get_session_summary, get_comments_for_session

def create_bar_graph(frame, score, sentiment):
    """Creates a simple bar graph on a Tkinter Canvas."""
    canvas = tk.Canvas(frame, width=400, height=200, bg="white", highlightthickness=1, highlightbackground="gray")
    canvas.pack(pady=10)

    # Calculate heights (Score is out of 5, Sentiment is out of 1.0)
    score_norm = (score / 5.0) if score <= 5 else 1.0  # Normalize to 1.0
    sentiment_norm = (sentiment + 1.0) / 2.0 if -1.0 <= sentiment <= 1.0 else 0.5 # Normalize to 0.0-1.0 range

    # Canvas dimensions
    bar_width = 80
    gap = 100
    y_max = 180
    y_start = 190
    
    # --- Score Bar ---
    score_height = y_max * score_norm
    canvas.create_rectangle(50, y_start - score_height, 50 + bar_width, y_start, fill="#4CAF50")
    canvas.create_text(90, 10, text="Feedback Analysis", font=("Helvetica", 12, "bold"))
    canvas.create_text(90, y_start - score_height - 10, text=f"{score:.1f}", font=("Helvetica", 10))
    canvas.create_text(90, y_start + 10, text="Avg Score (out of 5)", font=("Helvetica", 9))

    # --- Sentiment Bar ---
    sentiment_height = y_max * sentiment_norm
    canvas.create_rectangle(50 + gap, y_start - sentiment_height, 50 + gap + bar_width, y_start, fill="#2196F3")
    canvas.create_text(90 + gap, y_start - sentiment_height - 10, text=f"{sentiment:.2f}", font=("Helvetica", 10))
    canvas.create_text(90 + gap, y_start + 10, text="Avg Sentiment (-1 to 1)", font=("Helvetica", 9))

def run_analysis_view(root, session):
    """Sets up the window to display analysis for a specific session."""
    
    # 1. Fetch Data
    session_id=session['id']
    session_name=session['name']
    summary = get_session_summary(session_id)
    comments = get_comments_for_session(session_id)

    # 2. Create Window
    analysis_window = tk.Toplevel(root)
    analysis_window.title(f"Analysis for Session: {session_name}")
    analysis_window.geometry("800x700")

    main_frame = ttk.Frame(analysis_window, padding="10")
    main_frame.pack(fill='both', expand=True)

    # 3. Display Summary (Text)
    ttk.Label(main_frame, text=f"Session ID: {session_id}\n Session Name: {session_name}", font=("Helvetica", 16, "bold")).pack(pady=5)
    
    avg_score = summary.get('avg_score', 0.0)
    avg_sentiment = summary.get('avg_sentiment', 0.0)

    ttk.Label(main_frame, text=f"Average Score: {avg_score:.1f} / 10", font=("Helvetica", 12,'bold')).pack(pady=5)
    ttk.Label(main_frame, text=f"Average Sentiment: {avg_sentiment:.2f} (-1.0 to 1.0)", font=("Helvetica", 12)).pack()
    
    # 4. Display Graph
    # ---- SCORE PROGRESS BAR ----
    ttk.Label(main_frame, text="Overall Session Rating", font=("Helvetica", 13, "bold")).pack(pady=(10, 5))

    score_bar = ttk.Progressbar(
    main_frame,
    orient="horizontal",
    length=400,
    mode="determinate",
    maximum=10
    )
    score_bar.pack(pady=5)
    score_bar["value"] = avg_score

    # ---- SENTIMENT INTERPRETATION ---
    # ---- SENTIMENT INTERPRETATION (SCORE-AWARE) ----
    if avg_score >= 7:
      sentiment_text = "😊 Positive Feedback"
    elif avg_score <= 4:
      sentiment_text = "😟 Negative Feedback"
    else:
      sentiment_text = "😐 Neutral Feedback"

    ttk.Label( main_frame,text=f"Overall Sentiment: {sentiment_text}",font=("Helvetica", 12)).pack(pady=5)
    feedback_count = len(comments)

    ttk.Label(main_frame,text=f"Total Responses: {feedback_count}",font=("Helvetica", 12)).pack(pady=5)

    # 5. Display Comments
    ttk.Label(main_frame, text="\n--- Individual Feedback Comments ---", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Use a ScrolledText or Treeview for better display of comments
    comments_frame = ttk.Frame(main_frame)
    comments_frame.pack(fill='both', expand=True)

    tree = ttk.Treeview(comments_frame, columns=('Score', 'Comment'), show='headings')
    tree.heading('Score', text='Score')
    tree.heading('Comment', text='Comment')
    tree.column('Score', width=80, anchor='center')
    tree.column('Comment', width=600, anchor='w')

    for score, comment in comments:
        tree.insert('', tk.END, values=(score, comment))

    tree.pack(side='left', fill='both', expand=True)
    
    # Add a scrollbar
    vsb = ttk.Scrollbar(comments_frame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

def create_score_distribution(frame, scores):
    canvas = tk.Canvas(frame, width=500, height=250, bg="white", highlightthickness=1)
    canvas.pack(pady=15)

    canvas.create_text(250, 15, text="Score Distribution", font=("Helvetica", 13, "bold"))

    max_count = max(scores.values()) if scores else 1

    bar_width = 25
    spacing = 15
    x_start = 30
    y_base = 220
    max_height = 160

    for i in range(1, 11):
        count = scores.get(i, 0)
        height = (count / max_count) * max_height if max_count else 0

        x1 = x_start + (i - 1) * (bar_width + spacing)
        y1 = y_base - height
        x2 = x1 + bar_width
        y2 = y_base

        canvas.create_rectangle(x1, y1, x2, y2, fill="#4CAF50")
        canvas.create_text(x1 + bar_width / 2, y_base + 10, text=str(i), font=("Helvetica", 9))
        canvas.create_text(x1 + bar_width / 2, y1 - 8, text=str(count), font=("Helvetica", 9))
