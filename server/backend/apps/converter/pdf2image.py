
import fitz

from .base.abstract_converter import FileConverter


class Pdf2Image(FileConverter):

    async def convert(from_path, to_path) -> None:
        mat = fitz.Matrix(2.0, 2.0)
        doc = fitz.open(from_path)
        for page in doc:
            pix = page.get_pixmap(matrix=mat)
            pix.save(to_path)
