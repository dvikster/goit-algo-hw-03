import os
import shutil
import argparse

def sort_and_copy_files(source_dir, dest_dir):
    try:
        # Перевірка, чи існує директорія призначення, якщо ні — створюємо
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Перебираємо всі елементи у вихідній директорії
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            if os.path.isdir(item_path):
                sort_and_copy_files(item_path, dest_dir)
            # Якщо елемент є файлом, копіюємо його
            elif os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1].lstrip(".").lower() or "no_extension"
                target_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(target_dir, exist_ok=True)  # Створюємо піддиректорію для розширення, якщо вона не існує
                
                target_file_path = os.path.join(target_dir, item)
                shutil.copy2(item_path, target_file_path)  # Копіюємо файл з метаданими
                print(f"Файл '{item}' скопійовано до '{target_dir}'")
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    # Налаштування парсингу аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширеннями.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument(
        "dest_dir", nargs="?", default="dist",
        help="Шлях до директорії призначення (за замовчуванням 'dist')"
    )
    args = parser.parse_args()
    
    # Перевірка, чи існує вихідна директорія
    if not os.path.exists(args.source_dir):
        print(f"Помилка: Вихідна директорія '{args.source_dir}' не існує.")
        return
    
    # Запуск функції сортування та копіювання
    sort_and_copy_files(args.source_dir, args.dest_dir)
    print(f"Файли успішно скопійовані та відсортовані в '{args.dest_dir}'.")

if __name__ == "__main__":
    main()

# python task-3/task3-1.py task-3/folder-1 task-3/folder-2
# python task3-1.py /шлях-до/вихідної-директорії /шлях-до/директорії-призначення