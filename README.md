# FolderOrganizer.exe
Your Digital Maid 😉🧹 

Tired of messy download folders? This Python script is your personal digital assistant! It automatically sorts your files into neat categories, so your system can do its own chores, not you. Crafted by YogaWilanda, for the clean addict (and the happily lazy!)

# Folder Organizer: Your Digital Maid 😉🧹

Tired of messy download folders? This Python script is your personal digital assistant! It automatically sorts your files into neat categories, so your system can do its own chores, not you. Crafted by **YogaWilanda**, for the clean addict (and the happily lazy!), with a little help from Gemini. Features a welcoming animated startup!

---

## ✨ Features

* **Automated Sorting:** Automatically scans a specified folder and organizes files based on their extensions.
* **Categorized Folders:** Creates dedicated subfolders for various file types (Images, Videos, Documents, Applications, etc.).
* **"Others" Category:** Intelligently handles files with unrecognized extensions by moving them to an `others` folder.
* **Interactive Welcome:** Greets you with a persistent, friendly banner and a fun, animated emoji loading sequence.
* **Simple Console Interface:** Easy to use directly from your command prompt.
* **Error Handling:** Basic error handling for file operations (e.g., file in use, already exists).

---

## 🚀 Getting Started

Follow these steps to get your Folder Organizer up and running.

### Prerequisites

You need **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/yogawilanda/FolderOrganizer.exe.git)
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd YourRepoName # Replace YourRepoName with the name of your repository folder
    ```
3.  **Run the script:**
    ```bash
    python your_script_name.py # Replace 'your_script_name.py' with the actual name of your main Python file (e.g., folder_organizer.py)
    ```

### Customizing the Target Folder

By default, the script is set to organize `C:/Users/{username}/Downloads`. You can easily change this to any folder you wish by editing the `target_folder` variable directly in the Python script:

```python
# main execution flow of the program
if __name__ == "__main__":
    # ...
    target_folder = "C:/Users/{username}/Downloads" # <--- Change this path!
    # ...
