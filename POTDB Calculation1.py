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
time.sleep(35)
#Click the PO named TORcat2014-105 in the list seen
driver.find_element(By.LINK_TEXT,"TORmax2014-116").click()

#TOTAL1 CALCULATION
t1=driver.find_element(By.XPATH,"//tbody/tr[6]/td[7]/div[1]/b[1]/font[1]").text
print("T1 is:",t1)
#extract the number
t1_extracted=t1[3:]
#convert to integer
t1_final=int(t1_extracted)
print("Total1 is:",t1_final)

#TOTAL2 CALCULATION
t2=driver.find_element(By.XPATH,"//tbody/tr[7]/td[7]/div[1]/b[1]/font[1]").text
print("T2 is:",t2)
#extract the number
t2_extracted=t2[3:]
#convert to integer
t2_final=int(t2_extracted)
print("Total2 is:",t2_final)


#TOTAL3 CALCULATION
t3=driver.find_element(By.XPATH,"/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[3]/tbody[1]/tr[1]/td[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[8]/td[7]/div[1]/b[1]/font[1]").text
print("T3 is:",t3)
#extract the number
t3_extracted=t3[3:]
#convert to integer
t3_final=int(t3_extracted)
print("Total3 is:",t3_final)

#TOTAL4 CALCULATION
t4=driver.find_element(By.XPATH,"//tbody/tr[9]/td[7]/div[1]/b[1]/font[1]").text
print("T4 is:",t4)
#extract the number
t4_extracted=t4[3:]
#convert to integer
t4_final=int(t4_extracted)
print("Total4 is:",t4_final)

#TOTAL5 CALCULATION
t5=driver.find_element(By.XPATH,"//tbody/tr[10]/td[7]/div[1]/b[1]/font[1]").text
print("T5 is:",t5)
#extract the number
t5_extracted=t5[3:]
#convert to integer
t5_final=int(t5_extracted)
print("Total5 is:",t5_final)

Total_sum=driver.find_element(By.XPATH,"//tbody/tr[11]/td[7]/b[1]/font[1]").text
#extract the number
Total_sum_extracted=Total_sum[3:]
#convert to integer
Total_sum_final=int(Total_sum_extracted)
print("Final sum is:",Total_sum_final)
Total_sum_calculated=t1_final+t2_final+t3_final+t4_final+t5_final
print("Final sum calculated is:",Total_sum_calculated)
if(Total_sum_extracted==Total_sum_calculated):
    print("TC Passed")
else:
    print("TC failed")
