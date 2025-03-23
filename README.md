# File Encryption/Decryption Tool

A Python script for encrypting and decrypting files using AES encryption with Fernet. Supports password-based encryption and dictionary-based brute-force decryption.

## Features
- 🔒 **Encrypt files** with a password using PBKDF2 key derivation
- 🔓 **Decrypt files** with the correct password
- 🗝️ **Dictionary attack** to brute-force decrypt files using a list of potential passwords
- 🔐 Secure salt storage (saved with encrypted files for proper decryption)

## Installation
1. Ensure **Python 3.x** is installed.
2. Install the required library:
   ```bash
   pip install cryptography
Usage
Copy
python3 skrypt.py [OPTIONS] [ARGUMENTS]
Options
Option	Description
-h, --help	Show help message
-s	Encrypt a file
-o	Decrypt a file using a password dictionary
Examples
1. Encrypt a File

bash
Copy
python3 skrypt.py -s input.txt encrypted.txt "myStrongPassword"
Encrypts input.txt into encrypted.txt using the password "myStrongPassword".

2. Decrypt with a Password Dictionary

bash
Copy
python3 skrypt.py -o encrypted.txt decrypted.txt passwords.txt
Attempts to decrypt encrypted.txt using passwords from passwords.txt (one password per line).

Security Notes
🔑 Password Strength: Use a strong password for encryption. Weak passwords may be cracked by dictionary attacks.

🔧 PBKDF2: Key derivation uses 100,000 iterations of SHA-256 to slow brute-force attacks.

⚠️ Dictionary Files: For decryption (-o), ensure the dictionary file is a text file with one password per line (encoded in latin-1).

Contribution
Feel free to create issues and PRs (pull requests) to improve this tool - any help is appreciated!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Copy

This is the complete `README.md` file in the requested format. You can copy and paste it directly into your project.
