import requests
from .config import ACCESS_TOKEN, STATUS_DATE_S, STATUS_DATE_E, FILES_PATH


def get_smfl_id(acc_num: str, city: str) -> int:
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    url = f"http://smfl.kuzro.ru/api/accounts/?acc_num={acc_num}&city={city}&status_date={STATUS_DATE_S},{STATUS_DATE_E}"

    response = requests.request("GET", url, headers=headers)
    #print(response.text, "\t", response.status_code)
    data = response.json()
    #print(data)

    return data["results"][0]["id"]


def upload_file(file_name: str, id: str) -> int:
    files = [("file", (file_name, open(FILES_PATH + file_name, "rb"), "text/plain"))]
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    payload = {"model_type": "accountpackage", "model_id": id, "file_name": file_name}
    url = "http://smfl.kuzro.ru/api/files/"

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.status_code


def get_current_status(id : str) -> int:
    pass


def change_current_status(id: str, new_status: str) -> bool:
    pass
