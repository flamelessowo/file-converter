
from .base.abstract_converter import FileConverter
from docx2pdf import convert


class Word2Pdf(FileConverter):

    async def convert(from_path, to_path) -> None:
        convert(from_path, to_path)
