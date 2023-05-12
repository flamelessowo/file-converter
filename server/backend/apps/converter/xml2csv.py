from .base.abstract_converter import FileConverter
import xml.etree.ElementTree as ET
import csv


def extract_data(element):
    data = {}
    if element.text:
        data[element.tag] = element.text.strip()
    for child in element:
        child_data = extract_data(child)
        if child.tag in data:
            if isinstance(data[child.tag], list):
                data[child.tag].append(child_data)
            else:
                data[child.tag] = [data[child.tag], child_data]
        else:
            data[child.tag] = child_data
    return data


class XmlToCsv(FileConverter):
    async def convert(from_path, to_path) -> None:
        tree = ET.parse(from_path)
        root = tree.getroot()

        # Extract data from XML
        data = []
        for item in root.findall('.//'):
            item_data = extract_data(item)
            data.append(item_data)

        # Flatten data and identify all unique keys
        all_keys = set()
        for item in data:
            all_keys.update(item.keys())

        # Write data to CSV
        with open(to_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(all_keys))
            writer.writeheader()
            for item in data:
                writer.writerow(item)
