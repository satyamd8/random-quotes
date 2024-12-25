import tkinter as tk
import requests
import os
from tkinter import messagebox, PhotoImage

#fetches quote from quotable api, dependent on tag/category
def fetch_quote(category):
    url = f"https://api.quotable.io/random?tags={category}"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    
    data = response.json()
    quote = f"\"{data['content']}\"\n\n- {data['author']}"
    quote_label.config(text=quote)


#creates gui environment
root = tk.Tk()
root.title("Quote Generator")
root.geometry("600x600")

#script_dir = os.path.dirname(__file__)
icon = PhotoImage(file="greek.png")
root.iconphoto(True, icon)

ask_label = tk.Label(root, text="Choose a type of quote:", wraplength=500, justify="center", font=("Helvetica", 12), pady=15)
ask_label.pack(pady=20)

categories = {
    "Inspirational": "inspirational",
    "Love": "love",
    "Humor": "Humorous",
    "Wisdom": "wisdom",
    "Depressing": "sadness",
}

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

for text, tag in categories.items():
    btn = tk.Button(button_frame, text=text, command=lambda t=tag: fetch_quote(t), font=("Times New Roman", 12), width=20)
    btn.pack(side="top", padx=10)

quote_label = tk.Label(root, wraplength=500, justify="center", font=("Georgia", 14), pady=20)
quote_label.pack(pady=20)

root.mainloop()