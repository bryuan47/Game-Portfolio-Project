# 🕹️ Jumping Kid (Pygame)

Jumping Kid is a 2D arcade-style game built with **Python** and **Pygame**. The player controls a character that can run, jump, shoot projectiles, and score points by jumping before time runs out.

This project was created as part of a Python fundamentals and game development learning portfolio.

---

## 🎮 Gameplay Overview

* Move left and right across the screen
* Jump to score points
* Shoot projectiles
* Race against a countdown timer
* When time reaches 0, the game ends and the player can restart or quit

---

## 🧠 Features

* Sprite-based animation (idle + running)
* Jump physics using quadratic motion
* Projectile system with limits
* Countdown timer using `pygame.USEREVENT`
* Game over state with restart / quit options
* Score tracking

---

## 🕹️ Controls

| Key            | Action                   |
| -------------- | ------------------------ |
| ⬅️ Left Arrow  | Move left                |
| ➡️ Right Arrow | Move right               |
| Space          | Jump                     |
| Tab            | Shoot projectile         |
| Esc            | Restart game (Game Over) |
| Q              | Quit game                |

---

## ⏱️ Timer Logic

* Game starts with **60 seconds**
* Timer decreases once per second using:

```python
pygame.time.set_timer(pygame.USEREVENT, 1000)
```

* When time reaches 0:

  * Timer stops
  * Game enters **Game Over** state

---

## 🧩 Project Structure

```
Jumping_Kid/
│
├── app.py                # Main game file
├── Game/
│   ├── Run (1).png       # Run animation frames
│   ├── Idle (1).png      # Idle sprite
│   ├── orig.png          # Background image
│
└── README.md
```

---

## 🛠️ Requirements

* Python 3.10+
* Pygame

Install Pygame:

```bash
pip install pygame
```

---

## ▶️ How to Run

```bash
python app.py
```

---

## 🚀 Future Improvements

* Add enemies and collision detection
* Sound effects and background music
* High-score system
* Start menu and pause menu
* Difficulty scaling

---

## 📚 What This Project Demonstrates

* Game loops and frame control
* Event-driven programming
* Object-oriented design (Player, Projectiles)
* Animation state management
* Timers and keyboard input handling

---

## 👤 Author

**Bryuan Mathis**
Python / Game Development / Software Engineering Portfolio Project

---

Feel free to fork, modify, and build upon this project!
