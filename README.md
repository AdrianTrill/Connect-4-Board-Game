---

# Connect 4 Board Game

### Description
This project is an implementation of the classic **Connect 4** game, featuring both a **graphical user interface (GUI)** and a **command-line interface (CLI)**. The game can be played by two human players or against an AI opponent with adjustable difficulty levels. It uses the **minimax algorithm** with **alpha-beta pruning** to power the AI. The GUI is built using **Pygame**, while the logic is implemented in **Python**.

---

### Features
- **Command-Line Interface (CLI)** for text-based play.
- **Graphical User Interface (GUI)** built with Pygame, providing an intuitive and visually appealing experience.
- Play **two-player** games or challenge the **AI**.
- Three levels of AI difficulty: **Easy**, **Medium**, and **Hard**.
- **Minimax algorithm with alpha-beta pruning** for efficient decision-making by the AI.
- Game mechanics include **horizontal, vertical, and diagonal win checks**.

---

### Project Structure

```
📁 domain
   └── board.py            # Board class managing the game board.

📁 RunProgram
   └── RunProgram.py       # Main entry point for running the game.

📁 Services
   ├── AI.py               # AI logic, including minimax algorithm and pruning.
   └── Game.py             # Game class managing the game state and rules.

📁 UI
   ├── UI.py               # Command-line interface for text-based game.
   └── GUI.py              # Graphical user interface using Pygame.

📁 Tests
   └── tests.py            # Unit tests for various game mechanics.

📁 images
   ├── red.png             # Image of the red token used in the game.
   └── black.png           # Image of the black token used in the game.

📁 resources
   ├── dog.jpeg            # Image resource for the game (example, not directly used).

```

---

### How to Run

#### 1. Command-Line Interface (CLI)
1. Clone the repository.
2. Run the `RunProgram.py` file to start the game.
```bash
python3 RunProgram.py
```
3. Select the game mode (Player vs Player or Player vs AI) and follow the on-screen instructions to play.

#### 2. Graphical User Interface (GUI)
1. Install **Pygame** via pip:
```bash
pip install pygame
```
2. Run the `UI.py` file to start the GUI version of the game:
```bash
python3 UI.py
```
3. Play against a friend or challenge the AI with adjustable difficulty settings.

---

### AI Mechanics
- The AI uses the **minimax algorithm** with **alpha-beta pruning** to efficiently decide moves.
- AI difficulty levels adjust the search depth:
  - **Easy**: Depth = 2
  - **Medium**: Depth = 4
  - **Hard**: Depth = 5
- The AI evaluates board states based on the number of connected pieces and prioritizes winning moves, while also attempting to block the opponent’s winning moves.

---

### Tests
Unit tests for the game are provided in the `tests.py` file. The tests cover:
- Draw conditions
- Win conditions (horizontal, vertical, diagonal)
- AI behavior and blocking strategies

To run the tests:
```bash
python3 -m unittest discover tests
```

---

### Technologies Used
- **Python**: Core game logic and AI.
- **Pygame**: For the graphical user interface (GUI).
- **Numpy**: Efficient handling of the game board and arrays.

---

### Future Enhancements
- Multiplayer support over a network.
- Adding sound effects and animations to enhance the GUI experience.
- Further optimizations in AI decision-making for larger board sizes or advanced strategies.

---

### License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
