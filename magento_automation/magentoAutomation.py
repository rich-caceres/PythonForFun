from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
from excelfileWithOpenPyXl import *
import yaml
import sys
import time

configuration = yaml.safe_load(open('magentoLogin.yml'))
user = configuration['magento_user']['username']
magPassword = configuration['magento_user']['password']

filepath= "ExcelFiles\\"
workbook = load_workbook(filepath + input('Enter name of excel file:\n') + '.xlsx')
worksheet = workbook[input('Enter name of worksheet:\n')]#still need to add method to grab the cell content

#print(f'{user} {magPassword}')

driver = webdriver.Chrome()

#loging the user in
def login(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_class_name(submit_buttonId).click()

#clears the search bar in catalog
def clearSearchBar(productField):
    driver.find_element_by_id(productField).clear()
    wait_till_complete = input("press enter once load completes")

#getting to catalog once the user moves away from catalog
def get_to_catalog():
    element= driver.find_element_by_id('menu-magento-catalog-catalog')
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    wait_till_complete= input("press enter once complete")
    element= driver.find_element_by_class_name('item-catalog-products')
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    wait_till_complete= input("press enter once complete")

# finds the search bar and uses the SKU from the excel sheet to search for the product
def searchProduct(productSku, productField):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, productField)))
    driver.implicitly_wait(60)
    #driver.find_element_by_id(productField).send_keys(product, u'\ue007')
    element.send_keys(productSku['sku'], u'\ue007')
    print(f"Product description in spreadsheet is {productSku['descrip']}")
    wait_till_complete = input("press enter once load completes")
    element = driver.find_element_by_class_name('data-row')
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

#finds Attribute set dropdown and opens it to quickly type attribute set
def changeContent():
    element = driver.find_element_by_class_name('admin__action-multiselect-text')
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

#counter used to keep track of row in the  excel sheet, orientation is established at runtime
def rowCounter(row, orientation):
    if orientation == 'y':
        return row - 1
    else:
        return row + 1

def save():
    element = driver.find_element_by_id('save-button')
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    
def back():
    element = driver.find_element_by_id('back')
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


#Used for searching and updating products in magento
def SearchAndUpdate(cells, completed, row, columns, orientation):
    wait = ''
    while(wait.lower() != 'n'):

            clearSearchBar("fulltext")

            if(returnCellVal(cells['cell1'], cells['cell2'], worksheet) == None):
                print(f'End of worksheet reached. You completed {completed} rows.')
                break
        
            searchProduct(returnCellVal(cells['cell1'], cells['cell2'], worksheet), "fulltext")
            driver.implicitly_wait(10)
            changeContent()
            completed = completed + 1
            print(f'You have completed {completed}')
            row = rowCounter(row, orientation)
            cells['cell1'] = columns['column1'] + str(row)
            cells['cell2'] = columns['column2'] + str(row)
            wait = input('Would you like to continue searching?\n')
            back()

#Used to add new products from Spreadsheet
def AddNewProduct(cells, completed, row, columns, orientation):
    wait = ''
    while(wait.lower() != 'n'):

        if(returnCellVal(cells['cell1'], cells['cell2'], worksheet) == None):
            print(f'End of worksheet reached. You added {completed} rows.')
            break

        element = driver.find_element_by_id('add_new_product-button')
        webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
        wait = input('Press enter when load completes')

        products = returnCellVal(cells['cell1'], cells['cell2'], worksheet)

        element = driver.find_element_by_name('product[sku]')
        element.send_keys(products['sku'])
        element = driver.find_element_by_name('product[name]')
        element.send_keys(products['descrip'])
        element = driver.find_element_by_name('product[price]')
        element.send_keys('0.00')
        element = driver.find_element_by_name('product[uom]')
        element.send_keys('EA')

        wait = input('Would you like to save this product?\n')

        if wait.lower() == 'n':
            saveAnswer = print('review before continuing, hit save if you made a mistake\n')
            back()
        else:
            save()
            saveAnswer = input('hit enter once completed with saving\n')
            back()

        row = rowCounter(row, orientation)
        cells['cell1']= columns['column1'] + str(row)
        cells['cell2']= columns['column2'] + str(row)
        wait = input('Would you like to continue adding? y/n')
        
    
if __name__ == '__main__':

    column = ''
    row = 0
    completed = 0
    orientation = None
    
    login("http://starsales.patracompany.com/admin_1b7unb/admin/index/index/key/c6a9c4978139a87c7b4119e779ddd95bc0bc2b10b3df7e8ba920db39048eaffb/", "username", user, "login", magPassword,"action-login")
    answer = input('Would you like to start entering data? y/n \n')
    orientation = input('Do you want to reverse count? y/n \n')
    
    if answer.lower() == 'y':
        orientation = input('Do you want to reverse count? y/n \n')
        #gets the columns required to start the search
        columns = {'column1': input('What is the column letter for Sku?\n'), 'column2': input('What is the column letter for description?\n')}
        #gets the rows to begin searching from.
        row = int(input('What is the beginning row number?\n'))
        cells = {'cell1': columns['column1'] + str(row), 'cell2': columns['column2'] + str(row)}
        print(f"The program will begin at the following cells: {cells['cell1']} and {cells['cell2']}\n")
        get_to_catalog()
    else:
        print('The application will now close in 5 seconds')
        time.sleep(5)
        driver.close()
        sys.exit()
            
    while True:
        answer = input('Would you like to (1)search or (2)add product? press 1 or 2 respectively.\n')

        try:
            if int(answer) == 1:
                SearchAndUpdate(cells, completed, row, columns, orientation)
            elif int(answer) == 2:
                AddNewProduct(cells, completed, row, columns, orientation)
            flowContinuance = input('Would you like to continue with this flow?')

            if flowContinuance != 'y':
                break
    
        except NameError:
            print('This is not a valid answer, try again')
       
