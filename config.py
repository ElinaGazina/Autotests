import os
from pathlib import Path
from dotenv import load_dotenv

# Получаем значение переменной окружения "ENV"
env = os.environ.get('ENV', 'test')

# Определяем путь к файлу .env
# Проверяет, существует ли файл
path = os.path.join(os.path.dirname(__file__), '.env')
env_path = Path('.') / f'{path}.{env}'
if not env_path.exists():
    print('.env файл не существует')

# Загружаем значения переменных окружения из файла .env
load_dotenv(dotenv_path=env_path)


# Yotube url
URL_YOUTUBE = os.getenv('URL_YOUTUBE')




