import openpyxl
import re
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet

if __name__ == '__main__':

    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    print(sheet.sheet_name)
