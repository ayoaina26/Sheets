import gspread
import oauth2client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#For Webdriver and Gspread

PATH = 'C:\Python27\chromedriver.exe'
driver = webdriver.Chrome(PATH)

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("1ZIKFHMGNLzyE-cNUqwx8OuEFLreZlhr98gO7cqGmmQ8")
worksheet = sh.sheet1
res = worksheet.get('A2:C2')

print(res)

#Code starts
driver.get('https://www.humbleisd.net/hhs')
driver.maximize_window()

search = driver.find_element_by_id('search')
search.click()

bar = driver.find_element_by_id('gb-search-input')
bar.send_keys(str(res))
bar.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

time.sleep(300)

driver.quit()

#username.send_keys('ayo_theblackguy')
#username.send_keys(Keys.RETURN)
#driver.implicitly_wait(10)

