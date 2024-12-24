import sqlite3
import hashlib
import random
import string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    return data + b" " * (16 - len(data) % 16)


def encrypt_password(password, key):
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    encrypted = cipher.encrypt(pad(password.encode()))
    return base64.b64encode(encrypted).decode()


def decrypt_password(encrypted, key):
    cipher = AES.new(key, AES.MODE_ECB)
    
    decrypted = cipher.decrypt(base64.b64decode(encrypted)).strip()
    
    return decrypted.decode()

def hash_master_key(master_key):
    return hashlib.sha256(master_key.encode()).digest()

def init_db():
    conn = sqlite3.connect("passwords_save.db")
    
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            account_name TEXT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_password(account_name, username, password, key):
    encrypted_password = encrypt_password(password, key)
    conn = sqlite3.connect("passwords_save.db")
    
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO passwords (account_name, username, password) VALUES (?, ?, ?)",
                   (account_name, username, encrypted_password))
    conn.commit()
    
    conn.close()
    
    print("password added successfully!")

def view_passwords(key):
    conn = sqlite3.connect("passwords_save.db")
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT account_name, username, password FROM passwords")
    
    rows = cursor.fetchall()
    
    conn.close()

    print("\nStored Passwords:")
    for row in rows:
        account_name, username, encrypted_password = row
        
        decrypted_password = decrypt_password(encrypted_password, key)
        
        print(f"Account: {account_name}, Username: {username}, Password: {decrypted_password}")

def generate_password(length=12, use_special_chars=True):
    
    chars = string.ascii_letters + string.digits
    
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Welcome to the Password Manager!")
    init_db()

    master_key = input("Enter your Master key:")
    
    hashed_key = hash_master_key(master_key)

    while True:
        print("\nOptions:")
        print("1. Add a new password")
        print("2. view stored Passwords")
        print("3. Generate a password")
        print("4. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            account_name = input("Enter the account name:")
            username = input("Enter the username: ")
            password = input("Enter the password (leave blank to auto-generate):")
            if not password:
                password = generate_password()
                
                print(f"Generated password: {password}")
            add_password(account_name, username, password, hashed_key)

        elif choice == "2":
            view_passwords(hashed_key)

        elif choice == "3":
            try:
                length = int(input("Enter the desired password length (e.g., 12):"))
                use_special_chars = input("Include special characters? (yes/no):").strip().lower() == 'yes'
                
                print(f"Generated password: {generate_password(length, use_special_chars)}")
                
            except ValueError:
                print("Invalid input. Please enter a number for the length.")

        elif choice == "4":
            print("Exiting the Password Manager. goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
