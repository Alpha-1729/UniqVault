import json


class JsonReader:
    @staticmethod
    def read_from_file(file_path: str) -> dict:
        with open(file_path, "r") as file:
            return json.load(file)
