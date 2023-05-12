from .base.abstract_converter import FileConverter
import json
import xml.etree.ElementTree as ET


def build_xml_structure(parent_element, data):
    if isinstance(data, dict):
        for key, value in data.items():
            child_element = ET.SubElement(parent_element, key)
            build_xml_structure(child_element, value)
    elif isinstance(data, list):
        for item in data:
            child_element = ET.SubElement(parent_element, 'item')
            build_xml_structure(child_element, item)
    else:
        parent_element.text = str(data)


class JsonToXml(FileConverter):
    async def convert(from_path, to_path) -> None:
        with open(from_path, 'r') as file:
            json_data = json.load(file)

            root_element = ET.Element('root')
            build_xml_structure(root_element, json_data)
            xml_tree = ET.ElementTree(root_element)

            with open(to_path, 'wb') as file:
                xml_tree.write(file, encoding='utf-8', xml_declaration=True)
