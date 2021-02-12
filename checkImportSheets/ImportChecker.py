import openpyxl
from openpyxl import load_workbook

toImportWb = openpyxl.load_workbook('ExcelSheets/' + input('Enter name of the sheet that is staged to be imported\n')+ '.xlsx')
toImportWs = toImportWb.active

fromMagentoWb = openpyxl.load_workbook('ExcelSheets/' + input('Enter name of the sheet that was exported from Magento\n')+ '.xlsx')
fromMagentoWs = fromMagentoWb.active


for row1 in range(2, toImportWs.max_row):
    sku1 = toImportWs['A' + str(row1)].value
    print(sku1)
    toImportWs['N' + str(row1)].value = '0'

    #TODO: Add feature to import pictures from source
    for row2 in range(2, fromMagentoWs.max_row + 1):
        sku2 = fromMagentoWs['A' + str(row2)].value
        if(sku1 == sku2):
            if(fromMagentoWs['C' + str(row2)].value != 'Default' or fromMagentoWs['C' + str(row2)].value != None):
                #Add feature to take the data in the cell and replace
                #data in the cell of excel sheet that will be imported
                toImportWs['C' + str(row1)].value = fromMagentoWs['C' + str(row2)].value
                
                if(fromMagentoWs['E' + str(row2)].value != None):
                    toImportWs['E' + str(row1)].value = fromMagentoWs['E' + str(row2)].value

                if(fromMagentoWs['N' + str(row2)].value != None):
                    toImportWs['N' + str(row1)].value = fromMagentoWs['N' + str(row2)].value
                
                if(fromMagentoWs['G' + str(row2)].value != None):
                    toImportWs['G' + str(row1)].value = fromMagentoWs['G' + str(row2)].value

toImportWb.save('toImport.xlsx')
