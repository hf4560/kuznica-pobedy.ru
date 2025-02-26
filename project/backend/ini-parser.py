import configparser

# Создаем объект парсера
config = configparser.ConfigParser()

# Читаем файл
config.read('config.ini')

# Получаем значения из секций
db_host = config['database']['host']
db_port = config['database'].getint('port')  # Преобразуем в целое число
debug_mode = config['settings'].getboolean('debug')  # Преобразуем в логическое значение

print(f"Database host: {db_host}")
print(f"Database port: {db_port}")
print(f"Debug mode: {debug_mode}")