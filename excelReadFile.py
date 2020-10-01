import xlrd

loc = (input("Enter path of file:\n"))

try:
    wb = xlrd.open_workbook(loc)    
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    print(sheet.nrows)

except:
    print('No such file exists')
