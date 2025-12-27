from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")
driver.find_element(By.NAME, "uname").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("pass")
driver.find_element(By.NAME, "SUBMIT").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Schedule Courses").click()

time.sleep(5)





driver.find_element(By.XPATH,"/html/body/table[2]/tbody[1]/tr/td/div/p/table/tbody/tr/td/table/tbody/tr/td/div/table[2]/tbody/tr[3]/td[5]/div/a/img").click()

time.sleep(5)
ddm1=Select(driver.find_element(By.NAME,"instructor"))

for inst in ddm1.options:
    print(inst.text)

print(len(ddm1.options))

#Verify select instructor is displayed by default
displayed=ddm1.first_selected_option
print(displayed.text)

if(displayed.text=="Select Instructor"):
    print("PASS")
else:
    print("FAIL")

ddm2 = Select(driver.find_element(By.NAME,"ClassID"))

for classroom in ddm2.options:
        print(classroom.text)

print(len(ddm2.options))

    # Verify select classroom is displayed by default
displayed1 = ddm2.first_selected_option
print(displayed1.text)

if (displayed1.text == "Select Classroom"):
        print("PASS")
else:
        print("FAIL")

for id in ddm2.options:
        print(id.text)
        if(id.text=='BRDM1'):
                print('YES')
                break
        else:
                print('NO')