driver = webdriver.Chrome()
driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")
driver.find_element(By.NAME, "uname").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("pass")
driver.find_element(By.NAME, "SUBMIT").click()


driver.find_element(By.LINK_TEXT, "Schedule Courses").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Create New Course").click()

time.sleep(5)
ddm1=Select(driver.find_element(By.NAME, "Cat"))

ddm1.select_by_index(2)

driver.find_element(By.NAME, "Title").send_keys("qa7777000001")


ddm2=Select(driver.find_element(By.NAME, "course_Level"))
ddm2.select_by_index(1)
description= driver.find_element(By.NAME, "Description").get_attribute("value")

print(description)
driver.find_element(By.NAME, "Cert").click()

driver.find_element(By.NAME, "Submit").click()

driver.find_element(By.LINK_TEXT,"qa7777000001").click()

time.sleep(5)

description2= driver.find_element(By.NAME, "Description").get_attribute("value")


if (description2==description):
    print("test case passed")
else:
    print("test case failed")