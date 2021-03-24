import openpyxl
import re
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet

if __name__ == '__main__':
    
    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    colDiction= {}
    #following loop will return a dictionary of column letters
    numOfCols = sheet.totalCols()
    for i in range(1,numOfCols):
        colDiction['col{0}'.format(i)] = sheet.returnCols()
    print(sheet.sheet_name)
