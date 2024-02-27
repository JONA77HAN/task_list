# Función para mostrar la lista de tareas
def show_tasks(tasks):
    print("Lista de tareas:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Función para agregar una nueva tarea
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Tarea '{new_task}' agregada.")

# Función para eliminar una tarea
def delete_task(tasks, task_index):
    if task_index >= 0 and task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Tarea '{deleted_task}' eliminada.")
    else:
        print("Índice de tarea fuera de rango.")

# Lista de tareas
tasks = []

# Loop principal para interactuar con el usuario
while True:
    print("\n1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    choice = input("Ingrese su opción: ")
    
    if choice == '1':
        if tasks:
            show_tasks(tasks)
        else:
            print("No hay tareas.")
    elif choice == '2':
        new_task = input("Ingrese la nueva tarea: ")
        add_task(tasks, new_task)
    elif choice == '3':
        if tasks:
            task_index = int(input("Ingrese el número de tarea que desea eliminar: ")) - 1
            delete_task(tasks, task_index)
        else:
            print("No hay tareas para eliminar.")
    elif choice == '4':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elija nuevamente.")
