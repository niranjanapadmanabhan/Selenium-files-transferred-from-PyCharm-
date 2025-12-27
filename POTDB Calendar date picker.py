from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
# username
driver.find_element(By.NAME,"username").send_keys("admin.admin")
#password
driver.find_element(By.NAME,"password").send_keys("welcome")
#Click login
driver.find_element(By.NAME,"SUBMIT").click()
#click create PO button
driver.find_element(By.LINK_TEXT,"Create PO").click()
#Click Select Date Calendar hyperlink
driver.find_element(By.LINK_TEXT,"Select Date").click()

#Give these statements after clicking the select date calendar link because then only we get two windows.
main_window=driver.current_window_handle
print(main_window)
all_windows=driver.window_handles
print(all_windows)

for x in all_windows:
    if x!=main_window:
        driver.switch_to.window(x)

table=driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table")
print(table.text)
#Extract only the table data from the entire table . Also, note it is find elements,and not find element.
td_tags=table.find_elements(By.TAG_NAME, value="td")
#print(td_tags)

#  loop the table calendar data
for td in td_tags:
    print(td.text)
    if (td.text == "2"):
        driver.find_element(By.LINK_TEXT, td.text).click()
        break
    else:
        print("Test case failed")