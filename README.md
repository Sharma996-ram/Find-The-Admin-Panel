
# Finder The Admin Panel 

This tool is designed to help find the admin panel of websites by scanning for known subdirectories. It automatically checks a list of predefined subdirectories to identify the admin panel location.

## Features
- Scans websites to find possible admin panel links.
- Displays working admin panel URLs from a list of known subdirectories.
- Simple and easy-to-use interface.

## Requirements
- Python 2.7 or higher.
- Access to the terminal on your system.

## Installation

### Windows
1. Install Python (if not already installed) from [here](https://www.python.org/downloads/).
2. Open Command Prompt (`cmd`).
3. If the script is not already on your system, download it using `curl` or `wget`:
   - Using `wget`:
     ```bash
     wget https://github.com/DV64/Finder-The-Admin-Panel.py
     ```
   - Using `curl`:
     ```bash
     curl -O https://github.com/DV64/Finder-The-Admin-Panel.py
     ```
4. Navigate to the directory where the script is located:
   ```bash
   cd path\to\your\script
   ```
5. Run the script using Python:
   ```bash
   python Finder_The_Admin_Panel.py
   ```

### Linux
1. Ensure Python is installed on your system. If not, install it using:
   ```bash
   sudo apt install python
   ```
2. If the script is not on your system, download it using `wget` or `curl`:
   - Using `wget`:
     ```bash
     wget https://github.com/DV64/Finder-The-Admin-Panel.py
     ```
   - Using `curl`:
     ```bash
     curl -O https://github.com/DV64/Finder-The-Admin-Panel.py
     ```
3. Navigate to the directory where the script is located:
   ```bash
   cd /path/to/your/script
   ```
4. Make the script executable:
   ```bash
   chmod +x Finder_The_Admin_Panel.py
   ```
5. Run the script:
   ```bash
   ./Finder_The_Admin_Panel.py
   ```

### Android (Using Termux)
1. Install Python in Termux:
   ```bash
   pkg install python
   ```
2. Download the script using `wget` or any method you prefer:
   - Using `wget`:
     ```bash
     wget https://github.com/DV64/Finder-The-Admin-Panel.py
     ```
3. Run the script:
   ```bash
   python Finder_The_Admin_Panel.py
   ```

## How to Use
1. Ensure the `link.txt` file is present in the same directory as the script. This file should contain a list of known subdirectories (one per line).
2. When prompted, enter the website URL (e.g., `example.com` or `www.example.com`).
3. The script will check various subdirectories and output the links to the console if they are accessible.

## Example
```
Enter Site Name 
(ex : example.com or www.example.com ): example.com

Available links:
Link =>  http://example.com/admin
Link =>  http://example.com/wp-admin
```
