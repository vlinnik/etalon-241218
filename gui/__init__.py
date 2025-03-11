import os
import sys

# Получаем путь к каталогу, в котором находится текущий файл __init__.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Добавляем этот каталог к пути поиска модулей
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Теперь можно импортировать модули из этого каталога
# os.chdir(os.path.expanduser('~/.local'))