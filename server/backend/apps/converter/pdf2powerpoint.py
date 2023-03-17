
from .base.abstract_converter import FileConverter
import pdf2pptx

class Pdf2Pptx(FileConverter):

    async def convert(from_path, to_path) -> None:
      pdf2pptx.convert_pdf2pptx(from_path, to_path, 300, 0, None, True)
