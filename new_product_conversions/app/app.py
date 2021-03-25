import openpyxl
import re
import sys
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet

if __name__ == '__main__':

    wb = openpyxl.Workbook()
    ws = wb.active
    
    while True:
        try:
            sheet = ExcelSheet(input('Please enter excel sheet name:\n'), input('Enter Sku Identification to add to beginning of SKU:\n'), input('Enter starting row:\n'))
            workbook = openpyxl.load_workbook('../ExcelFiles/' + sheet.sheet_name)
            multiSheet = input("Are there multiple sheets? y/n\n")
            if(multiSheet == "Y"):
                worksheet = workbook[input('What is the name of the worksheet to target?\n')]
            else:
                worksheet = workbook.active
            break
        except:
            answer = input("This workbook was not found! try again, Enter Q to quit the program, otherwise hit enter to continue.\n")
            if(answer == 'Q'):
                sys.exit('You have quit the program!')
        
    colDiction= {}
    #following loop will return a dictionary of column letters
    numOfCols = sheet.totalCols()
    for i in range(1,numOfCols):
        colDiction['col{0}'.format(i)] = sheet.returnCols()

    for i in range(1,numOfCols):
        rowForWs = 1
        for row in range(sheet.starting_row, worksheet.max_row + 1):
            ws.cell(row = rowForWs, column = i).value = worksheet[colDiction['col{0}'.format(i)] + str(row)].value
            rowForWs += 1
            print("process complete")
            
    print(sheet.sheet_name)
