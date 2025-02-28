import os
import json
from statistics import mean

class GradeTracker:
    def __init__(self, filename="grades.json"):
        """Initialize the grade tracker with the specified file."""
        self.filename = filename
        self.grades = self.load_grades()
    
    def load_grades(self):
        """Load grades from the file, or create a new grades dictionary if the file doesn't exist."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return json.load(file)
            else:
                return {}
        except json.JSONDecodeError:
            print("Error: Grade file is corrupted. Creating a new one.")
            return {}
        except PermissionError:
            print("Error: No permission to read the grades file.")
            return {}
        except Exception as e:
            print(f"Unexpected error loading grades: {e}")
            return {}
    
    def save_grades(self):
        """Save the grades dictionary to the file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.grades, file, indent=4)
            print("Grades saved successfully!")
        except PermissionError:
            print("Error: No permission to write to the grades file.")
        except Exception as e:
            print(f"Unexpected error saving grades: {e}")
    
    def add_grade(self):
        """Add a new grade for a subject."""
        print("\n=== Add New Grade ===")
        
        # Get subject name
        subject = input("Enter subject name: ").strip()
        if not subject:
            print("Subject name cannot be empty.")
            return
        
        # Get grade value with validation
        while True:
            grade_input = input(f"Enter grade for {subject} (0-100): ").strip()
            try:
                grade = float(grade_input)
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        
        # Initialize subject in dictionary if it doesn't exist
        if subject not in self.grades:
            self.grades[subject] = []
        
        # Add the grade
        self.grades[subject].append(grade)
        print(f"Grade {grade} added for {subject}.")
        
        # Save updated grades
        self.save_grades()
    
    def calculate_averages(self):
        """Calculate and return average grades for each subject and overall."""
        if not self.grades:
            return None, None
        
        subject_averages = {}
        all_grades = []
        
        for subject, grades in self.grades.items():
            if grades:  # Check if there are grades for this subject
                subject_avg = mean(grades)
                subject_averages[subject] = subject_avg
                all_grades.extend(grades)
        
        if all_grades:  # Check if there are any grades at all
            overall_average = mean(all_grades)
            return subject_averages, overall_average
        else:
            return {}, None
    
    def display_grades(self):
        """Display all grades and averages."""
        if not self.grades:
            print("\nNo grades found. Add some grades first.")
            return
        
        print("\n=== Your Grades ===")
        
        # Display grades for each subject
        for subject, grades in self.grades.items():
            if grades:  # Check if there are grades for this subject
                print(f"\n{subject}:")
                for i, grade in enumerate(grades, 1):
                    print(f"  Grade {i}: {grade}")
                subject_avg = mean(grades)
                print(f"  Average: {subject_avg:.2f}")
        
        # Display overall average
        subject_averages, overall_average = self.calculate_averages()
        if overall_average is not None:
            print(f"\nOverall Average: {overall_average:.2f}")
    
    def delete_subject(self):
        """Delete a subject and all its grades."""
        if not self.grades:
            print("\nNo grades found. Add some grades first.")
            return
        
        print("\n=== Delete Subject ===")
        print("Available subjects:")
        for i, subject in enumerate(self.grades.keys(), 1):
            print(f"{i}. {subject}")
        
        choice = input("\nEnter subject number to delete (or 0 to cancel): ")
        try:
            index = int(choice)
            if index == 0:
                print("Deletion cancelled.")
                return
            
            if 1 <= index <= len(self.grades):
                subject = list(self.grades.keys())[index-1]
                confirm = input(f"Are you sure you want to delete '{subject}'? (y/n): ").lower()
                if confirm == 'y':
                    del self.grades[subject]
                    print(f"Subject '{subject}' deleted.")
                    self.save_grades()
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid subject number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the grade tracker application."""
    tracker = GradeTracker()
    
    while True:
        print("\n=== Student Grade Tracker ===")
        print("1. Add a new grade")
        print("2. View all grades")
        print("3. Delete a subject")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            tracker.add_grade()
        elif choice == '2':
            tracker.display_grades()
        elif choice == '3':
            tracker.delete_subject()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
