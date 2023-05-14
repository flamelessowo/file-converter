from .base.abstract_converter import FileConverter
from docx import Document


class Word2Txt(FileConverter):
    async def convert(from_path, to_path) -> None:
        doc = Document(from_path)
        paragraphs = [p.text for p in doc.paragraphs]
        text = '\n'.join(paragraphs)

        with open(to_path, 'w', encoding='utf-8') as file:
            file.write(text)
