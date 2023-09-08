import tkinter as tk
import random

# Define a list of words and their translations
vocabulary = {
    "apple": "manzana",
    "banana": "plátano",
    "car": "coche",
    # Add more words and translations here
}

# Function to display the meaning of a random word
def display_random_meaning():
    random_word = random.choice(list(vocabulary.keys()))
    meaning_label.config(text=f"Translate: {vocabulary[random_word]}")
    # Store the correct answer for later comparison
    display_random_meaning.answer = random_word

# Function to check the user's answer
def check_answer():
    user_word = user_input.get().strip().lower()
    if user_word == display_random_meaning.answer:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect. Try again.")

# Create the main application window
root = tk.Tk()
root.title("Language Vocabulary Quiz App")

# Create a label widget to display a question
question_label = tk.Label(root, text="Translate the word:", font=("Helvetica", 16))
question_label.pack()

# Create a display meaning button
display_meaning_button = tk.Button(root, text="Display Meaning", command=display_random_meaning)
display_meaning_button.pack()

# Create an entry widget for user input
user_input = tk.Entry(root, font=("Helvetica", 14))
user_input.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

# Create a label to display the meaning
meaning_label = tk.Label(root, text="", font=("Helvetica", 14))
meaning_label.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

# Run the application
root.mainloop()
