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
  - `pip install pygame numpy`

## Usage

### Running the Project

Clone the repository:

```bash
git clone https://github.com/poprostuoskar6/Labirynt.git
cd Labirynt
Run the main script:

Kopiuj
python3 main.py
Command-Line Options
--size x: Set maze dimensions (e.g., --size 20x20).
--algorithm: Choose generation/solving algorithm (e.g., --algorithm dfs).
--visualize: Enable real-time visualization.
Example
Generate a 15x15 maze using recursive backtracking and solve it with A*:

Kopiuj
python3 main.py --size 15x15 --algorithm recursive_backtracking --solve a_star --visualize
Project Structure
Kopiuj
Labirynt/
├── main.py # Main entry point
├── maze_generator.py # Maze generation logic
├── maze_solver.py # Pathfinding algorithms
├── visualizer.py # Visualization module
└── README.md # Documentation
Contributing
Feel free to submit issues or pull requests. To add a new algorithm:

Fork the repository.
Implement your algorithm in a new module.
Update main.py to include your method.
License
This project is licensed under the MIT License. See LICENSE for details.

File Encryption and Decryption Script
This script provides functionality to encrypt and decrypt files using a password. It uses the cryptography library to handle encryption and decryption processes.

Features
Encrypt a File: Encrypts a given file using a password.
Decrypt a File: Decrypts a given file using a password.
Dictionary Attack: Attempts to decrypt a file using a dictionary of passwords.
Requirements
Python 3.x
cryptography library (install via pip install cryptography)
Usage
Help
To display the usage instructions, run:

Kopiuj
python3 skrypt.py --help
Encrypt a File
To encrypt a file, use the -s option followed by the input file, output file, and password:

Kopiuj
python3 skrypt.py -s <input_file> <output_file> <password>
<input_file>: The file to be encrypted.
<output_file>: The name of the resulting encrypted file.
<password>: The password to use for encryption.
Example:

Kopiuj
python3 skrypt.py -s plik.txt zaszyfrowany.txt mojehaslo
Decrypt a File Using a Dictionary
To decrypt a file using a dictionary of passwords, use the -o option followed by the input file, output file, and dictionary file:

Kopiuj
python3 skrypt.py -o <input_file> <output_file> <dictionary_file>
<input_file>: The file to be decrypted.
<output_file>: The name of the resulting decrypted file.
<dictionary_file>: The path to the dictionary file containing passwords.
Example:

Kopiuj
python3 skrypt.py -o zaszyfrowany.txt odszyfrowany.txt slownik.txt
Functions
generuj_klucz(haslo: str, sol: bytes) -> bytes: Generates an encryption key based on a password and salt.
szyfruj_plik(plik_wejsciowy: str, plik_wyjsciowy: str, haslo: str) -> None: Encrypts a file using a given password.
odszyfruj_plik(plik_wejsciowy: str, plik_wyjsciowy: str, haslo: str) -> None: Decrypts a file using a given password.
odszyfruj_plik_slownik(plik_wejsciowy: str, plik_wyjsciowy: str, slownik: str) -> bool: Attempts to decrypt a file using a dictionary of passwords.
wyswietl_pomoc(): Displays the usage instructions.
