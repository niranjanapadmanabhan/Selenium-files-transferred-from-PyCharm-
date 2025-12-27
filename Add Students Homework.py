from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
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

#Click on Students
std=driver.find_element(By.LINK_TEXT,value="Students")
std.click()

time.sleep(3)

#Add Student
addstd=driver.find_element(By.LINK_TEXT,value="Add Student")
addstd.click()
time.sleep(4)

#Fill the form
fname=driver.find_element(By.NAME,value="fname")
fname.send_keys("Naina")
lastname=driver.find_element(By.NAME,value="lname")
lastname.send_keys("N")
time.sleep(2)
uname=driver.find_element(By.NAME,value="username")
uname.send_keys("Naina")
email=driver.find_element(By.NAME,value="email")
email.send_keys("hellothere@gmail.com")
time.sleep(2)
tel=driver.find_element(By.NAME,value="phone_code")
tel.send_keys("4165702899")
province=driver.find_element(By.CSS_SELECTOR,value="body > table:nth-child(5) > tbody:nth-child(1) > tr > td > table:nth-child(10) > tbody > tr > td > table > tbody > tr > td > div > form > table:nth-child(4) > tbody > tr > td > table > tbody:nth-child(1) > tr > td > table > tbody > tr:nth-child(17) > td > table > tbody > tr > td:nth-child(2) > p > select")
ddm=Select(province)
ddm.select_by_index(8)
time.sleep(4)
country=driver.find_element(By.XPATH,value="/html/body/table[2]/tbody[1]/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/div/form/table[2]/tbody/tr/td/table/tbody[1]/tr/td/table/tbody/tr[19]/td/table/tbody/tr/td[2]/p/select")
ddm1=Select(country)
ddm1.select_by_index(38)
time.sleep(4)
ZipCode=driver.find_element(By.NAME,value="Zip")
ZipCode.send_keys("M2N5X9")
#Click Add Student Button
buttonclick1=driver.find_element(By.NAME,value="submit")
buttonclick1.click()
time.sleep(4)
