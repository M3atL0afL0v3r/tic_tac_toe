# tic_tac_toe
## Overview

This is a console-based Tic-Tac-Toe game implemented in Python. The player competes against the computer, which can play at two difficulty levels: Easy (random moves) or Hard (Minimax AI). The game also includes a coin flip to decide who goes first and a play again feature for repeated matches.

## Features

*Two Difficulty Levels
  +Easy: The computer chooses random moves.
  +Hard: The computer uses the Minimax algorithm for optimal moves.
*Coin Flip to Decide First Player
*Input Validation
  +Accepts only valid board positions (TL, MM, BR, etc.).
  +Rejects invalid or occupied positions.
*Dynamic Board Display
  +Shows a grid with row/column references for easy input.
*Game Outcome
  +Detects win, loss, or tie.
*Replay Option
  +After a game ends, the player can choose to play again by entering Y or N.

## How to Play

1. Run the game using Python 3:
   ```
   python tic_tac_toe.py
   ```
2. Choose the difficulty level:
  +1 for Easy
  +2 for Hard
3. Call the coin flip:
  +Enter H for heads or T for tails.
4. Enter your moves using two-letter codes for the row and column:
  +T = Top, M = Middle, B = Bottom
  +L = Left, M = Middle, R = Right
  +Example: TL = Top Left, MM = Middle Middle, BR = Bottom Right
5. Watch the computer make its move.
6. The game ends when either player wins or the board is full (tie).
7. After the game, choose whether to play again by entering Y (yes) or N (no).

## Example Board
```
  Top Left(TL) | Top Middle(TM) | Top Right(TR)
  Middle Left(ML) | Middle Middle(MM) | Middle Right(MR)
  Bottom Left(BL) | Bottom Middle(BM) | Bottom Right(BR)
  
   X |   | O
  ---+---+---
     | X |  
  ---+---+---
   O |   | X
```
## How the Minimax AI Works
The Minimax algorithm is a decision-making algorithm used in two-player turn-based games like Tic-Tac-Toe. It assumes that both players play optimally and explores all possible future moves to choose the best outcome.
*Maximizing Player: The computer tries to maximize its score by selecting the move with the highest evaluation.
*Minimizing Player: The human player is assumed to play optimally, minimizing the computer’s score.
*Evaluation Function:
  ++10 if the computer can win.
  +-10 if the player can win.
  +0 if the game ends in a tie.
*Depth Factor: The score is adjusted by the depth of recursion to prefer faster wins and slower losses.
This ensures that on Hard difficulty, the computer never loses if played correctly.

## Dependencies
>Python 3.x
>No external libraries required.

## Author
**David Gautier**
