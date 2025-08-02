

# **Hangman-Game**

Hangman Game is a GUI-based word guessing game built using Python and Tkinter. The objective is simple: guess the hidden word by selecting letters. Each wrong guess adds to the hangman drawing. Fail to guess the word before your lives run out, and the hangman meets his fate!
The project features a modern dark mode interface, clickable alphabet icons, and dynamic gameplay that keeps track of your score across multiple rounds.

## **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#Contributing)

## **Features**  
- **Dark Mode UI**: A visually appealing interface with a modern design.  
- **Clickable Character Icons**: Guess letters by clicking alphabet icons.  
- **Dynamic Hangman Graphics**: Images update with each wrong guess.  
- **Score Tracking**: Keeps track of the player’s score across rounds.  
- **External Word List**: Words are dynamically loaded from a text file.  
- **Game Over Dialogs**: Displays the correct word and asks to play again.  
- **Replay Option**: Restart or exit directly from the UI.  

## **Technologies Used**
- **Programming Language**: Python v3.x
- **GUI Framework**: Tkinter
- **Assets**: PNG images for alphabets and hangman states

## **Project Structure**
```
Hangman-Game/Home/
│
├── main.py                   # Main game script
│
├── assets/
│   ├── hangman/              # Hangman state images (h1.png to h7.png)
│   └── word/                 # Alphabet button images (a.png to z.png, exit.png)
│
└── assets/words.txt          # Word list for the game
```


## **Installation**
Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
cd Home
```

### **2. (Optional) Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Verify Assets**
Ensure that the following assets are correctly placed:
- `assets/hangman/h1.png` to `h7.png`
- `assets/word/a.png` to `z.png` and `exit.png`
- `assets/words.txt` contains your list of words.

## **Configuration**
- No environment variables or special configuration are required.
- You can customize the word list by editing `assets/words.txt.`

## **Usage**
Run the game using:
```bash
python hangman.py
```
- Click on the alphabet icons to guess letters.
- Correct guesses reveal the letters, while incorrect guesses draw parts of the hangman.
- The game ends when you either guess the word or the hangman is fully drawn.
- Choose to restart or exit after each game round.

## **Contributing**
Your feedback is appreciated!
If you’d like to suggest improvements or report bugs, please open an issue or submit a pull request.
