# Add, Update, and Delete tasks
tasks = []
menu_option = False

def create_task():
  task = {
    "name": input("Nome: "),
    "id": len(tasks) + 1,
    "done": False
  }

  tasks.append(task)

def list_tasks():
  for task in tasks:
    is_done = "x" if task["done"] else  "-"
    print("[", task["id"], "]: ", is_done, ":", task["name"])

def remove_task(id):
  for task in tasks:
    if (task["id"] == id):
      tasks.remove(task)
  
while True:
  menu_option = input("(n/N) para nova tarefa / (l/L) para ver todas / (task_id) para detalhes: ")

  create_task_menu_option = menu_option == "n" or menu_option == "N"
  list_task_menu_option = menu_option == "l" or menu_option == "L"

  if (create_task_menu_option):
    create_task()

  if (list_task_menu_option):
    list_tasks()

  # if (menu_option != create_task or menu_option != list_task_menu_option):
  #   remove_task(menu_option)

# ---

# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress