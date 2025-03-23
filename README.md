File Encryption and Decryption Script

This script provides functionality to encrypt and decrypt files using a password. It uses the cryptography library to handle encryption and decryption processes.

Features

- Encrypt a File: Encrypts a given file using a password.
- Decrypt a File: Decrypts a given file using a password.
- Dictionary Attack: Attempts to decrypt a file using a dictionary of passwords.

Requirements

- Python 3.x
- cryptography library (install via pip install cryptography)

Usage

Help

To display the usage instructions, run:

python3 skrypt.py --help

Encrypt a File

To encrypt a file, use the -s option followed by the input file, output file, and password:

python3 skrypt.py -s <input_file> <output_file> <password>

<input_file>: The file to be encrypted.
<output_file>: The name of the resulting encrypted file.
<password>: The password to use for encryption.

Example:

python3 skrypt.py -s plik.txt zaszyfrowany.txt mojehaslo

Decrypt a File Using a Dictionary

To decrypt a file using a dictionary of passwords, use the -o option followed by the input file, output file, and dictionary file:

python3 skrypt.py -o <input_file> <output_file> <dictionary_file>

<input_file>: The file to be decrypted.
<output_file>: The name of the resulting decrypted file.
<dictionary_file>: The path to the dictionary file containing passwords.

Example:

python3 skrypt.py -o zaszyfrowany.txt odszyfrowany.txt slownik.txt

Functions

- generuj_klucz(haslo: str, sol: bytes) -> bytes: Generates an encryption key based on a password and salt.
- szyfruj_plik(plik_wejsciowy: str, plik_wyjsciowy: str, haslo: str) -> None: Encrypts a file using a given password.
- odszyfruj_plik(plik_wejsciowy: str, plik_wyjsciowy: str, haslo: str) -> None: Decrypts a file using a given password.
- odszyfruj_plik_slownik(plik_wejsciowy: str, plik_wyjsciowy: str, slownik: str) -> bool: Attempts to decrypt a file using a dictionary of passwords.
- wyswietl_pomoc(): Displays the usage instructions.
