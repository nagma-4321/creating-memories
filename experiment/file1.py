
print("hello")


import tkinter as tk
from tkinter import ttk, messagebox

# Questions for the chatbot
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you could write a book about the philosophy of living life, what would the title be?",
    "Do you pay gratitude to the higher power for all the opportunities in your life?",
    "What advice would you give yourself to be happier in life?"
]

# Suggestion for Question 7
suggestion = (
    "Please convert them to physical copies; otherwise, you might lose them due to storage issues."
)

# Variables
current_question_index = 0
user_responses = {}

# Function to add messages to the chat
def add_message(sender, message, sender_type):
    """Adds a message to the chatbox."""
    bubble_color = "#FFC7C7" if sender_type == "bot" else "#E1FFC7"
    text_align = "w" if sender_type == "bot" else "e"
    text_font = ("Arial", 12, "italic") if sender_type == "bot" else ("Arial", 12, "bold")
    border_color = "red"
    bubble = tk.Label(
        chat_frame,
        text=f"{sender}: {message}",
        bg=bubble_color,
        fg="black",
        font=text_font,
        anchor=text_align,
        padx=10,
        pady=5,
        wraplength=400,
        relief="solid",
        bd=2,
        highlightbackground=border_color,
        highlightthickness=1,
    )
    bubble.pack(anchor=text_align, pady=5)
    chat_canvas.yview_moveto(1.0)  # Scroll to the bottom as new messages appear

# Function to ask the next question
def ask_next_question():
    global current_question_index
    if current_question_index < len(questions):
        question = questions[current_question_index]
        add_message("DATE TO MEMORIES", question, "bot")
    else:
        name = user_responses.get("What's your name?", "Friend")
        add_message(
            "DATE TO MEMORIES",
            f"Thank you for your responses, {name}! I appreciate your thoughtful answers and wish you the best for the future.",
            "bot",
        )

# Function to handle user responses
def handle_response():
    global current_question_index
    user_message = user_input.get()
    if user_message.strip():
        if current_question_index < len(questions):
            question = questions[current_question_index]
            user_responses[question] = user_message
            add_message("You", user_message, "user")
            if current_question_index == 7:  # Question about memories
                add_message("DATE TO MEMORIES", suggestion, "bot")
            current_question_index += 1
            ask_next_question()
    else:
        messagebox.showwarning("Incomplete Response", "Please answer the question to proceed.")
    user_input.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("DATE TO MEMORIES (2024 EDITION)")
root.geometry("600x700")
root.configure(bg="#FF9900")

# Heading
heading_frame = tk.Frame(root, bg="#FF9900")
heading_frame.pack(pady=10)
heading_label = tk.Label(
    heading_frame,
    text="DATE TO MEMORIES (2024 EDITION)",
    font=("Arial", 20, "bold"),
    bg="#FF9900",
    fg="red",
)
heading_label.pack()
subtitle_label = tk.Label(
    heading_frame,
    text="Reliving Moments, Creating Memories",
    font=("Arial", 12, "italic"),
    bg="#FF9900",
    fg="black",
)
subtitle_label.pack()

# Chat area with scrolling
chat_frame_container = tk.Frame(root, bg="#FF9900")
chat_frame_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

chat_canvas = tk.Canvas(chat_frame_container, bg="#FF9900")
chat_scrollbar = ttk.Scrollbar(chat_frame_container, orient=tk.VERTICAL, command=chat_canvas.yview)
chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_frame = tk.Frame(chat_canvas, bg="#FF9900")
chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")
chat_canvas.configure(yscrollcommand=chat_scrollbar.set)
chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Update the scroll region whenever new content is added
def update_scroll_region(event=None):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

chat_frame.bind("<Configure>", update_scroll_region)

# Message input
input_frame = tk.Frame(root, bg="#FF9900")
input_frame.pack(fill=tk.X, pady=10)
user_input = ttk.Entry(input_frame, font=("Arial", 14))
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

# Send button
send_button = ttk.Button(input_frame, text="Send", command=handle_response)
send_button.pack(side=tk.RIGHT, padx=10)

# Start conversation
ask_next_question()

root.mainloop()





        