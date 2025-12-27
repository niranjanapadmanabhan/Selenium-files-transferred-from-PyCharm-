from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, value="username").send_keys("admin.admin")
driver.find_element(By.NAME, value="password").send_keys("welcome")
driver.find_element(By.NAME, value="SUBMIT").click()

#Clicking the Create PO link
driver.find_element(By.LINK_TEXT,value="Create PO").click()
time.sleep(10)
PO_NO=Select(driver.find_element(By.NAME,value="POopco"))

#Looping the ddm PO NO options and displaying them
for x in PO_NO.options:
    print(x.text)
#Printing the length of ddm

print("Length of PO No. options are:",len(PO_NO.options))

#Printing the option displayed by default in drop down menu
print("First option by default in drop down is:",PO_NO.first_selected_option.text)

OP_CO=Select(driver.find_element(By.NAME,value="OpCo"))

#Looping the ddm OP_CO options and displaying them
for x in OP_CO.options:
    print(x.text)
#Printing the length of ddm OP_CO

print("Length of OP_CO. options are:",len(OP_CO.options))

#Printing the option displayed by default in OP_CO drop down menu
print("First option by default in drop down is:",OP_CO.first_selected_option.text)


Supplier=Select(driver.find_element(By.NAME,value="Supplier"))

#Looping the ddm Supplier options and displaying them
for x in Supplier.options:
    print(x.text)
#Printing the length of ddm Supplier

print("Length of Supplier options are:",len(Supplier.options))

#Printing the option displayed by default in drop down menu
print("First option by default in drop down is:",Supplier.first_selected_option.text)

Shipping_Adr=Select(driver.find_element(By.NAME,value="shipping"))

#Looping the ddm Shipping address options and displaying them
for x in Shipping_Adr.options:
    print(x.text)
#Printing the length of ddm Shipping Address
print("Length of Shipping Address options are:",len(Shipping_Adr.options))

#Printing the option displayed by default in drop down menu
print("First option by default in drop down is:",Shipping_Adr.first_selected_option.text)

Billing_Adr=Select(driver.find_element(By.NAME,value="billing"))

#Looping the ddm Shipping address options and displaying them
for x in Billing_Adr.options:
    print(x.text)
#Printing the length of ddm Billing Address
print("Length of Billing Address options are:",len(Billing_Adr.options))

#Printing the option displayed by default in drop down menu
print("First option by default in drop down is:",Billing_Adr.first_selected_option.text)

driver.quit()