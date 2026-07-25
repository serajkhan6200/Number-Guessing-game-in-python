# 🎯 Number Guessing Game

A simple Python-based Number Guessing Game where the computer randomly selects a number between **1 and 100**, and the player has to guess it with the help of hints.

---

## 📌 Features

- 🎲 Random number generation
- 🔢 Guess a number between 1 and 100
- ⬆️ Gives "Higher" hint
- ⬇️ Gives "Lower" hint
- ✅ Displays success message when guessed correctly
- 📊 Counts the total number of attempts

---

## 🛠️ Technologies Used

- Python 3
- `random` module

---

## 📂 Project Structure

```
Number-Guessing-game-in-python/
│── NumberGuessingGame.py
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/serajkhan6200/Number-Guessing-game-in-python.git
```

2. Open the project folder

```bash
cd Number-Guessing-game-in-python
```

3. Run the program

```bash
python NumberGuessingGame.py
```

---

## 💻 Sample Output

```
Please Guess Your Number Between 1 to 100 :- 50
Go a Little Higher ⬆

Please Guess Your Number Between 1 to 100 :- 75
Go a Little Lower ↓

Please Guess Your Number Between 1 to 100 :- 68
You are Right ✅, You Guessed The Number in 3 tries
```

---

## 🧠 How It Works

- The computer generates a random number between **1 and 100**.
- The player enters a guess.
- If the guess is too high, the program displays:
  - `Go a Little Lower ↓`
- If the guess is too low, the program displays:
  - `Go a Little Higher ⬆`
- When the correct number is guessed, the program displays the total number of attempts and ends the game.

---

## 🚀 Future Improvements

- Difficulty levels (Easy, Medium, Hard)
- Limited number of attempts
- Play Again option
- High Score tracking
- GUI version using Tkinter
- Sound effects

---

## 👨‍💻 Author

**Mohammad Serajuddin**

- GitHub: https://github.com/serajkhan6200

---

⭐ If you like this project, don't forget to give it a **Star** on GitHub!
