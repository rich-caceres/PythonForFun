import openpyxl
import re
import sys
from openpyxl import load_workbook, Workbook
from Classes.ExcelSheetObject import ExcelSheet


def workbookCheck():

    columnLetter = None
    while True:
        try:
            magentoSheet = ExcelSheet(input('Please enter the name of the Magento exported excel sheet:\n'), '', input('Enter starting row:\n'))
            excelSheetToCheck = ExcelSheet(input('Please enter the name of the excel sheet to check:\n'), input('Enter initial identifier for manufacturer:\n'), input('Enter starting row:\n'))
            mageXcelWorkbook = openpyxl.load_workbook('../ExcelFiles/' + magentoSheet.sheet_name)
            mageXcelSheet = mageXcelWorkbook.active
            XcelWorkbook = openpyxl.load_workbook('../ExcelFiles/' + excelSheetToCheck.sheet_name)
            XcelWorksheet = XcelWorkbook.active
            break
        except:
            answer = input("This work book was not found! press enter to try again. Enter the letter Q to quit the program")
            if(answer == 'Q'):
                sys.exit('You have quit the program!')


    for row1 in range(excelSheetToCheck.starting_row, XcelWorksheet.max_row + 1):
        if columnLetter is None:
            columnLetter= input('Please enter the column letter containing SKU on the sheet the contains the cross sell items:\n')
        Sku1 = XcelWorksheet['B' + str(row1)].value
        upsell_products = {}
        for row2 in range(magentoSheet.starting_row, mageXcelSheet.max_row + 1):
            Sku2 = str(mageXcelSheet['A' + str(row2)].value)
            Sku2 = re.sub(".*\\s", "", Sku2)
            if(Sku1 == Sku2):
                print(f'Entered if Statement {Sku1} == {Sku2}')#testing
                
                for cols in range(5, XcelWorksheet.max_column+1):
                    
                    if XcelWorksheet.cell(row = row1, column = cols).value is not None:
                        upsell_products['{0}'.format(cols)] =excelSheetToCheck.manu_ident + " " + XcelWorksheet.cell(row=row1, column=cols).value

                if bool(upsell_products):
                    #print('in second if for bool products')
                    #print(upsell_products)
                    for key in list(upsell_products):
                        print(upsell_products)
                        for rowCheck in range(magentoSheet.starting_row, mageXcelSheet.max_row+1):
                            #print(str(mageXcelSheet['A' + str(rowCheck)].value)[0:3]) #testing
                            if(str(mageXcelSheet['A' + str(rowCheck)].value)[0:3] != str(excelSheetToCheck.manu_ident)):
                                #print(upsell_products)#testing
                                if(rowCheck == mageXcelSheet.max_row):
                                    print(f'Deleted {upsell_products[key]}')
                                    upsell_products.pop(key)
                                continue
                            if(upsell_products[key] == mageXcelSheet['A' + str(rowCheck)].value):
                                print('values equal if')#testing
                                break
                            
                                
                    print(upsell_products)
                #print(upsell_products)#testing
                break
                        
    """ 
        loop through dictionary of upsell_products:        
            if dictionary of upsell products not in mageXcelSheet:
                delete the sku from dictionary
            else:
                continue
    """
if __name__ == '__main__':

    workbookCheck()
    print('Nothing is happening here yet')
