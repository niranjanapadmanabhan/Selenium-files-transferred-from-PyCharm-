from selenium import webdriver
import time
#To open chrome browser
driver=webdriver.Chrome()   #NOTE:C should be capital, else it will give error
#To open edge browser
#driver=webdriver.Edge()
#To open Google URL
driver.get("https://www.google.com")
# To introduce a delay of 5 seconds so that google stays for 5 seconds.
time.sleep(5)
print(driver.title)  #This prints the title of the page that was opened above which is Google in the result window down.

driver.get("https://www.facebook.com")
time.sleep(5)
print(driver.current_url) # Prints Facebook URL in the result window down
#To go back to the page of google
driver.back()
time.sleep(5)
#To go forward to the page of facebook
driver.forward()
time.sleep(5)
#To refresh the page of facebook
driver.refresh()
time.sleep(5)
#driver.close()
#To maximize the window
driver.maximize_window()
