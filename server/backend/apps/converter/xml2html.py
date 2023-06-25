from .base.abstract_converter import FileConverter
import re


class XmlToHtml(FileConverter):
    async def convert(from_path, to_path) -> None:
        # Read XML data from the input file
        with open(from_path, 'r') as file:
            xml_data = file.read()

        # Extract the table headers from the XML data
        headers = list(set(re.findall(r'<([^>\s/]+)', xml_data)))

        # Extract the table rows from the XML data
        rows = re.findall(r'<book[^>]*>(.*?)</book>', xml_data, re.DOTALL)

        # Create the HTML table structure
        html_table = '<html><head>\n'
        html_table += '\t<meta charset="UTF-8">\n'
        html_table += '\t<title>XML To HTML</title>\n'
        html_table += '</head>\n<body>\n'
        html_table += '\t<table border="1">\n'

        # Add the table headers
        html_table += '\t\t<thead>\n'
        html_table += '\t\t\t<tr>\n'
        for header in headers:
            html_table += f'\t\t\t\t<th>{header}</th>\n'
        html_table += '\t\t\t</tr>\n'
        html_table += '\t\t</thead>\n'

        # Add the table rows
        html_table += '\t\t<tbody>\n'
        for row in rows:
            html_table += '\t\t\t<tr>\n'
            values = re.findall(r'<([^>\s/]+)>(.*?)</\1>', row)
            for header in headers:
                value = next((val for tag, val in values if tag == header), '')
                html_table += f'\t\t\t\t<td>{value}</td>\n'
            html_table += '\t\t\t</tr>\n'
        html_table += '\t\t</tbody>\n'

        # Close the HTML table structure
        html_table += '\t</table>\n'
        html_table += '</body></html>\n'

        # Write the HTML table to the output file
        with open(to_path, 'w') as file:
            file.write(html_table)
