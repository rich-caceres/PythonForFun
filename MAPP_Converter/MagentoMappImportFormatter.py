import openpyxl
import re
from openpyxl import load_workbook


def CheckMapp(Worksheet1, Worksheet2):

    #Workbook1 = openpyxl.load_workbook('ExcelFile/'+ input('Enter name of excel file from magento:\n') + '.xlsx', keep_vba=False)
    #Worksheet1 = Workbook1.active

    #Workbook2 = openpyxl.load_workbook('ExcelFile/' + input('Enter name of excel file with MAPP pricing:\n')+ '.xlsx', keep_vba = False)
    #Worksheet2 = Workbook2[input('Enter the name of the worksheet with MAPP pricing:\n')]

    startRowMapp = input('Enter the starting row for Mapp Sheet:\n')
    colWithMapp = input('Enter column letter with MAPP:\n')
    colWithMsrp = input('Enter column letter with MSRP:\n')

    for row1 in range(2, Worksheet1.max_row):
        sku1 = Worksheet1['A' + str(row1)].value
        sku1 = re.sub(".*\\s", "", sku1)
        print(sku1)

        for row2 in range(int(startRowMapp), Worksheet2.max_row):
            sku2 = Worksheet2['B' + str(row2)].value

            if(sku1 == sku2):
                print('Matching Sku found, adding mapp and msrp')
                mapp = Worksheet2[colWithMapp + str(row2)].value
                msrp = Worksheet2[colWithMsrp + str(row2)].value
                Worksheet1['E' + str(row1)].value = msrp
                Worksheet1['F' + str(row1)].value = mapp
                break

if __name__ == "__main__":

    Workbook1 = openpyxl.load_workbook('ExcelFile/'+ input('Enter name of excel file from magento:\n') + '.xlsx', keep_vba=False)
    Worksheet1 = Workbook1.active

    Workbook2 = openpyxl.load_workbook('ExcelFile/' + input('Enter name of excel file with MAPP pricing:\n')+ '.xlsx', keep_vba = False)
    Worksheet2 = Workbook2[input('Enter the name of the worksheet with MAPP pricing:\n')]


    CheckMapp(Worksheet1, Worksheet2)
