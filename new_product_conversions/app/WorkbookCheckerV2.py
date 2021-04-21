import openpyxl
import re
import sys
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet


def workbookCheck():

    while True:
        try:
            magentoSheet = ExcelSheet(input('Please enter the name of the Magento exported excel sheet:\n'), '', input('Enter starting row:\n'))
            excelSheetToCheck = ExcelSheet(input('Please enter the name of the excel sheet to check:\n'), '', input('Enter starting row:\n'))
            mageXcelSheet = openpyxl.load_workbook('../ExcelFiles/' + magentoSheet.sheet_name)
            XcelSheetToCheck = openpyxl.load_workbook('../ExcelFiles/' + excelSheetToCheck.sheet_name)
            break
        except:
            answer = input("This work book was not found! press enter to try again. Enter the letter Q to quit the program")
            if(answer == 'Q'):
                sys.exit('You have quit the program!')

        upsell_products = {}

    for row in range(excelSheetToCheck.starting_row, XcelSheetToCheck.max_row + 1):
        columnLetter = input('Enter column that contains the Sku for each product')
        Sku1 = XcelSheetToCheck['B' + str(row)].value

        for row1 in range(magentoSheet.starting_row, mageXcelSheet.max_row + 1):
            Sku2 = mageXcelSheet['A' + str(row)].value
            Sku2 = re.sub(".*\\s", "", Sku2)
            
            if(Sku1 == Sku2):
                print('Entered the if statement')
                        
    """ 
                if Sku1 matches Sku2:
                    create dictionary of upsell_products
        loop through dictionary of upsell_products:        
            if dictionary of upsell products not in mageXcelSheet:
                delete the sku from dictionary
            else:
                continue
    """
if __name__ == '__main__':

    workbookCheck()
    print('Nothing is happening here yet')
