from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")

#Finding the element for username
username=driver.find_element(By.NAME,value="uname")
#Typing admin for username
username.send_keys("admin")

#Finding element for password
password=driver.find_element(By.NAME,value="password")
#Typing pass for password
password.send_keys("pass")

#Finding element for Login button
login=driver.find_element(By.NAME,value="SUBMIT")
#To click the button login
login.click()
#time.sleep(5)

#Finding element for Schedule Courses
Schedule_Courses=driver.find_element(By.LINK_TEXT,value="Schedule Courses")

#To click the hyperlink Schedule Courses
Schedule_Courses.click()
driver.find_element(By.CSS_SELECTOR,"tr:nth-child(3) td:nth-child(5) div:nth-child(1) a:nth-child(1) > img:nth-child(1)").click()

#click the calendar link
driver.find_element(By.LINK_TEXT,"Select Date").click()

main_window=driver.current_window_handle
print(main_window)
all_windows=driver.window_handles
print(all_windows)

for x in all_windows:
    if x!=main_window:
        driver.switch_to.window(x)

fulldates=driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table")
print(fulldates.text)

#this table printed using above line has all contents including table row,table header etc...we need only table data i.e td..so next step is extracting only td.

td_tags=fulldates.find_elements(By.TAG_NAME,"td")
print(td_tags)

for td in td_tags:
    print(td.text)
    if (td.text == "2"):
        driver.find_element(By.LINK_TEXT, td.text).click()
        break
