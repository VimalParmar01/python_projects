import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Generate RSA keys for secure key exchange
def generate_rsa_keys():
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key.export_key())
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key.export_key())
    messagebox.showinfo("Success", "RSA keys generated: private.pem and public.pem")

# Encrypt file using AES
def encrypt_file():
    input_file = filedialog.askopenfilename(title="Select file to encrypt")
    if not input_file:
        return
    output_file = input_file + ".enc"
    public_key_path = filedialog.askopenfilename(title="Select recipient's public key")
    if not public_key_path:
        return

    key = get_random_bytes(16)
    cipher_aes = AES.new(key, AES.MODE_EAX)

    with open(input_file, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    with open(output_file, 'wb') as f:
        f.write(cipher_aes.nonce)
        f.write(tag)
        f.write(ciphertext)

    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(key)

    with open(output_file + ".key", 'wb') as f:
        f.write(encrypted_key)

    messagebox.showinfo("Success", f"File encrypted and saved to {output_file} with key {output_file}.key")

# Decrypt file using AES and RSA key
def decrypt_file():
    input_file = filedialog.askopenfilename(title="Select encrypted file")
    if not input_file:
        return
    key_file = filedialog.askopenfilename(title="Select AES key file")
    if not key_file:
        return
    private_key_path = filedialog.askopenfilename(title="Select your private key")
    if not private_key_path:
        return

    output_file = input_file.replace(".enc", "_decrypted")

    with open(key_file, 'rb') as f:
        encrypted_key = f.read()

    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    key = cipher_rsa.decrypt(encrypted_key)

    with open(input_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher_aes = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    with open(output_file, 'wb') as f:
        f.write(data)

    messagebox.showinfo("Success", f"File decrypted and saved to {output_file}")

# Generate SHA256 hash of a file
def generate_file_hash():
    file_path = filedialog.askopenfilename(title="Select file to verify")
    if not file_path:
        return
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    messagebox.showinfo("File Hash", f"SHA256 Hash: {sha256_hash.hexdigest()}")

# Create GUI window
root = tk.Tk()
root.title("Secure File Sharing System")
root.geometry("400x400")

# GUI Buttons
tk.Label(root, text="Secure File Sharing System", font=("Arial", 16)).pack(pady=10)

btn_generate_keys = tk.Button(root, text="Generate RSA Keys", command=generate_rsa_keys)
btn_generate_keys.pack(pady=5)

btn_encrypt = tk.Button(root, text="Encrypt File", command=encrypt_file)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt File", command=decrypt_file)
btn_decrypt.pack(pady=5)

btn_hash = tk.Button(root, text="Verify File Integrity", command=generate_file_hash)
btn_hash.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=5)

# Run the GUI
root.mainloop()
