## Higher Lower Game 🎮

This project is a command-line version of the "Higher Lower" game written in Python.  
The player must guess which person or brand has more social media followers.

The game continues as long as the player gives correct answers.  
When the player makes a wrong guess, the game ends and the final score is displayed.

---

## Features ✨

- Randomly selects two different entries from the dataset
- Displays:
  - Name
  - Description
  - Country
- Asks the user to guess who has more followers
- Keeps track of the score
- Ends the game when the user guesses incorrectly
- Uses external modules for:
  - Game data
  - 
---

- **main.py** → Contains the main game logic  
- **day14gamedata.py** → Stores the list of dictionaries with follower data  
- **day14logo.py** → Contains ASCII art for the game logo and "vs" graphic  
- **README.md** → Project documentation  

---

## How It Works ▶️

1. Two random entries are selected from the dataset.
2. The program ensures both selections are different.
3. The user sees:
   - Compare A
   - VS graphic
   - Against B
4. The user types:
   - `A` if they think A has more followers
   - `B` if they think B has more followers
5. If the answer is correct:
   - The score increases
   - B becomes the new A
   - A new B is randomly selected
6. If the answer is wrong:
   - The game ends
   - Final score is displayed
