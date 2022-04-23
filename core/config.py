from starlette.config import Config


config = Config(".env")

# Доступ к api
ACCESS_TOKEN = config("ACCESS_TOKEN")

# Даты перехода в статус пакета Лицевого счета
# /api/accounts/
STATUS_DATE_S = config("STATUS_DATE_S")
STATUS_DATE_E = config("STATUS_DATE_E")

# Относительный путь до реестра
REGISTRY_PATH = config("REGISTRY_PATH")

# Относительный путь до папки с файлами
FILES_PATH = config("FILES_PATH")

# Поля реестра
CODE_ACC = config("CODE_ACC")
CITY = config("CITY")
FILE_NAME = config("FILE_NAME")
STATUS = config("STATUS")
