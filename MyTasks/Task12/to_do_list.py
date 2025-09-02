from pathlib import Path

# Define the workspace and file path
workspace = Path("Task12")
file_path = workspace / "task.txt"
file_path

tasks=[]

# Function to get participant's task with validation
def add_task(task):
    while True:
        try:
            if task == "":  # task cannot be empty
                print("Sorry, task cannot be empty")
            elif task.isdigit():  # task cannot be a number
                print("task cannot be a number")         
            else:
              return tasks.append(task) 

             # Valid task
        except ValueError:
            print("\ntask cannot be a number")
        except Exception:
            print("\nAn Unexpected Error Occured")


def remove_task(task):
    while True:
        try:
            if task in tasks:
                tasks.remove(task)
            else:
                ("You don't have this task set")    

        except Exception as e :  
            print(f"An unexpected error occured: {e}")  

def view_task():
         while True:
             try:
                if tasks:
                    print("Your Tasks:")
                    for my_task, task in enumerate(tasks, 1): 
                        print(f'{my_task}. {task}')
                else:
                    print("No tasks in your list!")         
             except Exception as e :  
                print(f"An unexpected error occured: {e}") 



# def save_task(file_path,tasks):
#     if file_path.exists():
#        with open(file_path, "a", newline="", encoding="utf-8") as f:
#          for task in tasks:
#              f.write(task + "\n")
        
#     else:   
#         print(f"File {file_path} doesn't exist, Creating it now!")  
#         with open(tasks, "w", encoding="utf-8") as f:
#             f.write(tasks)
#     print("Tasks sucesfully added")


def view_tasks(file_path):
    print("\nReading Text file:")
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("No Tasks found yet.")                 

def main():
    while True:
        try:
            print("Welcome to Raiza To-do list App")
            print("1. Add Task")                     
            print("2. Remove Task")
            print("3. View Task")
            print("4. Mark Task as complete") 
            print("5. Exit App")

            choice = int(input("Enter a number between 1-4 to select your choice: "))

            # Validate choice using range
            if choice not in range(1, 6):
                print("Invalid choice! Please choose a number between 1 and 4.")
                continue

            if choice == 1:
                task = input("Enter your task: ").strip()
                add_task(task)
                # save_task(file_path, tasks)
            elif choice == 2:
                task = input("Enter task to remove: ")
                remove_task(task)
            elif choice == 3:
                view_task()
                break
            
            elif choice == 5:
                print("Exiting app... ")    
                break        

  # Ask if user wants to add another task
            again = input("Do you want to add another task? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thanks for using the app. Goodbye!")
                break

        except ValueError:
            print("Error: Please enter a valid number!")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    main()