
from fastapi import UploadFile
from typing import List
from .upload_service import UploadService

# region convertors imports
from ..pdf2word import Pdf2Word
from ..pdf2image import Pdf2Image
from ..pdf2powerpoint import Pdf2Pptx
from ..json2csv import JsonToCsv
from ..csv2json import CsvToJson
from ..xml2csv import XmlToCsv
from ..xml2json import XmlToJson
from ..json2xml import JsonToXml
from ..csv2xml import CsvToXml
from ..html2txt import HtmlToTxt
from ..word2pdf import Word2Pdf
from ..mp42mp3 import Mp4ToMp3
from ..mp42compress import Mp4ToCompress
from ..word2txt import Word2Txt
from ..html2json import HTMLtojsonAlgo
from ..csv2excel import CsvToExcel
from ..excel2csv import ExcelToCsv
from ..xml2html import XmlToHtml
# endregion

from ..base.abstract_converter import FileConverter
from helpers import get_file_paths_with_formats

CONVERTORS = {
    '.pdf': {
        '.docx': Pdf2Word,
        '.png': Pdf2Image,
        '.jpg': Pdf2Image,
        '.jpeg': Pdf2Image,
        '.pptx': Pdf2Pptx
    },
    '.json': {
        '.csv': JsonToCsv,
        '.xml': JsonToXml,
    },
    '.csv': {
        '.json': CsvToJson,
        '.xml': CsvToXml,
        '.xlsx': CsvToExcel
    },
    '.xlsx': {
        '.csv': ExcelToCsv
    },
    '.xml': {
        '.csv': XmlToCsv,
        '.json': XmlToJson,
        '.html': XmlToHtml
    },
    '.html': {
        '.txt': HtmlToTxt,
        '.json': HTMLtojsonAlgo
    },
    '.docx': {
        '.pdf': Word2Pdf,
        '.txt': Word2Txt,
    },
    '.mp4': {
        '.mp3': Mp4ToMp3,
        '.mp4': Mp4ToCompress
    }
}


class ConverterService:

    def __init__(self, files: List[UploadFile], folder_name: str, from_format: str, to_format: str) -> None:
        self.files = files
        self.folder_name = folder_name
        self.from_format = from_format
        self.to_format = to_format

        self.upload_service = UploadService(folder_name, files)

    def resolve_convertor(self) -> FileConverter:
        return CONVERTORS[self.from_format][self.to_format]

    async def convert(self):
        converted_filepaths: List[str] = []
        usr_path = await self.upload_service.create_user_folder()
        file_paths = get_file_paths_with_formats(
            self.files, self.to_format, usr_path)
        file_convertor = self.resolve_convertor()
        for file in self.files:
            await self.upload_service.upload_file(file, usr_path)

        for file_path in file_paths:
            await file_convertor.convert(file_path[0], file_path[1])
            converted_filepaths.append(file_path[1])

        zipped_files = await self.upload_service.zip_files(converted_filepaths)
        await self.upload_service.destroy_user_folder()
        return zipped_files
