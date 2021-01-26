import openpyxl
import re
from openpyxl import load_workbook


def GetWorkBooks():
    newWorkbook = openpyxl.Workbook()
    ws= newWorkbook.active
    
    workbook1 = openpyxl.load_workbook( 'ExcelFiles/' + input('Enter name of first excel file:\n')+ '.xlsx')
    worksheet1 = workbook1[input('Enter name of first worksheet:\n')]

    workbook2 = openpyxl.load_workbook('ExcelFiles/' + input('Enter name of second excel file:\n') + '.xlsx')
    worksheet2 = workbook2[input('Enter name of second worksheet\n')]
    rowNum = 1
    
    for row1 in range(2, worksheet1.max_row):
            sku1 = worksheet1['A' + str(row1)].value
            sku1 = re.sub(".*\\s", "", sku1)
            print(sku1)
            for row2 in range(2, worksheet2.max_row+1):
                sku2 = worksheet2['C' + str(row2)].value
                if(sku1 == sku2):
                    print(sku1 + " " + sku2 + " are the same. Starting the data entry process.")
                    for nCol in range(1, worksheet2.max_column + 1): 
                        rowData= worksheet2.cell(row= row2, column= nCol)
                        ws.cell(row = rowNum, column= nCol).value = rowData.value
                    print('Row has been entered')
                    rowNum = rowNum + 1
                        
    newWorkbook.save('temp.xlsx')
            
                    

#def AddtoWorkbook(wsRow, newWorkbook):
    
    #TODO: create a new workbook so the program can use the cells
    #TODO: add the row to the new workbook
    #TODO: see the data being added to the workbook

if __name__ == '__main__':

    GetWorkBooks()
