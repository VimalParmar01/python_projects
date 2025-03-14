# Secure File Sharing System

## Overview
This project is a **Secure File Sharing System** built using **Python** and **Tkinter** for the GUI. It provides encryption, decryption, and file integrity verification using **AES (Advanced Encryption Standard), RSA (Rivest-Shamir-Adleman), and SHA-256**.

## Features
- **Generate RSA Keys**: Generates a public-private key pair for secure encryption.
- **Encrypt File**: Uses AES encryption with a randomly generated key, which is then encrypted using RSA.
- **Decrypt File**: Decrypts the AES key using the RSA private key and decrypts the file.
- **Verify File Integrity**: Computes and displays the SHA-256 hash of a file.
- **Graphical User Interface**: Simple and user-friendly Tkinter-based UI.

## Technologies Used
- **Python** (Programming Language)
- **Tkinter** (GUI Framework)
- **PyCryptodome** (Cryptography Library)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/secure-file-sharing.git
   cd secure-file-sharing
   ```
2. Install the required dependencies:
   ```bash
   pip install pycryptodome
   ```
3. Run the application:
   ```bash
   python secure_file_sharing.py
   ```

## Usage
1. **Generate RSA Keys**: Click the **"Generate RSA Keys"** button to create `private.pem` and `public.pem`.
2. **Encrypt a File**:
   - Select a file to encrypt.
   - Choose the recipient's **public key**.
   - The encrypted file (`filename.enc`) and AES key (`filename.enc.key`) will be created.
3. **Decrypt a File**:
   - Select the encrypted file and corresponding AES key.
   - Choose the **private key**.
   - The decrypted file will be saved.
4. **Verify File Integrity**: Select a file to view its SHA-256 hash.

## File Structure
```
secure-file-sharing/
│── secure_file_sharing.py  # Main Python script
│── private.pem             # Private RSA Key (Generated)
│── public.pem              # Public RSA Key (Generated)
│── example.enc             # Encrypted file (Generated)
│── example.enc.key         # Encrypted AES Key (Generated)
│── README.md               # Project Documentation
```

## Security Considerations
- Always **keep your private key safe**.
- Do not share the **AES key file** publicly.
- Use strong passwords for key storage if required.

## License
This project is **open-source** and available under the **MIT License**.

## Author
- **Your Name**
- **Email: your.email@example.com**
- **GitHub: [your-github-profile](https://github.com/your-github-profile)**

---
Feel free to contribute or suggest improvements!

