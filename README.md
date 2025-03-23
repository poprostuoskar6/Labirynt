# Labirynt (Maze Solver/Generator)

A Python project for generating and solving mazes. Includes algorithms for maze creation (e.g., recursive backtracking, Kruskal's) and pathfinding (e.g., A*, DFS, BFS).

## Features

- **Maze Generation**: Create mazes using different algorithms.
- **Maze Solving**: Solve mazes with pathfinding algorithms.
- **Visualization**: Visualize maze generation and solving in real-time (e.g., using Pygame or Tkinter).
- **Customization**: Adjust maze size, algorithm speed, and display options.

## Requirements

- Python 3.x
- Dependencies (if applicable):
  ```bash
  pip install pygame numpy
Usage
Running the Project
Clone the repository:

bash
Copy
git clone https://github.com/poprostuoskar6/Labirynt.git
cd Labirynt
Run the main script:

bash
Copy
python3 main.py
Command-Line Options
--size <rows>x<cols>: Set maze dimensions (e.g., --size 20x20).

--algorithm <name>: Choose generation/solving algorithm (e.g., --algorithm dfs).

--visualize: Enable real-time visualization.

Example
Generate a 15x15 maze using recursive backtracking and solve it with A*:

bash
Copy
python3 main.py --size 15x15 --algorithm recursive_backtracking --solve a_star --visualize
Project Structure
Copy
Labirynt/
├── main.py            # Main entry point
├── maze_generator.py  # Maze generation logic
├── maze_solver.py     # Pathfinding algorithms
├── visualizer.py      # Visualization module
└── README.md          # Documentation
Contributing
Feel free to submit issues or pull requests. To add a new algorithm:

Fork the repository.

Implement your algorithm in a new module.

Update main.py to include your method.

License
This project is licensed under the MIT License. See LICENSE for details.

Copy

---

If you provide details about your specific implementation (e.g., algorithms used, dependencies, or features), I can refine this further. Let me know!
