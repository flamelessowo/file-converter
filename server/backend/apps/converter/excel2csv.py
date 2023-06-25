from .base.abstract_converter import FileConverter
import openpyxl
import csv

class ExcelToCsv(FileConverter):
    async def convert(from_path, to_path) -> None:
        # Open the Excel file
      workbook = openpyxl.load_workbook(from_path)

      # Get the active sheet
      sheet = workbook.active

      # Read the data from the Excel sheet
      data = []
      for row in sheet.iter_rows(values_only=True):
          data.append(row)

      # Write the data to a CSV file
      with open(to_path, 'w', newline='') as csv_file:
          csv_writer = csv.writer(csv_file)
          csv_writer.writerows(data)
