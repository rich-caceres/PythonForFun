from openpyxl import load_workbook, Workbook


def GetWorkBooks():
    workbook = load_workbook( 'ExcelFiles/' + input('Enter name of excel file:\n')+ '.xlsx')
    worksheet = workbook[input('Enter name of worksheet:\n')]


if __name__ == '__main__':

    GetWorkBooks()
