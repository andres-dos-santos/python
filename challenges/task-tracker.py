tasks = []

def create_task(task_name):
  task = {
    "name": task_name,
    "id": len(tasks) + 1,
    "done": False
  }

  tasks.append(task)

def get_task():
  task_id = input(": ")
  print("----")

  finded_task = {}

  for i in tasks:
    if (i["id"] == int(task_id)):
      finded_task = i

  return finded_task

def remove_task(task):
  for i in tasks:
    if (i["id"] == task["id"]):
      tasks.remove(task)

def get_all_tasks():
  print("----")
  for i in tasks:
    is_done = "✅" if i["done"] else  "❌"
    print(i["id"], ".", is_done, ":", i["name"])

def actions():
  get_all_tasks()

  task = get_task()
  
  task_action = input(f"({task["name"]}) R to remove / D to done / Press a new task name: ")
  print("----")

  remove_action = task_action == "r" or task_action == "R"
  done_action = task_action == "d" or task_action == "D"

  if (not remove_action and not done_action):
    task["name"] = task_action
  
  if (remove_action):
    remove_task(task["id"])

  if (done_action):
    task["done"] = True if task["done"] == False else  False

def remove_task(id):
  for task in tasks:
    if (task["id"] == id):
      tasks.remove(task)

print("L / para listar todas as tarefas")
print("")

while True:
  action = input(f"{len(tasks) + 1} [or Enter]: ")
  
  if (action == ""):
      actions()

  create_task(task_name = action)

# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress