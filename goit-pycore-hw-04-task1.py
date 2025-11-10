def total_salary(path):

    try:
        # Ініціалізація змінних
        total = 0
        count = 0
        
        # Використовуємо with та зчитуємо у 'utf-8'
        with open(path, 'r', encoding='utf-8') as file:
            # Обробляємо файл по рядках
            for line in file:
                # Видаляємо пробіли та символи нового рядка
                line = line.strip()
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                try:
                    # Розділяємо ім'я та зарплату через кому
                    parts = line.split(',')
                    
                    # Перевіряємо, чи рядок має правильний формат (2 частини)
                    if len(parts) != 2:
                        print(f"Некоректний формат рядка: {line}")
                        continue
                    
                    # Прибираємо пробіли і конвертуємо в число
                    salary = float(parts[1].strip())
                    
                    # Додаємо зарплату до загальної суми і збільшуємо лічільник
                    total += salary
                    count += 1
                    
                except (ValueError, IndexError) as e:
                    # Якщо невдала конвертція в число аоб інша помилка
                    print(f"Не вдалося обробити рядок '{line}': {e}")
                    continue
        
        # Перевіряємо, чи знайдено хоча б один коректний запис
        if count == 0:
            print("Файл не містить коректних записів про зарплати")
            return (0, 0)
        
        # Обчислюємо середню зарплату
        average = total / count
        
        # Повертаємо результат у вигляді кортежу
        return (total, average)
    
    except FileNotFoundError:
        # Якщо файл не знайдено
        print(f"Файл '{path}' не знайдено")
        raise
    
    except Exception as e:
        # Обробка будь-яких інших непередбачених помилок
        print(f"Помилка при читанні файлу: {e}")
        raise


def main():
    
    test_file = 'C:/Users/serge/salary_file.txt'
    
    # Викликаємо функцію для аналізу файлу
    try:
        total, average = total_salary(test_file)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        
    except FileNotFoundError:
        print("Не вдалося знайти файл з даними")
        
    except Exception as e:
        print(f"Виникла помилка: {e}")
    
if __name__ == "__main__":
    main()