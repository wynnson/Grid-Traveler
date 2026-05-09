# Grid Traveler
<div align="center">
<img width="49%" height="825" alt="image" src="https://github.com/user-attachments/assets/32958034-3d49-4e3b-9edc-ebaeea949846" />
<img width="49%" height="827" alt="image" src="https://github.com/user-attachments/assets/cf6c7448-f990-4301-9776-6db9a033a068" />
<img width="49%" height="866" alt="image" src="https://github.com/user-attachments/assets/127be1b1-a24b-416b-b609-0a6ea27b039a" />
</div>

## Description
A simple 2d grid traveler with pygame to visualize traditional graph traversal algorithms:

- A* (L1 / L2 heuristics)
- (Dijkstra's) UCS
- Depth-First Search
- Breath-First Search

#### Controls
```bash
r - reset
w - toggle weighted graph (generates a new graph or turns weights off)
a - run Dijkstra's / UCS
m - run A* L1 heuristic
e - run A* L2 heuristic
b - run BFS
d - run DFS
```

## Requirements

#### Version:
```bash
Python3.13+
```

#### Venv:
Python virtual environment is recommended.

```bash
python -m venv .venv
python3.13 -m venv .venv   # Recommended
source .venv/bin/activate
```

#### Install:
```bash 
pip install -r requirements.txt
```

## Run
Inside your venv,
```bash 
python3 -m src.main 
```
