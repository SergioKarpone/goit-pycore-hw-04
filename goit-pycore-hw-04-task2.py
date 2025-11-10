def get_cats_info(path):
    
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо пробіли та символи нового рядка
                line = line.strip()
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                # Розділяємо рядок через кому
                parts = line.split(',')
                
                # Перевіряємо наявність даних
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0].strip(),
                        "name": parts[1].strip(),
                        "age": parts[2].strip()
                    }
                    cats_list.append(cat_info)
                else:
                    print(f"Неправильний формат рядка: {line}")
                    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except PermissionError:
        print(f"Немає прав доступу до файлу '{path}'.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []
    
    return cats_list


if __name__ == "__main__":
    
    cats_info = get_cats_info('C:/Users/serge/cats_file.txt')
    
    print("\nІнформація про котів:")
    for cat in cats_info:
        print(cat)