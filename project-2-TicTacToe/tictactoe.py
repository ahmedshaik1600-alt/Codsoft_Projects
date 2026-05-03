"""
CodSoft AI Internship — Task 2
GRID.AI: Tic-Tac-Toe with Minimax + Alpha-Beta Pruning
Author: [Your Name]

The AI uses the Minimax algorithm with Alpha-Beta Pruning to play optimally.
It is unbeatable on 'hard' difficulty — the best you can do is draw!
"""

import math
import os
import random

# ── Constants ──────────────────────────────────────
HUMAN = 'X'
AI    = 'O'
EMPTY = ' '

WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
    [0, 4, 8], [2, 4, 6]               # diagonals
]


# ── Board Utilities ────────────────────────────────
def new_board():
    return [EMPTY] * 9

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n  ╔═══╦═══╦═══╗")
    for row in range(3):
        cells = []
        for col in range(3):
            idx = row * 3 + col
            val = board[idx]
            cells.append(f" {val} ")
        print(f"  ║{'║'.join(cells)}║")
        if row < 2:
            print("  ╠═══╬═══╬═══╣")
    print("  ╚═══╩═══╩═══╝")
    # Show position numbers
    print("\n  Position guide:")
    print("  ╔═══╦═══╦═══╗")
    for row in range(3):
        cells = [f" {row*3+col+1} " for col in range(3)]
        print(f"  ║{'║'.join(cells)}║")
        if row < 2:
            print("  ╠═══╬═══╬═══╣")
    print("  ╚═══╩═══╩═══╝\n")

def check_winner(board):
    for line in WIN_LINES:
        a, b, c = line
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    return EMPTY not in board and check_winner(board) is None

def get_empty(board):
    return [i for i, v in enumerate(board) if v == EMPTY]

def is_terminal(board):
    return check_winner(board) is not None or not get_empty(board)


# ── Minimax with Alpha-Beta Pruning ───────────────
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:    return 10 - depth
    if winner == HUMAN: return depth - 10
    if is_draw(board):  return 0

    if is_maximizing:
        best = -math.inf
        for i in get_empty(board):
            board[i] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i] = EMPTY
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Alpha-Beta cutoff
        return best
    else:
        best = math.inf
        for i in get_empty(board):
            board[i] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i] = EMPTY
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha-Beta cutoff
        return best


def best_move(board, difficulty):
    """Get the AI's best move based on difficulty."""
    empty = get_empty(board)

    if difficulty == 'easy':
        return random.choice(empty)

    if difficulty == 'medium':
        # 40% chance of random move
        if random.random() < 0.4:
            return random.choice(empty)

    # Hard / Unbeatable: full Minimax
    best_score = -math.inf
    move = None
    for i in empty:
        board[i] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i] = EMPTY
        if score > best_score:
            best_score = score
            move = i
    return move


# ── Game Loop ──────────────────────────────────────
def play_game(difficulty='hard'):
    board = new_board()
    scores = {HUMAN: 0, AI: 0, 'Draw': 0}

    while True:
        print_board(board)
        print(f"  Difficulty: {difficulty.upper()}")
        print(f"  Score  →  You: {scores[HUMAN]}  |  AI: {scores[AI]}  |  Draw: {scores['Draw']}")
        print()

        # Human turn
        while True:
            try:
                pos = int(input("  Enter position (1-9): ")) - 1
                if pos < 0 or pos > 8:
                    print("  ⚠ Enter a number between 1 and 9.")
                    continue
                if board[pos] != EMPTY:
                    print("  ⚠ That cell is taken. Choose another.")
                    continue
                break
            except ValueError:
                print("  ⚠ Invalid input. Enter a number.")

        board[pos] = HUMAN
        winner = check_winner(board)

        if winner or is_draw(board):
            print_board(board)
            if winner == HUMAN:
                print("  🎉 You win! Amazing play!\n")
                scores[HUMAN] += 1
            elif is_draw(board):
                print("  🤝 It's a draw! Well played.\n")
                scores['Draw'] += 1
        else:
            # AI turn
            print_board(board)
            print(f"  Score  →  You: {scores[HUMAN]}  |  AI: {scores[AI]}  |  Draw: {scores['Draw']}")
            print("  🤖 AI is thinking...\n")
            ai_pos = best_move(board, difficulty)
            board[ai_pos] = AI
            winner = check_winner(board)

            if winner or is_draw(board):
                print_board(board)
                if winner == AI:
                    print("  🤖 AI wins! Better luck next time.\n")
                    scores[AI] += 1
                elif is_draw(board):
                    print("  🤝 It's a draw! Well played.\n")
                    scores['Draw'] += 1
            else:
                continue

        # Play again?
        again = input("  Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n  Thanks for playing GRID.AI! 👾\n")
            break
        board = new_board()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
  ╔══════════════════════════════════╗
  ║         G R I D . A I           ║
  ║   Tic-Tac-Toe · Minimax AI      ║
  ║   CodSoft AI Internship T2      ║
  ╚══════════════════════════════════╝
    """)
    print("  Select difficulty:")
    print("  1. Easy    (random AI)")
    print("  2. Medium  (partially smart)")
    print("  3. Hard    (unbeatable Minimax)\n")

    choice = input("  Enter choice (1/2/3): ").strip()
    diff_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
    difficulty = diff_map.get(choice, 'hard')

    print(f"\n  Starting {difficulty.upper()} mode. You are X, AI is O.\n")
    input("  Press Enter to begin...")
    play_game(difficulty)


if __name__ == "__main__":
    main()
