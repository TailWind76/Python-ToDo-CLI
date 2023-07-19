def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Активные задачи:")
        for index, task in enumerate(tasks, 1):
            print(f"\033[32m{index}. {task}\033[0m")  # Зеленый цвет (32) и сброс форматирования (0)

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Задача '{new_task}' добавлена.")

def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Задача '{completed_task}' выполнена и удалена из списка.")
    else:
        print("Недопустимый индекс задачи.")

def main():
    tasks = []
    
    while True:
        print("\nВыберите действие:")
        print("1. Показать список задач")
        print("2. Добавить задачу")
        print("3. Завершить задачу")
        print("0. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Введите новую задачу: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Введите номер выполненной задачи: "))
            complete_task(tasks, task_index)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()