class ExcelSheet:
    
    def __init__(self, sheet_name):
        try:
            self.sheet_name = sheet_name
        except:
            print("An error ocurred")

    def totalCols(self):
        while True:
            try:
                return int(input("how many columns do you want to check?\n")) + 1
            except:
                print("You did not type a number! try again")

    def returnCols(self):
        return input("The column letter for Python:\n")

            
if __name__ == '__main__':

    sheet = ExcelSheet(input('Please enter excel sheet name:\n'))
    col = sheet.returnCols()
    totalCols = sheet.totalCols()
    print(totalCols)
    print(sheet.sheet_name)
    print(col)
