import random
import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections

class ChatBotUI:
    def __init__(self, master):
        self.master = master
        master.title("Learnify Predictive ChatBot")
        master.configure(bg="#FFB6C1")

        self.message_listbox = tk.Listbox(master, width=80, height=30)
        self.message_listbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.message_listbox.yview)
        self.scrollbar.grid(row=0, column=2, sticky='nsew')
        self.message_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_field = tk.Entry(master, width=50)
        self.entry_field.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.bot_responses = [
            "How can I assist you today?",
            "What can I do for you?",
            "How may I help you?",
            "How can I help you? "
        ]

        # Rule-based responses
        self.rule_responses = {
            "What course does this chatbot focus on?": 
            "This chatbot focuses on the Software Design course.",
            "What is this course about?":
            "This course focuses on design principles, and UML methodologies.",
            "Why is this course important for SWE?":
            "You focus on the user and business requirments needed during the intial development process."
        }

        filename ="/Users/emilyflores/Desktop/Work/EdTechChatBot/cis260.txt"
        self.load_cis260(filename)

    def load_cis260(self, filename):
        try:
            with open(filename, "r") as file:
                for line_number, line in enumerate(file, 1):  
                    if line.strip():
                        parts = line.strip().split("|")  
                    if len(parts) == 2:  
                        question, answer = parts
                        self.rule_responses[question.strip()] = answer.strip()
                    else:
                        print("Invalid format in line", line_number, ":", line.strip())
        except FileNotFoundError:             
            print("File not found:", filename)   
        except Exception as e:
            print("An error has occurred while loading responses:", e)




    def send_message(self):
        # TODO: fix the intital response (outputs bot_responses)
        message = self.entry_field.get()
        if message:
            self.message_listbox.insert(tk.END, "You: " + message)
            self.entry_field.delete(0, tk.END)

            # check if message matches any rule-based responses
            for key in self.rule_responses:
                if key.lower() in message.lower():
                    bot_response = self.rule_responses[key]
                    break
            else:
                bot_response = self.bot_responses[random.randint(0, len(self.bot_responses) - 1)]    
            self.message_listbox.insert(tk.END, "Groove: " + bot_response)
            self.message_listbox.see(tk.END)  


def main():
    root = tk.Tk()
    chatbot_ui = ChatBotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
