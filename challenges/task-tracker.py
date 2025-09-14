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

def get_task_by_id(id):
  task_id = input(": ")
  print("----")

  task_id = int(id)
  finded_task = {}

  for task in tasks:
    if (task["id"] == task_id):
      finded_task = task
  return finded_task

def remove_task(task):
  for i in tasks:
    if (i["id"] == task["id"]):
      tasks.remove(task)

def list_tasks():
  print("----")
  for i in tasks:
    is_done = "✅" if i["done"] else  "❌"
    print(i["id"], ".", is_done, ":", i["name"])

  task = get_task_by_id(i["id"])
  task_action = input(f"R para remover / U para atualizar ({task["name"]}): ")
  print("----")

  if (task_action == "r" or task_action == "R"):
    remove_task(task)

  if (task_action == "u" or task_action == "U"):
    update_task(task["id"])

def remove_task(id):
  for task in tasks:
    if (task["id"] == id):
      tasks.remove(task)

def update_task(id):
  for i in tasks:
    if (i["id"] == id):
      new_task_name = input(f"Digite o novo nome da tarefa, padrão ({i["name"]}): ") or i["name"]
      i["name"] = new_task_name

      new_task_done = input(f"V para dar checked / F para dar unchecked") or i["done"]
      i["done"] = True if  new_task_done == "v" else  False

while True:
  menu_option = input("(N) para nova tarefa / (L) para ver todas: ")

  create_task_menu_option = menu_option == "n" or menu_option == "N"
  list_task_menu_option = menu_option == "l" or menu_option == "L"

  if (create_task_menu_option):
    create_task()

  if (list_task_menu_option):
    list_tasks()

# ---

# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress