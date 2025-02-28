import os

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, task):
        """Add a task to the list."""
        try:
            if not task.strip():
                print("Error: Task cannot be empty.")
                return
            
            self.tasks.append(task.strip())
            print(f"Task added: {task}")
            self.save_tasks()
        except Exception as e:
            print(f"Error adding task: {e}")
    
    def remove_task(self, task_number):
        """Remove a task by its number."""
        try:
            if not self.tasks:
                print("No tasks to remove.")
                return
            
            index = int(task_number) - 1
            
            if index < 0 or index >= len(self.tasks):
                print(f"Error: Please enter a number between 1 and {len(self.tasks)}.")
                return
            
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task}")
            self.save_tasks()
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"Error removing task: {e}")
    
    def view_tasks(self):
        """Display all tasks in the list."""
        try:
            if not self.tasks:
                print("No tasks in the list.")
                return
            
            print("\n===== TASK LIST =====")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("=====================")
        except Exception as e:
            print(f"Error viewing tasks: {e}")
    
    def save_tasks(self):
        """Save tasks to the file."""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task}\n")
        except PermissionError:
            print(f"Error: No permission to write to file '{self.filename}'.")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from the file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.tasks = [line.strip() for line in file if line.strip()]
            else:
                self.tasks = []
        except PermissionError:
            print(f"Error: No permission to read file '{self.filename}'.")
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []

def main():
    """Main function to run the task manager."""
    task_manager = TaskManager()
    
    while True:
        print("\n===== SIMPLE TASK MANAGER =====")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            task_manager.add_task(task)
            
        elif choice == '2':
            task_manager.view_tasks()
            
        elif choice == '3':
            task_manager.view_tasks()
            if task_manager.tasks:
                task_number = input("Enter task number to remove: ")
                task_manager.remove_task(task_number)
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
