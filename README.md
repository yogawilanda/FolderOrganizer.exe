# Folder Organizer: Your Digital Maid 😉🧹

Tired of messy download folders? This Python script is your personal digital assistant! It automatically sorts your files into neat categories, so your system can do its own chores, not you. Crafted by **YogaWilanda**, for the clean addict (and the happily lazy!). Features a welcoming animated startup!

---

## ✨ Features

* **Automated Sorting:** Automatically scans a selected folder and organizes files based on their extensions.
* **Categorized Folders:** Creates dedicated subfolders for various file types (Images, Videos, Documents, Applications, etc.).
* **"Others" Category:** Intelligently handles files with unrecognized extensions by moving them to an `others` folder.
* **Interactive Welcome:** Greets you with a persistent, friendly banner and a fun, animated emoji loading sequence.
* **Intuitive Folder Selection:** Uses a graphical interface (GUI) to let you easily choose the target folder with your mouse.
* **Simple Console Interface:** Easy to monitor progress directly from your command prompt.
* **Error Handling:** Basic error handling for file operations (e.g., file in use, already exists).

---

## 🚀 Getting Started

You can run this application in two ways: by downloading the standalone executable or by running the Python script directly.

### Option 1: Download & Run the Executable (Recommended for Windows)

This is the easiest way to use the Folder Organizer, as it doesn't require Python installation.

1.  **Download:** Go to the [**Releases section**](https://github.com/yogawilanda/FolderOrganizer.exe/releases) of this GitHub repository.
2.  Download the latest `folder_organizer.exe` file (e.g., `v.0.1.0-beta/folder_organizer.exe`).
3.  **Run:** Simply double-click the `folder_organizer.exe` file. A console window will open, and a folder selection dialog will appear.

### Option 2: Run from Python Source

If you prefer to run the script directly or want to explore the code:

#### Prerequisites

You need **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/downloads/). `tkinter` (for the GUI folder selection) is usually included with Python, but if you encounter issues on Linux, you might need to install it via your package manager (e.g., `sudo apt-get install python3-tk`).

#### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yogawilanda/FolderOrganizer.exe.git
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd FolderOrganizer.exe
    ```
3.  **Run the script:**
    ```bash
    python folder_organizer.py # Assuming your main script is named folder_organizer.py
    ```
    *(When running the script, a folder selection dialog will automatically pop up.)*

---

## 📂 File Categories

The organizer uses the following categories and file extensions:

```python
kategorisasi_folder = {
    "image": ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp", "ico", "htm"],
    "video": ["mp4", "mkv", "webm", "flv", "avi", "wmv", "mov", "mpg", "mpeg", "3gp"],
    "audio": ["mp3", "wav", "flac", "m4a", "wma", "aac", "ogg"],
    "document": ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "csv"],
    "app": ["exe", "msi", "jar", "apk", "msix"],
    "others": ["pixil"], 
    "code": ["dart", "json", "sql"],
    "compressed": ["rar", "zip"],
}
```

You can modify this dictionary directly in the `folder_organizer.py` script to add or change categories and extensions as needed!

---

## 📦 Building Your Own Executable (`.exe`)

For developers or those who want to build their own `.exe` from the source:

### Steps to Build:

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Navigate to your project's root directory** in your command prompt.
3.  **Run PyInstaller:**
    ```bash
    pyinstaller --onefile folder_organizer.py # Use the actual name of your main script
    ```
    Your `.exe` file will be found in the newly created `dist/` folder.

---

## 🙏 Credits

This project was crafted by **YogaWilanda**.

---

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
*(**Note:** You'll need to create a separate file named `LICENSE` in your repository's root directory and paste the MIT license text into it.)*

```
