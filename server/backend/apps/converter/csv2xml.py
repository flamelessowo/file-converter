import csv
import xml.etree.ElementTree as ET
from .base.abstract_converter import FileConverter


class CsvToXml(FileConverter):

    async def convert(from_path, to_path) -> None:
        with open(from_path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            headers = next(csv_data)
            root = ET.Element('data')
            for row in csv_data:
                item = ET.SubElement(root, 'item')
                for idx, value in enumerate(row):
                    ET.SubElement(item, headers[idx]).text = value
        tree = ET.ElementTree(root)
        tree.write(to_path, encoding='utf-8', xml_declaration=True)
