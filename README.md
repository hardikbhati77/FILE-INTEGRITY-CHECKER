# FILE-INTEGRITY-CHECKER
![Image](https://github.com/user-attachments/assets/a50618f0-b81c-4e51-8cb7-56e3e8b008f9)
Name: HARDIK BHATI
Company: CODETECH IT SOLUTION
Domain : CYBERSECURITY & ETHICAL HACKING
Duration : 6 WEEKS
Mentor : Neela Santhosh kumar

# 🔐 File Integrity Checker

This Python script monitors changes in files within a specified folder by calculating and comparing their SHA-256 hash values.

## 🧩 Features
- Detects **modified**, **new**, and **deleted** files.
- Uses secure **SHA-256** hashing.
- Logs results to the terminal (and optionally to a `.txt` log file).
- Stores hash values in a JSON file for future comparison.

## 🛠️ Requirements
- Python 3.6+
- No external libraries needed (uses built-in modules: `os`, `hashlib`, `json`)

## 🚀 How to Use

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/file-integrity-checker.git
   cd file-integrity-checker
2. Set the target folder:
Edit the FOLDER_TO_MONITOR variable in the script with the path you want to monitor:
FOLDER_TO_MONITOR = "path/to/your/folder"
