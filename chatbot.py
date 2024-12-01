import openai
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Ladda API-nyckeln från .env-filen
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Kontrollera om API-nyckeln är laddad
if openai.api_key is None:
    raise ValueError("API-nyckeln kunde inte laddas. Kontrollera din .env-fil.")

# Funktion för att få svar från OpenAI API
def get_response(user_input):
    try:
         def get_response(user_input):
    
           response = openai.ChatCompletion.create(
               model="gpt-4",
               messages=[
                   {"role": "system", "content": "Du är en hjälpsam chatbot."},
                   {"role": "user", "content": user_input}
               ],
               max_tokens=150,
               temperature=0.7
           )
           return response.choices[0].message.content.strip()
       except openai.error.OpenAIError as e:
           return f"OpenAI API error: {str(e)}"
       

# Funktion som hanterar när användaren trycker på "Skicka"
def send_message():
    user_input = user_input_entry.get().strip()
    if user_input:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Du: {user_input}\n")
        user_input_entry.delete(0, tk.END)

        # Få svar från API och visa det
        response = get_response(user_input)
        chat_area.insert(tk.END, f"Chatbot: {response}\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)

    user_input_entry.focus_set()

# Inställningar för huvudfönstret
root = tk.Tk()
root.title("Chatbot med GUI")
root.geometry("500x600")

# Textområde för att visa konversationen
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10)

# Textfält för användarens input
user_input_entry = tk.Entry(root, width=40)
user_input_entry.pack(padx=10, pady=5)
user_input_entry.focus_set()

# Knapp för att skicka input
send_button = tk.Button(root, text="Skicka", command=send_message)
send_button.pack(pady=5)

# Starta GUI:t
root.mainloop()

