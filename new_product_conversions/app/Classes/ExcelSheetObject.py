class ExcelSheet:
    
    def __init__(self, sheet_name):

        try:
            self.sheet_name = sheet_name
        except:
            print("An error ocurred")

    def returnCols(self):

        col = input("The column letter for Python:\n")

        return col
            
if __name__ == '__main__':

    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    col = sheet.returnCols()
    print(sheet.sheet_name)
    print(col)
