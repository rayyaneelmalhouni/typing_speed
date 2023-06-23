# # Imports
import random
import tkinter as tk
from tkinter import messagebox
from random_words import random_words

# # Variables
WORDS_PER_LINE = 7
words = []
words_typed = 0
current_word_index = 0
playing = False


# # # Functions
# # Detectors
def on_start():
    global playing, words_typed, current_word_index
    if start_btn.cget("text") == "Start":
        messagebox.showinfo(title="How the program works",
                            message=f"_The program calculates the wpm(words per minute) of your typing.\n"
                                    f"_To start click on the start button then start typing on the input.\n"
                                    f"_After writing each word you should move to the next one by clicking on the space "
                                    f"bar.\n"
                                    f"_If the word that you typed is wrong or you didn't type anything then it will "
                                    f"not be counted.")
    if not playing:
        generate_words()
        display_words()
        start_timer(60)
        playing = True
        words_typed = 0
        current_word_index = 0
        change_word()
        main_input.delete(0, tk.END)
        main_input.focus_set()


def on_space(event):
    global current_word_index
    if playing:
        check_value()
        main_input.delete(0, tk.END)
        if not (current_word_index + 1) % WORDS_PER_LINE:
            next_row()
        else:
            current_word_index += 1
            change_word()


# # Timer Managers
def start_timer(count):
    if count > 0:
        timer_label.config(text=str(count))
        timer_label.after(1000, start_timer, count - 1)
    else:
        stop_timer()


def stop_timer():
    global playing
    playing = False
    timer_label.config(text="60")
    word_label.config(text="Finished!!")
    start_btn.config(text="Restart")
    display_answer()


# # Data manipulators
def generate_words():
    global words
    words = random_words
    random.shuffle(words)


def next_row():
    global words, current_word_index
    row = words[:WORDS_PER_LINE]
    words = words[WORDS_PER_LINE:]
    words.extend(row)
    display_words()
    current_word_index = 0
    change_word()


# # Data readers
def display_words():
    text_1 = ""
    text_2 = ""
    for i in range(WORDS_PER_LINE):
        text_1 += f"{words[i]} "
        text_2 += f"{words[i+ WORDS_PER_LINE]} "
    first_text_line.config(text=text_1)
    second_text_line.config(text=text_2)


def check_value():
    global words_typed
    given_word = main_input.get().replace(" ", "")
    current_word = words[current_word_index]
    if current_word == given_word:
        words_typed += 1


# # Other
def display_answer():
    first_text_line.config(text="Your Typing speed was:")
    second_text_line.config(text=f"  {words_typed} WPM ")


def change_word():
    word = words[current_word_index]
    word_label.config(text=word)


# # # Display
# # Window
window = tk.Tk()
window.title("Typing Speed")
window.config()

# # Window Elements
# Buttons
start_btn = tk.Button(text="Start", font=("Arial", 18), command=on_start)
start_btn.grid(row=4, column=0, padx=50)

# Labels
title_label = tk.Label(text="Typing Speed", font=("Arial", 48), pady=50)
title_label.grid(row=0, column=1)

word_label = tk.Label(text="", font=("Arial", 18), pady=10)
word_label.grid(row=1, column=1)

first_text_line = tk.Label(text="Welcome to the Typing Speed Program", font=("Arial", 16), width=50)
first_text_line.grid(row=2, column=1)

second_text_line = tk.Label(text="Click on the start button to start", font=("Arial", 16), width=50)
second_text_line.grid(row=3, column=1)

timer_label = tk.Label(text="60", font=("Arial", 24), padx=50, width=1)
timer_label.grid(row=0, column=2)

# Inputs
main_input = tk.Entry(width=50)
main_input.bind("<space>", on_space)
main_input.grid(row=4, column=1, pady=50)

# Mainloop
window.mainloop()














