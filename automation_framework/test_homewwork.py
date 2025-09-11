from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import time

#Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open URL
driver.get("https://www.wikipedia.org/")

#Wait for the page to load
time.sleep(2)

#Print URL
print(f"Page URL is: {driver.current_url}")

#Print title
print(f"Page title is: {driver.title}")

'''#switch to alert
alert = driver.switch_to.alert
alert.dismiss()
print("Alert dismissed")'''

#Find the search box using its name attribute value
search_box = driver.find_element(By.ID, "searchInput")

#Type in search box
search_box.send_keys("shopee")
search_box.submit()

#Wait for loading
time.sleep(2)

#Print URL
print(f"Page URL is: {driver.current_url}")

#assert checkpoint
heading = driver.find_element(By.ID, "firstHeading")
assert heading.is_displayed()
print(f"Heading check passed" )

#go back and forward
driver.back()
time.sleep(2)
print(f"Page Url is: {driver.current_url} previous page passed")


driver.forward()
time.sleep(2)
print(f"Page Url is: {driver.current_url} next page passed")

#Close the browser
driver.quit()

#End of code
print("Test completed.")
