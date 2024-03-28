import random
import tkinter as tk

class ChatBotUI:
    def __init__(self, master):
        self.master = master
        master.title("Learnify ChatBot")

        self.message_listbox = tk.Listbox(master, width=50, height=20)
        self.message_listbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.message_listbox.yview)
        self.scrollbar.grid(row=0, column=2, sticky='nsew')
        self.message_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_field = tk.Entry(master, width=40)
        self.entry_field.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.bot_responses = [
            "Hello, how can I assist you today?",
            "What can I do for you?",
            "How may I help you?"
        ]

    def send_message(self):
        message = self.entry_field.get()
        if message:
            self.message_listbox.insert(tk.END, "You: " + message)
            self.entry_field.delete(0, tk.END)
            bot_response = self.bot_responses[random.randint(0, len(self.bot_responses) - 1)]
            self.message_listbox.insert(tk.END, "Bot: " + bot_response)
            self.message_listbox.see(tk.END)  

def main():
    root = tk.Tk()
    chatbot_ui = ChatBotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
