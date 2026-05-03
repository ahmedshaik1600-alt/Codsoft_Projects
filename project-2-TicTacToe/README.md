# GRID.AI — Tic-Tac-Toe AI
### CodSoft AI Internship | Task 2

---

## Overview
GRID.AI is an unbeatable Tic-Tac-Toe AI powered by the **Minimax algorithm with Alpha-Beta Pruning**. It includes a Python terminal version and a glassmorphic neon web UI.

---

## Files
| File | Description |
|------|-------------|
| `tictactoe.py` | Python terminal game with Minimax AI |
| `index.html` | Neon glassmorphic web UI |
| `README.md` | Project documentation |

---

## How to Run

### Web UI
Open `index.html` in any browser. No installation needed.

### Terminal
```bash
python tictactoe.py
```
Requires Python 3.6+

---

## Algorithm: Minimax + Alpha-Beta Pruning

### Minimax
The AI simulates **all possible future game states** recursively, choosing the move that maximizes its score while minimizing the human's.

- AI winning = **+10** (minus depth, prefers faster wins)
- Human winning = **-10** (plus depth)
- Draw = **0**

### Alpha-Beta Pruning
Cuts off branches that can't affect the final decision, making the algorithm significantly faster without changing the result.

```
alpha = best score maximizer can guarantee
beta  = best score minimizer can guarantee
If beta <= alpha → prune the branch
```

---

## Difficulty Levels
| Level | Behavior |
|-------|----------|
| Easy | Fully random moves |
| Medium | 60% Minimax, 40% random |
| Hard | Full Minimax — unbeatable |

---

## Web UI Features
- Neon glow aesthetic with animated background grid
- Score tracking across games
- 2-player mode
- Animated win detection with particles
- Typing indicator for AI "thinking"
