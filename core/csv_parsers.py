import pandas as pd

from .config import REGISTRY_PATH, CODE_ACC, CITY, FILE_NAME, STATUS


def get_data_from_registry(registry_path: str = REGISTRY_PATH) -> list:
    df = pd.read_csv(registry_path, sep=';', header=0, dtype=str) 
    
    code_acc = df[CODE_ACC]
    city = df[CITY]
    file_name = df[FILE_NAME]
    status = df[STATUS]

    return [list(code_acc), list(city), list(file_name), list(status)]
