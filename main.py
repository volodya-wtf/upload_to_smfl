from os import stat
from core.api_requests import get_smfl_id, upload_file
from core.csv_parsers import get_data_from_registry


def main():
    code_acc, city, file_name, status = get_data_from_registry()
    for c_a, c, f_n in zip(code_acc, city, file_name):
        id = get_smfl_id(c_a, c)
        status_code = upload_file(f_n, id)
        print(id, ";", c_a, ";", c, ";", f_n, ";", status_code)





if __name__ == "__main__":
    main()
