import openpyxl
import re
from openpyxl import load_workbook, Workbook

class ExcelSheet:
    
    def __init__(self, sheet_name):

        self.sheet_name = sheet_name

if __name__ == '__main__':

    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    print(sheet.sheet_name)
