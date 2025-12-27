from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
# username
driver.find_element(By.NAME,"username").send_keys("admin.admin")
#password
driver.find_element(By.NAME,"password").send_keys("welcome")
#Click login
driver.find_element(By.NAME,"SUBMIT").click()
time.sleep(60)
#Click the PO named TORcat2014-105 in the list seen
driver.find_element(By.LINK_TEXT,"TORcat2014-105").click()
# #quantity
q=driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody[1]/tr[2]/td/div/table[3]/tbody/tr/td/form/table/tbody[1]/tr/td/table/tbody/tr[4]/td/table/tbody/tr[3]/td/table/tbody/tr[6]/td[5]/div/b/input").get_attribute("value")
print(q)
# #get attrubute retun type is string...so even if the textbox shows number 2, it is string. Convert to int for calculation
# q1=int(q)
# print(q1)
# #price
# p=driver.find_element(By.XPATH,"//tbody/tr[6]/td[6]/div[1]/b[1]/input[1]").get_attribute("value")
# print(p)
# p1=int(p)
# print(p1)
#
# total=driver.find_element(By.XPATH,value="//tbody/tr[6]/td[7]/div[1]/b[1]/font[1]").text
# print("Total is:",total)
# #extract and remove the dollar sign
# total1=total[2:]
# #convert to int
# total2=int(total1)
# print("Total after converting to integer:",total2)
#calculation
# my_total=q1*p1
# print(my_total)
#
# if(my_total==total2):
#     print("TC passed")
# else:
#     print("TC failed")
