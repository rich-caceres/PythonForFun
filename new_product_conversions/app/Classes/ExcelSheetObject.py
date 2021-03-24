class ExcelSheet:
    
    def __init__(self, sheet_name):
        try:
            self.sheet_name = sheet_name
        except:
            print("An error ocurred")

    def totalCols(self):
        return input("how many columns do you want to check?\n")

    def returnCols(self):
        return input("The column letter for Python:\n")

            
if __name__ == '__main__':

    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    col = sheet.returnCols()
    totalCols = sheet.totalCols()
    print(sheet.sheet_name)
    print(col)
