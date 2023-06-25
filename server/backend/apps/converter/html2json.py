from .base.abstract_converter import FileConverter


def html_to_json_algo(from_path):
    with open(from_path, 'r') as file:
        html = file.read()
    stack = []
    json_data = {}
    current_dict = json_data

    i = 0
    while i < len(html):
        # Спочатку перевіряєм на відкритий тег
        if html[i] == '<':
            closing_index = html.find('>', i)
            tag = html[i + 1:closing_index]

            # Перевірка на закритий тег
            if tag.startswith('/'):
                if len(stack) > 1:
                    stack.pop()
                    current_dict = stack[-1]
                    i = closing_index + 1
                    continue

                tag_parts = tag.split()
                tag_name = tag_parts[0]
                attributes = {}
                if len(tag_parts) > 1:
                    attributes = dict(attr.split('=') for attr in tag_parts[1:])

                # Створюєм хеш мапу для даного тегу
                new_dict = {'tag': tag_name, 'attributes': attributes, 'children': []}

                current_dict['children'].append(new_dict)

                current_dict = new_dict
                stack.append(new_dict)

                i = closing_index + 1
            else:
                closing_index = html.find('<', i)
                if closing_index == -1:
                    closing_index = len(html)
                text_content = html[i:closing_index].strip()
                if text_content:
                    current_dict['text'] = text_content

                i = closing_index

        return json_data


def build_json_string(data):
    json_string = "{\n"
    for key, value in data.items():
        if key == 'children':
            json_string += '    "children": [\n'
            for child in value:
                json_string += '        {}\n'.format(build_json_string(child))
            json_string += '    ]\n'
        else:
            json_string += '    "{}": "{}",\n'.format(key, value)
    json_string += '}'
    return json_string


class HTMLtojsonAlgo(FileConverter):

    async def convert(from_path, to_path) -> None:
        json_file = html_to_json_algo(from_path)
        json_string = build_json_string(json_file)
        with open(to_path, 'w') as file:
            file.write(json_string)
