Password Manager with Encryption
This is a simple yet powerful Password Manager built with Python and SQLite that securely stores user credentials. It uses AES encryption to protect passwords, ensuring privacy and security. Additionally, it provides password generation and viewing functionalities, making it a complete solution for managing sensitive data.

Features
Secure Password Storage:
Encrypts passwords using AES (Advanced Encryption Standard) encryption before saving them in a local SQLite database.

Master Key Protection:
A master key is hashed with SHA-256 to derive a secure encryption key for encrypting and decrypting stored passwords.

Password Generation:
Easily generate strong, random passwords with options to include special characters.

View Stored Passwords:
Displays stored passwords in a decrypted format, only accessible with the correct master key.

Local Database:
Uses SQLite for efficient local storage of account information.

Add new passwords: Store account credentials with AES encryption.
View stored passwords: Retrieve and view decrypted credentials.
Generate secure passwords: Automatically generate strong passwords.
Exit the program: Close the password manager.
