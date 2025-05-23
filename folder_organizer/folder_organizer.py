# os package is used to access operating system functionality such as command line arguments
import os
# shutil package is used for file operations
import shutil
# time package is used for introducing delays in animation
import time

# --- ADD THESE IMPORTS FOR GUI FOLDER SELECTION ---
import tkinter as tk
from tkinter import filedialog
# --------------------------------------------------

def clear_screen():
    """Clears the console screen based on the operating system."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def loading_animation():
    """
    Displays a simple loading animation on a single line, without clearing the screen.
    Uses carriage return to overwrite the line.
    """
    loading_emojis = ['😎', '😉', '😄']
    
    # Loop for a bit longer to give a good loading feel
    for _ in range(5): 
        for emoji in loading_emojis:
            # \r moves cursor to the beginning of the line
            # end='' prevents a newline, keeping subsequent prints on the same line
            # flush=True ensures the output is shown immediately
            # Added spaces after emoji to clear any previous longer text if necessary
            print(f"Loading... {emoji}   \r", end='', flush=True) 
            time.sleep(0.3) # Adjusted sleep to make emoji changes more noticeable
    
    # After the animation, clear the loading message from the line
    # and then print a newline so subsequent output starts on a fresh line.
    print(" " * 20 + "\r", end='', flush=True) # Overwrite the "Loading..." text with spaces
    print("\n") # Move to the next line for subsequent output


def print_banner():
    """
    Displays the introductory banner for the Folder Organizer.
    This version focuses on a static introductory message that remains on screen.
    """
    # Introductory decoration
    print("================================================================")
    print("           Welcome to the Automated Folder Organizer!           ")
    print("          Let your system do its own chores, not you.           ")
    print("            From YogaWilanda, for the clean addict.             ") 
    print("================================================================")
    # No time.sleep here, as the loading animation will provide the necessary pause.
    # No clear_screen() here, as per your request for the intro to persist.

# =============================================================================
# Original Folder Organizer Script
# =============================================================================

kategorisasi_folder = {
    "image": ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp", "ico", "htm"],
    "video": ["mp4", "mkv", "webm", "flv", "avi", "wmv", "mov", "mpg", "mpeg", "3gp"],
    "audio": ["mp3", "wav", "flac", "m4a", "wma", "aac", "ogg"],
    "document": ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "csv"],
    "app": ["exe", "msi", "jar", "apk", 'msix'],
    "others": ["pixil"], 
    "code": ["dart", "json", "sql"],
    "compressed": ["rar", "zip"],
}

def organisir_file(target_folder):
    """
    Organizes files in the specified target_folder into subfolders based on their extensions.
    Returns True if any files were moved, False otherwise.
    """
    print("\nStarting file organization...\n")
    found_files_to_organize = False # Flag to track if any files were moved

    # Iterate through each item in the target folder
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)
        
        # Check if the item is a file (and not a directory)
        if os.path.isfile(file_path):
            # Get the file extension and convert to lowercase for consistent matching
            ext = filename.split(".")[-1].lower()
            moved = False # Flag to check if the current file has been moved

            # Iterate through defined categories and their extensions
            for kategori, ekstensi in kategorisasi_folder.items():
                if ext in ekstensi:
                    # Construct the destination folder path
                    folder = os.path.join(target_folder, kategori)
                    
                    # Create the destination folder if it doesn't exist
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    
                    try:
                        # Attempt to move the file
                        shutil.move(file_path, os.path.join(folder, filename))
                        print(f"Moved: {filename} -> {folder}")
                        found_files_to_organize = True # Mark that at least one file was moved
                        moved = True # Mark that this file was moved
                        break # Exit the inner loop once the file is categorized and moved
                    except shutil.Error as e:
                        # Handle specific shutil errors (e.g., destination file already exists, permission denied)
                        print(f"Error moving {filename}: {e} (File might already exist or be in use)")
                        moved = True # Consider it handled, don't try "others" for this file
                        break
                    except Exception as e:
                        # Handle any other unexpected errors during file movement
                        print(f"An unexpected error occurred moving {filename}: {e}")
                        moved = True
                        break
            
            # If the file was not moved into any specific category, move it to "others"
            # This ensures files not matching any specific category are still organized
            if not moved:
                other_folder = os.path.join(target_folder, "others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                try:
                    shutil.move(file_path, os.path.join(other_folder, filename))
                    print(f"Moved: {filename} -> {other_folder} (categorized as others)")
                    found_files_to_organize = True
                except shutil.Error as e:
                    print(f"Error moving {filename} to 'others': {e} (File might already exist or be in use)")
                except Exception as e:
                    print(f"An unexpected error occurred moving {filename} to 'others': {e}")
    
    return found_files_to_organize

# =============================================================================
# Main execution flow of the program
# =============================================================================
if __name__ == "__main__":
    print_banner() 
    print("") # Blank line after banner
    loading_animation()

    # --- GUI FOLDER SELECTION LOGIC ---
    # Create a Tkinter root window, but hide it
    root = tk.Tk()
    root.withdraw() 

    print("Please select the folder you want to organize in the dialog box that appears...")
    # Open the directory selection dialog
    target_folder = filedialog.askdirectory(
        title="Which folder you want to organize?",
        initialdir=os.path.expanduser("~"), # Start in the user's home directory
    ) 

    # Destroy the Tkinter root window after selection to clean up resources
    root.destroy()

    # Check if the user selected a folder or cancelled the dialog
    if not target_folder: # If target_folder is an empty string (user cancelled)
        print("\nFolder selection cancelled. Exiting the program. 👋")
    else:
        # Proceed with the rest of your program's logic
        # Check if the target folder exists and is a directory (it should, as filedialog ensures valid selection)
        if not os.path.exists(target_folder): # This check is mostly for robustness, filedialog usually returns existing paths
            print(f"\nError: Target folder '{target_folder}' does not exist. This shouldn't happen with GUI selection.")
        elif not os.path.isdir(target_folder): # Again, mostly for robustness
            print(f"\nError: '{target_folder}' is not a valid directory. This shouldn't happen with GUI selection.")
        else:
            # Check if the folder is empty or has no files to organize initially
            if not os.listdir(target_folder):
                print("=====================================")
                print("Folder sudah tidak ada file yang bisa diorganisir.")
                print("Program tidak mendeteksi file yang perlu diorganisir.")
                print("=====================================")
            else:
                print(f"Mengorganisir file di folder: {target_folder}...")
                has_files_to_organize = organisir_file(target_folder)
                
                print("\n=====================================")
                if has_files_to_organize:
                    print("Organisir file selesai.")
                    print(f"File yang ada di folder: {target_folder} telah diorganisir.")
                else:
                    print("Tidak ada file baru yang perlu diorganisir.")
                print("=====================================")

    # Keep the console window open until the user presses a key
    input("\nTekan tombol apapun untuk keluar... 👋")