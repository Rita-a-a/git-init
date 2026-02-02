# Создаём файл todo.py с базовым кодом
cat > todo.py << 'EOF'
# To-Do List Application
tasks = []

def main():
    print("Добро пожаловать в To-Do List!")
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            task = input("Введите задачу: ")
            tasks.append(task)
            print(f"Задача '{task}' добавлена!")
        elif choice == "2":
            if not tasks:
                print("Список задач пуст")
            else:
                print("Ваши задачи:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
EOF
