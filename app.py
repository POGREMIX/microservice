import os
from flask import Flask, jsonify
from config import path


app = Flask(__name__)


@app.route('/api/meta', methods=['GET'])
def main():
    file_names = get_path_file_names()
    if len(file_names) == 0:
        return jsonify({"data": []})

    return jsonify({"data": get_files_meta(file_names)})


def get_path_file_names():
    try:
        return os.listdir(path=path)
    except FileNotFoundError as ex:
        print(ex)
        return []


def get_files_meta(file_names):
    item_list = []
    for name in file_names:
        item = {
            "name": name,
            "type": get_file_extension(name),
            "time": get_creation_time(name)
        }
        item_list.append(item)
    return item_list


def get_file_extension(name):
    parts = name.split(".")
    if len(parts) == 1:
        return "folder"
    else:
        return "file"


def get_creation_time(name):
    full_path = os.path.join(path, name)
    return round(os.path.getctime(full_path))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
