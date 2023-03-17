
from .base.abstract_converter import FileConverter
from pdf2docx import parse


class Pdf2Word(FileConverter):

    async def convert(from_path, to_path) -> None:
        parse(from_path, to_path)
