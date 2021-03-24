import openpyxl
import re
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet

if __name__ == '__main__':
    
    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))

    #following method will return column letters
    col = sheet.returnCols()
    '''write a while loop to allow the user to choose the total amount of cols
    that they would like to enter to dynamically chose the total amount of cols.
    May need to create a tuple to do this! Look into Tuples again.
    '''
    
    print(sheet.sheet_name)
