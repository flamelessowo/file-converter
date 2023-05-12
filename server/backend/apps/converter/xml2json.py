from .base.abstract_converter import FileConverter
import xml.etree.ElementTree as ET
import json


def parse_element(element):
    data = {}
    if element.text and element.text.strip():
        data['text'] = element.text.strip()
    for child in element:
        child_data = parse_element(child)
        if child.tag in data:
            if isinstance(data[child.tag], list):
                data[child.tag].append(child_data)
            else:
                data[child.tag] = [data[child.tag], child_data]
        else:
            data[child.tag] = child_data
    return data


class XmlToJson(FileConverter):
    async def convert(from_path, to_path) -> None:
        tree = ET.parse(from_path)
        root = tree.getroot()

        data = {}
        data[root.tag] = parse_element(root)

        with open(to_path, 'w') as file:
            json.dump(data, file, indent=4)
