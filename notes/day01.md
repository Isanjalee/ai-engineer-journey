# Day 01 — Environment Setup & Project Initialization (AI Engineer Journey)

## Date
1st January 2026

---

## Purpose of This Document

This file documents **everything done on Day 01**, including:
- Software installations
- Exact versions
- Folder structure
- Commands executed
- Errors faced and how they were fixed
- Configuration steps
- Git initialization

This level of detail is intentional so that:
- Anyone can reproduce my setup
- I can track my growth accurately
- My learning journey remains transparent and professional

---

## Goal of Day 01

- Set up a clean AI development environment
- Configure Python with a virtual environment
- Configure VS Code correctly
- Fix Jupyter/Notebook issues
- Initialize Git and start daily logging

---

## System Information

- Operating System: Windows 10 / Windows 11
- Architecture: 64-bit
- Terminal Used:
  - Command Prompt
  - VS Code Integrated Terminal
- Editor:
  - Visual Studio Code (latest stable)

---

## Software Installed (With Versions)

### 1. Python Installation

- Python Version Installed: **Python 3.14.2**
- Installation Source: Official Python installer
- Installation Options:
  - ✅ “Add python.exe to PATH” enabled
- Python installed system-wide

Verification command:
```bash
python --version

Notes:
- Python was successfully installed and accessible from the command line
- PATH configuration worked correctly

## Visual Studio Code Setup & Usage (Detailed)

### Opening the Project in VS Code

Steps followed:

1. Opened **Visual Studio Code**
2. Clicked **File → Open Folder**
3. Selected:

```
C:\Dev\ai-engineer-journey
```

4. Clicked **Select Folder**
5. Trusted the folder when prompted

Result:

* Project root opened in VS Code
* All subfolders (`day01_python_basics`, `notes`, `projects`) visible in Explorer

---

### VS Code Terminal Usage

Steps:

1. Opened terminal using:

   * Menu: **Terminal → New Terminal**
   * OR shortcut: `Ctrl + ``

Terminal used:

* VS Code Integrated Terminal (Command Prompt)

Verified working directory:

```bash
cd
```

Confirmed current path:

```
C:\Dev\ai-engineer-journey
```

---

### Installing VS Code Extensions (Inside VS Code)

Steps:

1. Clicked **Extensions** icon (left sidebar)
2. Installed the following extensions:

Installed Extensions:

* **Python** (Microsoft)
* **Pylance**
* **Jupyter**
* **GitLens** (optional)

Purpose:

* Python → Python language support
* Pylance → IntelliSense & type checking
* Jupyter → Notebook & cell execution
* GitLens → Git history & file tracking

---

### Selecting Python Interpreter in VS Code

Steps followed:

1. Pressed `Ctrl + Shift + P`
2. Typed:

```
Python: Select Interpreter
```

3. Selected interpreter:

```
.venv\Scripts\python.exe
```

Result:

* VS Code linked to project virtual environment
* Python execution isolated to `.venv`

---

### Running Python Files in VS Code

Steps:

1. Opened file:

```
day01_python_basics/test.py
```

2. Ran the file using:

   * Terminal command:

     ```bash
     python day01_python_basics\test.py
     ```
   * OR VS Code Run button

Observed Output:

* Python executable path showed `.venv`
* Program executed successfully

---

### Notebook / Python Cell Execution in VS Code

Issue faced:

* Notebook cells did not run initially

Error shown:

```
Running cells with '.venv (Python 3.14.2)' requires the notebook package
```

Fix steps:

1. Activated virtual environment
2. Installed missing packages:

```bash
pip install notebook jupyter ipykernel
```

3. Restarted VS Code
4. Reopened project folder

Result:

* Notebook cells executed correctly
* VS Code fully integrated with Jupyter

---

## Git Installation & Verification

- Git for Windows (latest version)
- Installed using official Git installer
- Default editor selected as Visual Studio Code

Verification command:
```bash
git --version

### Git Integration Inside VS Code

Steps:

1. Opened **Source Control** panel in VS Code
2. Verified file changes visually
3. Used terminal for Git commands:

```bash
git status
git add .
git commit -m "Day 01: environment setup and project initialization"
```

Result:

* Files tracked correctly
* Commit created successfully

---


