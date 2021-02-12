import openpyxl
from openpyxl import load_workbook

toImportWb = openpyxl.load_workbook('ExcelSheets/' + input('Enter name of the sheet that is staged to be imported')+ '.xlsx')
toImportWs = toImportWb.active

fromMagentoWb = openpyxl.load_workbook('ExcelSheets/' + input('Enter name of the sheet that was exported from Magento')+ '.xlsx')
fromMagentoWs = fromMagentoWb.active


for row1 in range(2, toImportWs.max_row):
    sku1 = toImportWs['A' + str(row1)].value
    print(sku1)
    for row2 in range(2, fromMagentoWs.max_row + 1):
        sku2 = fromMagentoWs['A' + str(row2)].value
        print(sku2)
        if(sku1 == sku2):
            if(fromMagentoWs['C' + str(row2). value != 'Default']):
                #Add feature to take the data in the cell and replace
                #data in the cell of excel sheet that will be imported
