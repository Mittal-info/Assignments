
import tkinter as tk


# Quiz Questions
questions = [
    {
        "question": "1. What is the capital of Gujarat?",
        "options": ["Surat", "Ahmedabad", "Gandhinagar", "Rajkot"],
        "answer": "Gandhinagar"
    },
    {
        "question": "2. Which is the longest river in India?",
        "options": ["Ganga", "Yamuna", "Narmada", "Godavari"],
        "answer": "Ganga"
    },
    {
        "question": "3. Which is the highest mountain peak in India?",
        "options": ["Nanda Devi", "Kanchenjunga", "Anamudi", "Guru Shikhar"],
        "answer": "Kanchenjunga"
    },
    {
        "question": "4. Which Indian state is famous for tea gardens?",
        "options": ["Punjab", "Assam", "Gujarat", "Rajasthan"],
        "answer": "Assam"
    },
    {
        "question": "5. Which is the largest Indian state by area?",
        "options": ["Maharashtra", "Madhya Pradesh", "Rajasthan", "Uttar Pradesh"],
        "answer": "Rajasthan"
    }
]


# Store quiz state
state = {
    "index": 0,
    "score": 0,
    "answered": False
}


# Main Window
root = tk.Tk()
root.title("Indian Geography Quiz")
root.geometry("450x350")
root.config(bg="lightblue")


# Heading Label
heading = tk.Label(
    root,
    text="INDIAN GEOGRAPHY QUIZ",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.grid(row=0, column=0, columnspan=2, pady=15)


# Question Label
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    wraplength=420
)
question_label.grid(row=1, column=0, columnspan=2, pady=10)


# Result Label
result_label = tk.Label(
    root,
    text="Select your answer",
    font=("Arial", 12),
    bg="lightblue"
)
result_label.grid(row=3, column=0, columnspan=2, pady=10)


# Score Label
score_label = tk.Label(
    root,
    text="Score: 0/5",
    font=("Arial", 11, "bold"),
    bg="lightblue"
)
score_label.grid(row=4, column=0, columnspan=2)


# Option Buttons
option_buttons = []

def check(option):

    if state["answered"]:
        return

    correct_answer = questions[state["index"]]["answer"]

    if option == correct_answer:

        result_label.config(text="Correct!", fg="green")
        state["score"] += 1

    else:

        result_label.config(text="Wrong! Correct answer: " + correct_answer,
                            fg="red")

    state["answered"] = True

    score_label.config(text="Score: " + str(state["score"]) + "/5")

    for btn in option_buttons:
        btn.config(state="disabled")


# Create 4 buttons in 2x2 grid
for i in range(4):

    btn = tk.Button(
        root,
        text="",
        font=("Arial", 10),
        width=18,
        command=lambda i=i: check(
            questions[state["index"]]["options"][i]
        )
    )

    btn.grid(row=2 + i // 2, column=i % 2, padx=10, pady=5)

    option_buttons.append(btn)


# Load Question
def load_question():

    current_question = questions[state["index"]]

    question_label.config(text=current_question["question"])

    for i in range(4):

        option_buttons[i].config(
            text=current_question["options"][i],
            state="normal"
        )

    result_label.config(text="Select your answer", fg="black")

    state["answered"] = False


# Next Question
def next_question():

    if not state["answered"]:
        result_label.config(text="Please select an answer first!")
        return

    state["index"] += 1

    if state["index"] < len(questions):

        load_question()

    else:

        show_result()


# Show Final Result
def show_result():

    question_label.config(text="Quiz Completed!")

    for btn in option_buttons:
        btn.grid_remove()

    result_label.config(text="Your score: " +
                         str(state["score"]) + "/5",
                         fg="blue")

    next_button.grid_remove()

    restart_button.grid(
        row=5, column=0, columnspan=2, pady=15
    )


# Restart Quiz
def restart_quiz():

    state["index"] = 0
    state["score"] = 0
    state["answered"] = False

    score_label.config(text="Score: 0/5")

    restart_button.grid_remove()

    for btn in option_buttons:
        btn.grid()

    next_button.grid(row=5, column=0, columnspan=2, pady=10)

    load_question()


# Next Button
next_button = tk.Button(
    root,
    text="Next",
    font=("Arial", 11, "bold"),
    command=next_question
)
next_button.grid(row=5, column=0, columnspan=2, pady=10)


# Restart Button
restart_button = tk.Button(
    root,
    text="Restart Quiz",
    font=("Arial", 11, "bold"),
    command=restart_quiz
)


# Load First Question
load_question()


# Run Application
root.mainloop()
