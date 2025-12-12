import tkinter as tk
from tkinter import messagebox

def run_gui(session):
  root = tk.Tk()
  root.title('Feedback Form')
  root.geometry('800x600')
  root.configure(bg='#333333')
  frame = tk.Frame(bg='#333333')
  frame.pack(padx=20, pady=20)
  title = tk.Label(frame, text="Feedback Form", font=("Arial", 24, "bold"), bg='#333333', fg='#FF3399')
  title.grid(row=0, column=0, columnspan=2, pady=20)

# Labels (placed in separate rows)
  tk.Label(frame, text='Reviewer Name', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
  tk.Label(frame, text='Reviewer ID', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')
  tk.Label(frame, text='Session Name', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky='w')
  tk.Label(frame, text='Session ID', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky='w')
  tk.Label(frame, text='Score', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky='w')
  tk.Label(frame, text='Comment', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=6, column=0, padx=10, pady=10, sticky='nw')

# Entry fields
  reviewer_name_entry = tk.Entry(frame, width=40)
  reviewer_ID_entry = tk.Entry(frame, width=40)
  score_entry = tk.Entry(frame, width=40)
  comment_entry = tk.Entry(frame, width=40)

  reviewer_name_entry.grid(row=1, column=1, padx=10, pady=10)
  reviewer_ID_entry.grid(row=2, column=1, padx=10, pady=10)
  score_entry.grid(row=3, column=1, padx=10, pady=10)
  comment_entry.grid(row=4, column=1, padx=10, pady=10)

# Submit button
  def submit_feedback():
     reviewer_name = reviewer_name_entry.get()
     reviewer_ID = reviewer_ID_entry.get()
     score = score_entry.get()
     comment = comment_entry.get()

     if not reviewer_name or not reviewer_ID or not score or not comment:
        messagebox.showerror('Error', 'All fields are required to be filled.')
     else:
        from data import insert_feedback, insert_sentiment
        from analysis import analyze_sentiment 
        insert_feedback(reviewer_name, reviewer_ID,  score, comment)
        sentiment = analyze_sentiment(comment)
        insert_sentiment(sentiment)


        print('Feedback submitted')
        messagebox.showinfo('Success', 'Feedback submitted successfully!')

  tk.Button(frame, text='Submit', fg='#FFFFFF', bg='#FF3399', command=submit_feedback, font=("Arial", 14, "bold")).grid(row=7, column=1, pady=20)

  root.mainloop()