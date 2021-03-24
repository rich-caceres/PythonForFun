import openpyxl
import re
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet

if __name__ == '__main__':
    
    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    colDiction= {}
    #following method will return column letters
    
    '''write a loop to allow the user to choose the total amount of cols
    that they would like to enter to dynamically chose the total amount of cols.
    May need to create a tuple to do this! Look into Tuples again.
    '''
    for i in range(1,10):
        colDiction['col{0}'.format(i)] = sheet.returnCols()
    print(sheet.sheet_name)
