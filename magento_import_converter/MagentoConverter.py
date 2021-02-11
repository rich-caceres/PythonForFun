import openpyxl
from openpyxl import load_workbook
import re

def OpenWorkbook():
    #opens the workbook
    toConvertWb = openpyxl.load_workbook(input('enter the name of workbook\n') + '.xlsx')
    toConvertWs = toConvertWb[input('Enter name of the worksheet to open:\n')]

    useOfScript = input('Would you like to (1)convert for import or (2) replace skus? type 1 or 2 respectively\n')

    #if user wants to convert for import
    if int(useOfScript) == 1:
        #opens the base file used for import in Magento
        importWb = openpyxl.load_workbook('catalog_product.xlsx')
        importWs = importWb['catalog_product']
        
        #loops throughout the entire workbook to get the correct information
        for row in range(2, toConvertWs.max_row + 1):
            #checks that it is base unit before pulling information
            if(toConvertWs['G' + str(row)].value != None):
                if (toConvertWs['G' + str(row)].value.lower() == 'base_unit_or_each'):
                    #getting all information from row
                    sku = toConvertWs['C' + str(row)].value
                    itemName = toConvertWs['O' + str(row)].value
                    productOnline = '1'
                    weight = toConvertWs['AE' + str(row)].value
                    picture = ''

                    if(weight == None):
                        weight = ''
                        productOnline= '2'
                    
                    #checks to see if item name is none, if so changes online status to not online
                    if(itemName == None):
                        itemName = ''
                        productOnline = '2'

                    #checks for a picture on the row
                    if(toConvertWs['AG' + str(row)].value != None):
                        picture = toConvertWs['AG' + str(row)].value
                    elif(toConvertWs['AH' + str(row)].value != None):
                        picture = toConvertWs['AH' + str(row)].value
                    else:
                        #remove string for no picture
                        picture = 'no picture'
                        productOnline = '2'
                
                    ConvertToImport(sku, productOnline, itemName, weight, picture, importWs)
    #if user wants to replace sku's
    elif int(useOfScript) == 2:
        wbToUse = openpyxl.load_workbook(input('enter the name of workbook:\n') + '.xlsx')
        wsToUse =  wbToUse[input('Enter name of the worksheet to open:\n')]
        wsToUse = ReplaceSku(toConvertWs, wsToUse)
        wbToUse.save('ConvertedFile.xlsx')
    else:
        print("Program will now exit.")
                                     
def ReplaceSku(wsUse, toConvWs):
     
     #TODO: Add Function to replace sku's between two worksheets
    print("to replace Sku's")
    for row in range(2, wsUse.max_row + 1):
            sku = wsUse['A' + str(row)].value
            if(sku == None):
                break
            print(sku)
            trimSku = re.sub(".*\\s", "", sku)
            
            for row2 in range(2, toConvWs.max_row + 1):
                sku2 = toConvWs['C' + str(row2)].value
                if(trimSku == sku2):
                    print('Replacing Sku')
                    toConvWs['C' + str(row2)].value = sku
    return toConvWs
def ConvertToImport(sku, productStatus, itemName, weight, picture, worksheet):
    #TODO: Add function to convert to import sheet
    print("Sku: " + sku + " Item Name: " + itemName + " Product Status: " + productStatus + " Weight: " + weight + " Picture: " + picture)
    category = 'Default/Products'
    productType = 'simple'
    productWebsite = 'base'
    
if __name__ == "__main__":

    OpenWorkbook()
