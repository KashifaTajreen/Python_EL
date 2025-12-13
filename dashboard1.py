"""import tkinter as tk
from gui import run_gui   # <-- import your feedback GUI function

def open_feedback_form(session):
    # Close the dashboard window before opening feedback form
    root.destroy()
    # Pass the session info to gui.py
    run_gui(session)

root = tk.Tk()
root.title("Session Dashboard")
root.geometry("600x400")
root.configure(bg="#222222")

sessions = [
    {"name": "AI Ethics", "date": "2025-11-20", "id": "S001"},
    {"name": "Urban Innovation", "date": "2025-11-22", "id": "S002"},
    {"name": "Python Workshop", "date": "2025-11-24", "id": "S003"},
]

dashboard_frame = tk.Frame(root, bg="#222222")
dashboard_frame.pack(pady=20)

for i, session in enumerate(sessions):
    card = tk.Frame(dashboard_frame, bg="#FF3399", padx=10, pady=10)
    card.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    tk.Label(card, text=session["name"], font=("Arial", 14, "bold"),
             bg="#FF3399", fg="white").pack()
    tk.Label(card, text=session["date"], font=("Arial", 12),
             bg="#FF3399", fg="white").pack()
    tk.Button(card, text="Give Feedback",
              command=lambda s=session: open_feedback_form(s),
              bg="white", fg="#FF3399", font=("Arial", 10, "bold")).pack(pady=5)

root.mainloop()"""
