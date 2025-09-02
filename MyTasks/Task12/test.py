
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
              tasks.append(task) 
              print(f"{tasks}")
            break
             # Valid task
        except ValueError:
            print("\ntask cannot be a number")
        except Exception:
            print("\nAn Unexpected Error Occured")

add_task("E")            