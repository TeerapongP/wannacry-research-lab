# WannaCry PoC Simulator 🖥️🔒

This repository contains a **Proof of Concept (PoC) Simulation** of **WannaCry Ransomware** behavior for **Cybersecurity education and research purposes only**.  
It simulates the key components of WannaCry, including **SMBv1 vulnerability scanning (MS17-010)**, **file encryption simulation**, **ransom note display**, and **kill-switch domain logic** — all in a **safe and controlled environment**.

> ⚠️ **Disclaimer:** This is a simulation project for educational purposes. No real malware payloads are included. The code does not contain any harmful exploits or propagation logic.

---

## 🧱 Project Structure

| Folder/File | Description |
|-------------|-------------|
| `SMB_Scanner/` | PoC code to simulate scanning for SMBv1 vulnerability (MS17-010) |
| `Encryption_Simulator/` | Python scripts simulating WannaCry's AES + RSA hybrid encryption (safe, non-destructive) |
| `Ransom_Note/` | Simulation of WannaCry ransom note GUI (Tkinter-based) |
| `killswitch.py` | Logic to simulate WannaCry's kill-switch domain check |
| `README.md` | This file |
| `requirements.txt` | Python dependencies |

---

## 🧪 Features
- **MS17-010 Vulnerability Scanner Simulation**
- **AES File Encryption Simulation (Safe Mode)**
- **Fake Ransom Note Pop-up (Tkinter)**
- **Kill Switch Domain Logic**
- **Sandbox-safe — does NOT spread or cause real damage**

---

## 🚀 How to Run (Simulation Environment)
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/wannacry-poc-simulator.git
    cd wannacry-poc-simulator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the simulation modules:
    - **SMB Scanner Simulation:**
      ```bash
      python SMB_Scanner/scanner.py
      ```
    - **Encryption Simulation:**
      ```bash
      python Encryption_Simulator/encryptor.py
      ```
    - **Ransom Note Simulation:**
      ```bash
      python Ransom_Note/ransom_note.py
      ```
    - **Kill Switch Check:**
      ```bash
      python killswitch.py
      ```

---

## 📚 Educational Objective
- Demonstrate **Cyber Kill Chain stages** using WannaCry case study
- Understand ransomware behavior in a **safe lab simulation**
- Visualize the impact of **patch management and kill-switch mechanisms**
- Provide students with hands-on **PoC demonstration tools**

---

## ⚠️ Legal & Ethical Notice
- This project is for **academic cybersecurity research only**.
- It is strictly prohibited to use any part of this project for malicious intent.
- You are responsible for ensuring that all activities comply with local laws and institutional guidelines.

---

## 👨‍💻 Author
Developed by [Your Name] for Master's Degree Cybersecurity Project  
Supervised by [Instructor Name], [University Name]

---

## 📄 License
MIT License — Educational Use Only
