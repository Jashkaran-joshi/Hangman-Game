import random
import tkinter as tk
from tkinter import messagebox

# Global variables
score = 0
run = True

# 🎨 Dark Theme Colors
BG_COLOR = "#1E1E2E"
HEADER_COLOR = "#3A3A55"
BTN_COLOR = "#2E2E40"
BTN_HOVER = "#4C4C6A"
TEXT_COLOR = "#FFFFFF"
ACCENT = "#6C63FF"


def create_hangman_ui():
    """Creates a dark-themed modern Hangman UI."""
    global score, run

    root = tk.Tk()
    root.title("🎯 Hangman Deluxe - Dark Mode")
    root.geometry("950x750")
    root.configure(bg=BG_COLOR)

    # ====== Header Section ======
    header = tk.Frame(root, bg=HEADER_COLOR, height=80)
    header.pack(fill="x")

    title = tk.Label(
        header,
        text="🎯 Hangman Game",
        font=("Segoe UI", 28, "bold"),
        fg=ACCENT,
        bg=HEADER_COLOR,
    )
    title.pack(side="left", padx=20)

    score_label = tk.Label(
        header, text=f"Score: {score}", font=("Segoe UI", 18, "bold"), fg=TEXT_COLOR, bg=HEADER_COLOR
    )
    score_label.pack(side="right", padx=20)

    # ====== Canvas for Hangman ======
    canvas = tk.Canvas(root, width=400, height=350, bg=BG_COLOR, highlightthickness=0)
    canvas.pack(pady=20)

    hangman_images = [tk.PhotoImage(file=f"assets/hangman/h{i}.png") for i in range(1, 8)]
    hangman_display = canvas.create_image(200, 180, image=hangman_images[0])

    # ====== Word Display ======
    word_frame = tk.Frame(root, bg=BG_COLOR)
    word_frame.pack(pady=10)

    with open("assets/words.txt", "r") as f:
        words = f.read().splitlines()
    selected_word = random.choice(words)

    word_labels = []
    for _ in selected_word:
        lbl = tk.Label(word_frame, text="_", font=("Segoe UI", 32, "bold"), fg=ACCENT, bg=BG_COLOR)
        lbl.pack(side="left", padx=5)
        word_labels.append(lbl)

    # ====== Letter Buttons ======
    letters_frame = tk.Frame(root, bg=BG_COLOR)
    letters_frame.pack(pady=15)

    alphabet_images = {ch: tk.PhotoImage(file=f"assets/word/{ch}.png") for ch in "abcdefghijklmnopqrstuvwxyz"}

    guessed_letters = set()
    count = 0

    def check_letter(letter, btn):
        nonlocal count
        btn.config(state="disabled", bg=BTN_HOVER)
        if letter in selected_word:
            for idx, char in enumerate(selected_word):
                if char == letter:
                    word_labels[idx].config(text=letter.upper(), fg="#00FF9C")
            if all(lbl.cget("text") != "_" for lbl in word_labels):
                win_game()
        else:
            count += 1
            if count < 7:
                canvas.itemconfig(hangman_display, image=hangman_images[count])
            else:
                lose_game()

    def win_game():
        global run, score
        score += 1
        if messagebox.askyesno("🎉 You Won!", "Play again?"):
            run = True
            root.destroy()
        else:
            run = False
            root.destroy()

    def lose_game():
        global run, score
        if messagebox.askyesno("💀 You Lost!", f"The word was: {selected_word}\nPlay again?"):
            run = True
            score = 0
            root.destroy()
        else:
            run = False
            root.destroy()

    # Create modern styled buttons
    for idx, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
        btn = tk.Button(
            letters_frame,
            image=alphabet_images[ch],
            bd=0,
            bg=BTN_COLOR,
            activebackground=BTN_HOVER,
            command=lambda l=ch, b=None: check_letter(l, b),
            cursor="hand2",
        )
        btn.grid(row=idx // 13, column=idx % 13, padx=4, pady=4)
        btn.config(command=lambda l=ch, b=btn: check_letter(l, b))

    # ====== Exit Button ======
    exit_img = tk.PhotoImage(file="assets/word/exit.png")
    exit_btn = tk.Button(
        root,
        image=exit_img,
        bd=0,
        bg=BG_COLOR,
        activebackground=BTN_HOVER,
        command=lambda: exit_game(root),
    )
    exit_btn.pack(side="bottom", pady=10)

    def exit_game(win):
        global run
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            run = False
            win.destroy()

    root.mainloop()


# ==== Main Loop ====
while run:
    create_hangman_ui()
