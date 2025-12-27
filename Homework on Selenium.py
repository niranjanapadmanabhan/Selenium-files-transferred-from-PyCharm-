from selenium import webdriver
import time
#Open Chrome Browser
driver=webdriver.Chrome()
#Maximize the window
driver.maximize_window()
driver.get("https://www.amazon.com")
time.sleep(5)
#Get the title of Amazon
print(driver.title)
#Navigate to Youtube
driver.get("https://www.youtube.com")
print(driver.current_url)
#Go back
driver.back()
time.sleep(5)
#Go forward
driver.forward()
time.sleep(5)
#Refresh
driver.refresh()