from .base.abstract_converter import FileConverter
import json
import csv


class CsvToJson(FileConverter):
    async def convert(from_path, to_path) -> None:
        data = []
        with open(from_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                item = {}
                for i in range(len(headers)):
                    item[headers[i]] = row[i]
                data.append(item)

        with open(to_path, 'w') as file:
            json.dump(data, file, indent=4)
