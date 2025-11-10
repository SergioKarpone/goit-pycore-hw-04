import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory_structure(path: Path, prefix: str = "", is_last: bool = True):

    try:
        # Визначаємо символи для дерева
        connector = "    "
        
        if path.is_dir():
            # Виводимо ім'я директорії синім кольором
            print(f"{prefix}{connector}{Fore.BLUE} {path.name}/{Style.RESET_ALL}")
            
            # Отримуємо список всіх елементів у директорії
            try:
                items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
            except PermissionError:
                print(f"{prefix}{connector}{Fore.RED}[Немає доступу]{Style.RESET_ALL}")
                return
            
            # Визначаємо новий префікс для вкладених елементів
            new_prefix = prefix + connector
            
            # Рекурсивно обробляємо кожен елемент
            for index, item in enumerate(items):
                is_last_item = (index == len(items) - 1)
                visualize_directory_structure(item, new_prefix, is_last_item)
        else:
            # Виводимо ім'я файлу зеленим кольором
            print(f"{prefix}{connector}{Fore.GREEN} {path.name}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{prefix}{connector}{Fore.RED}[Помилка: {e}]{Style.RESET_ALL}")


def main():

    # Перевірка наявності аргументів командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Не вказано шлях до директорії!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Використання: python hw03.py /шлях/до/директорії{Style.RESET_ALL}")
        sys.exit(1)
    
    # Отримання шляху з аргументів командного рядка
    directory_path = sys.argv[1]
    path = Path(directory_path)
    
    # Перевірка існування шляху
    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує!{Style.RESET_ALL}")
        sys.exit(1)
    
    # Перевірка, що це директорія
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{directory_path}' не є директорією!{Style.RESET_ALL}")
        sys.exit(1)
    
    # Виведення заголовка
    print(f"\n{Fore.CYAN}Структура директорії: {Fore.YELLOW}{path.absolute()}{Style.RESET_ALL}\n")
    
    # Виведення кореневої директорії
    print(f"{Fore.BLUE} {path.name}/{Style.RESET_ALL}")
    
    # Отримання та сортування елементів
    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        
        # Візуалізація структури
        for index, item in enumerate(items):
            is_last = (index == len(items) - 1)
            visualize_directory_structure(item, "", is_last)
            
    except PermissionError:
        print(f"{Fore.RED}Помилка: Немає прав доступу до директорії!{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Помилка при читанні директорії: {e}{Style.RESET_ALL}")
        sys.exit(1)
    

if __name__ == "__main__":
    main()