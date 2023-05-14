from bs4 import BeautifulSoup
from .base.abstract_converter import FileConverter


class HtmlToTxt(FileConverter):

    async def convert(from_path, to_path) -> None:
        with open(from_path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()
        with open(to_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
