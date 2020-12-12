from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
import requests
import json
from selectorlib import Extractor
from time import sleep

driver = webdriver.Chrome()
selector = Extractor.from_yaml_file('selectors.yml')

#using selenium to scrape data

def GettingData(url):
    
    print("Downloading %s"%url)
    driver.get(url)
    
    driver.find_element_by_class_name('search-toggle').click()
    driver.find_element_by_id('txtSiteSearch').send_keys('PJ-100', u'\ue007')
    wait = input("press enter when complete")
    driver.find_element_by_class_name('pf-result-PJ-100').click()
    wait = input("press enter when complete")
    data=driver.page_source
    return selector.extract(data)

# product_data = []
    #with open("urls.txt",'r') as urllist, open('output.jsonl','w') as outfile:
    #for url in urllist.readlines():
with open('output.jsonl', 'w') as outfile:
    data = GettingData('https://www.wernerco.com/') 
    if data:
        json.dump(data,outfile)
        outfile.write("\n")
                # sleep(5)

