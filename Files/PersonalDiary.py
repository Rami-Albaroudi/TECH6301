import os
import datetime
import time

class DiaryApp:
    def __init__(self, diary_file="my_diary.txt"):
        """Initialize the diary application with the specified diary file."""
        self.diary_file = diary_file
        self.ensure_diary_exists()
    
    def ensure_diary_exists(self):
        """Make sure the diary file exists, create it if it doesn't."""
        try:
            if not os.path.exists(self.diary_file):
                with open(self.diary_file, 'w') as f:
                    f.write("=== My Personal Diary ===\n\n")
                print(f"Created new diary file: {self.diary_file}")
        except PermissionError:
            print("Error: You don't have permission to create a diary file in this location.")
        except Exception as e:
            print(f"Unexpected error creating diary file: {e}")
    
    def add_entry(self, add_timestamp=True):
        """Add a new entry to the diary with optional timestamp."""
        try:
            print("\n=== New Diary Entry ===")
            print("(Type your entry and press Enter twice to finish)")
            
            lines = []
            while True:
                line = input()
                if line == "" and (not lines or lines[-1] == ""):
                    break
                lines.append(line)
            
            entry_text = "\n".join(lines).strip()
            
            if not entry_text:
                print("Empty entry not saved.")
                return
            
            with open(self.diary_file, 'a') as f:
                if add_timestamp:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"\n\n[{timestamp}]\n")
                else:
                    f.write("\n\n")
                f.write(entry_text)
            
            print("Entry saved successfully!")
            
        except PermissionError:
            print("Error: You don't have permission to write to the diary file.")
        except IOError as e:
            print(f"Error writing to diary: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def view_entries(self):
        """View all previous diary entries."""
        try:
            if not os.path.exists(self.diary_file):
                print("No diary entries found.")
                return
            
            with open(self.diary_file, 'r') as f:
                content = f.read()
            
            if content.strip() == "=== My Personal Diary ===":
                print("No entries yet. Add your first entry!")
                return
                
            print("\n=== Your Diary Entries ===\n")
            print(content)
            
        except PermissionError:
            print("Error: You don't have permission to read the diary file.")
        except FileNotFoundError:
            print("Diary file not found.")
        except Exception as e:
            print(f"Unexpected error reading diary: {e}")

def main():
    """Main function to run the diary application."""
    diary = DiaryApp()
    
    while True:
        print("\n=== Personal Diary ===")
        print("1. Add new entry")
        print("2. Add new entry (without timestamp)")
        print("3. View all entries")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            diary.add_entry(add_timestamp=True)
        elif choice == '2':
            diary.add_entry(add_timestamp=False)
        elif choice == '3':
            diary.view_entries()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
