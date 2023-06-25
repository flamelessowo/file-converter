from .base.abstract_converter import FileConverter
import csv
from openpyxl import Workbook

class CsvToExcel(FileConverter):
    async def convert(from_path, to_path) -> None:
        with open(from_path, 'r') as csv_file:
          csv_reader = csv.reader(csv_file)
          data = list(csv_reader)

      # Create a new Excel workbook
        workbook = Workbook()
        sheet = workbook.active

        # Write the data from CSV to the Excel sheet
        for row in data:
            sheet.append(row)

        # Save the workbook as an Excel file
        workbook.save(to_path)
