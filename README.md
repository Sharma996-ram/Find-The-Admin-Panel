# Find-The-Admin-Panel

## Description

**Find-The-Admin-Panel** is a Python tool designed to identify potential admin panel URLs for websites. The tool checks common admin panel paths and returns the results, helping security researchers and developers find potential vulnerabilities in websites. This tool is essential for identifying web applications' admin login interfaces, which are typically hidden from the public.

## Features

- Scan websites for common admin panel paths.
- Display results for found and missing admin panels.
- Customizable input for website URLs.
- Handles both sub-links and full admin panel URLs.
- Shows the number of successful and failed attempts.

---

## Installation

### Prerequisites

Ensure Python 3.x is installed on your system. Follow the specific installation steps for your operating system.

---

### Installing on Windows

1. **Download Python**:  
   - Download Python 3.x from [python.org](https://www.python.org/downloads/).  
   - During installation, check the box **"Add Python to PATH"**.

2. **Clone the Repository**:  
   Open the Command Prompt and run:
   ```bash
   git clone https://github.com/DV64/Find-The-Admin-Panel.git
   cd Find-The-Admin-Panel
   ```

3. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Tool**:  
   ```bash
   python Finder.py
   ```

---

### Installing on Linux

1. **Install Python**:  
   Most Linux distributions come with Python pre-installed. Verify using:
   ```bash
   python3 --version
   ```
   If Python is not installed, use the package manager to install it:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```

2. **Clone the Repository**:  
   Open a terminal and run:
   ```bash
   git clone https://github.com/DV64/Find-The-Admin-Panel.git
   cd Find-The-Admin-Panel
   ```

3. **Install Required Libraries**:
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run the Tool**:
   ```bash
   python3 Finder.py
   ```

---

### Installing on Android (Using Termux)

1. **Install Termux**:  
   Download Termux from [F-Droid](https://f-droid.org/) or the Google Play Store.

2. **Install Python**:  
   Open Termux and run:
   ```bash
   pkg update
   pkg install python git
   ```

3. **Clone the Repository**:
   ```bash
   git clone https://github.com/DV64/Find-The-Admin-Panel.git
   cd Find-The-Admin-Panel
   ```

4. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Tool**:
   ```bash
   python Finder.py
   ```

---

## Usage

1. Run the tool:
   ```bash
   python Finder.py
   ```

2. Enter the base URL of the website when prompted (e.g., `example.com`).
3. If sub-links are available, the script will automatically check them. If not, it will prompt you to add sub-links.
4. The tool will scan the website for potential admin panel URLs.
5. Results are displayed in the terminal, showing the status of each admin panel path.

At the end of the scan, a summary will show:
- The total number of links scanned.
- The number of successful admin panels found.
- The number of failed attempts.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

