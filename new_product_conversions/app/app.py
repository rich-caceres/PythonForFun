import openpyxl
import re
import sys
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet

if __name__ == '__main__':
    
    while True:
        try:
            sheet = ExcelSheet(input('Please enter excel sheet name:\n'), input('Enter Sku Identification to add to beginning of SKU'), input('Enter starting row'))
            workbook = openpyxl.load_workbook(sheet.sheet_name)
        except:
            answer = input("This workbook was not found! try again, Enter Q to quit the program, otherwise hit enter to continue.")
            if(answer == 'Q'):
                sys.exit('You have quit the program!')
        
    colDiction= {}
    #following loop will return a dictionary of column letters
    numOfCols = sheet.totalCols()
    for i in range(1,numOfCols):
        colDiction['col{0}'.format(i)] = sheet.returnCols()

    for i in range(1,numOfCols):
        print(colDiction['col{0}'.format(i)])
        
    print(sheet.sheet_name)
