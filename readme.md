# 4x4 Tic-Tac-Toe Game

This is a 4x4 Tic-Tac-Toe game implemented in Python using Pygame.

## Project Structure

- `tictactoe_4x4.py`: Main game file
- `sound_utils.py`: Utility file containing the sound generation function
- `requirements.txt`: List of required Python packages
- `README.md`: This file

## Setup Instructions

1. Ensure you have Python 3.7+ installed on your system.

2. Create a virtual environment:
   ```
   python -m venv games
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source games/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

To run the game, use the following command:

```
python tictactoe_4x4.py 
```

or use the script to run it
```bash
chmod +x run-game-sh.sh
./run-game-sh.sh
```

## How to Play

- Click on an empty cell to place your mark ('X' or 'O').
- The goal is to get 4 of your marks in a row (horizontally, vertically, or diagonally).
- Press 'R' to restart the game at any time.

Enjoy playing!