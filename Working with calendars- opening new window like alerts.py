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
print(main_window)  #prints Id of parent window

all_windows=driver.window_handles
print(all_windows)  #prints Id of parent window and child window. Everytime we run , the id numbers change.

for window in all_windows:
    if (window != main_window):
        driver.switch_to.window(window)
    # driver.find_element(By.LINK_TEXT,value="27").click()
#time.sleep(5)

# THE WHOLE CALENDAR TABLE
table = driver.find_element(By.XPATH, value="//body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]")
# PRINTING THE DATE TABLE AS TEXT ON SCREEN
print(table.text)

# DELETING WEB ELEMENTS - TABLE HEADER AND ROW, WE NEED ONLY TABLE DATA.
# TAKING OUT <TR> AND <TH> AND KEEPING ONLY <TD> I.E. EXTRACT TABLE DATA
#also we have many table data, so use find elements and not find_element.
td_tags = table.find_elements(By.TAG_NAME, value="td")
print(td_tags)

#loop the table calendar data
for td in td_tags:
    print(td.text)
    if (td.text == "2"):
        driver.find_element(By.LINK_TEXT, td.text).click()
        break
    else:
       print("Test case failed")