import openpyxl
#from openpyxl import load_workbook, Workbook


def GetWorkBooks():
    workbook1 = openpyxl.load_workbook( 'ExcelFiles/' + input('Enter name of first excel file:\n')+ '.xlsx')
    worksheet1 = workbook[input('Enter name of first worksheet:\n')]

    workbook2 = openpyxl.load_workbook('ExcelFiles/' + input('Enter name of second excel file:\n') + '.xlsx')
    worksheet2 = workbook[input('Enter name of second worksheet\n')]
    for row1 in range(2, worksheet1.max_row+1):
            sku1 = worksheet1['C' + str(row1)].value
            for row2 in range(2, worksheet2.max_row+1):    
                sku2 = worksheet2['C' + str(row2)].value
                if(sku1 == sku2):
                    #AddtoWorkBook(row1)
                break

def AddtoWorkbook(wsRow):
    #TODO: create a new workbook so the program can use the cells

if __name__ == '__main__':

    GetWorkBooks()
