import openpyxl
#from openpyxl import load_workbook, Workbook


def GetWorkBooks():
    workbook1 = openpyxl.load_workbook( 'ExcelFiles/' + input('Enter name of first excel file:\n')+ '.xlsx')
    worksheet1 = workbook[input('Enter name of first worksheet:\n')]

    workbook2 = openpyxl.load_workbook('ExcelFiles/' + input('Enter name of second excel file:\n') + '.xlsx')
    worksheet2 = workbook[input('Enter name of second worksheet\n')]
    for row in range(2, worksheet.max_row+1):
            sku1 = worksheet1['C' + str(row)].value
            sku2 = 
            break

def AddtoWorkbook():
    

if __name__ == '__main__':

    GetWorkBooks()
