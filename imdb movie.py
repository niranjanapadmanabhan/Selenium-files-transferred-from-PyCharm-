from selenium import webdriver

driver= webdriver.Chrome()

driver.get("https://www.imdb.com/")

driver.maximize_window()
driver.refresh()

# what i think is the title
title= "movies"

actual_title= driver.title
print(actual_title)

if(title==actual_title):
    print("Test Case Passed")
else:
    print("Test Case Failed")

#compare url and we need test case passed.

print(driver.current_url)
var="https://www.imdb.com/"
URL=driver.current_url
if(var==URL):
    print("TC passed")
else:
    print("TC failed")