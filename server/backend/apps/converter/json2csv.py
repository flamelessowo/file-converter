from .base.abstract_converter import FileConverter
import json
import csv


class JsonToCsv(FileConverter):
    async def convert(from_path, to_path) -> None:
        with open(from_path, 'r') as file:
            data = json.load(file)
        fields = list(data[0].keys())

        with open(to_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
