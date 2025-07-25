import socket
import sys

def scan_target(ip, port=445):
    print(f"[*] Scanning {ip}:{port} for SMBv1 (MS17-010) vulnerability...")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Port 445 is OPEN on {ip}")
            # --- Simulated Check for SMBv1 Enabled ---
            print(f"[!] Simulating SMBv1 Detection on {ip}... SMBv1 appears to be ENABLED (Simulated)")
            print(f"[!] {ip} is POTENTIALLY VULNERABLE to MS17-010 (EternalBlue) (Simulation Only)\n")
        else:
            print(f"[-] Port 445 is CLOSED on {ip}\n")

        sock.close()

    except socket.error as e:
        print(f"[-] Could not connect to {ip}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python MS17-010_Scanner.py <Target-IP>")
        sys.exit(1)

    target_ip = sys.argv[1]
    scan_target(target_ip)

if __name__ == "__main__":
    main()
